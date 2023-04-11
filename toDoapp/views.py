#from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet, GenericViewSet
from toDoapp.models import Project, ToDo
from toDoapp.serializers import ProjectModelSerializer, ToDoModelSerializer
from rest_framework.pagination import LimitOffsetPagination
from .filters import ProjectFilter
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser, BasePermission, \
     DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, SAFE_METHODS


#filterset_class = ProjectFilter


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10



class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS 


class IsDeveloper(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='developer').exists()
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user == obj.user:
            return True
        return False
       
    
   
    
    
class IsDeveloperReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.groups.filter(name='developer').exists()
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user in obj.users.all():
            return True
        return False
        
    



class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS 

    
class IsProjectOwner(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        projects = Project.objects.filter(users=request.user)
        users = [user for project in projects for user in project.users.all()]
        #print('Владельцы проектов', users)
        #print('Авторизованный пользователь', request.user)
        if request.user in users:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user in obj.users.all():
            return True
        return False
         
      
    
class ProjectModelViewSet(ModelViewSet):
    pagination_class = ProjectLimitOffsetPagination
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    #filterset_fields = ['name', 'users']
    permission_classes = [IsProjectOwner | IsAdminUser | IsDeveloperReadOnly]


    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        print("Search name:", name)
        if name:
            return Project.objects.filter(name__icontains=name)
        return Project.objects.all()
    

class IsProjectOwner2(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        projects = Project.objects.filter(users=request.user)
        users = [user for project in projects for user in project.users.all()]
        #print('Владельцы проектов', users)
        #print('Авторизованный пользователь', request.user)
        if request.user in users:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user == obj.user:
            return True
        return False
    
    
class ToDoModelViewSet(ModelViewSet):
    pagination_class = ToDoLimitOffsetPagination
    queryset = ToDo.objects.filter(is_active=True)
    serializer_class = ToDoModelSerializer
    permission_classes = [IsAdminUser | IsDeveloper | IsProjectOwner2]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


    def get_queryset(self):
        queryset = ToDo.objects.filter(is_active=True)
        project_id = self.request.query_params.get('project_id', None)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if project_id:
            return ToDo.objects.filter(project=project_id)
    
        if start_date and end_date:
            return ToDo.objects.filter(created__range=[start_date, end_date])
        
        return queryset
