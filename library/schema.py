import graphene
from graphene_django import DjangoObjectType
from authors.models import Author, Book
from toDoapp.models import Project, ToDo
from authapp.models import User


#class Query(graphene.ObjectType):
#    hello = graphene.String(default_value="Hi!")

#schema = graphene.Schema(query=Query)
class UserObjectType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class AuthorObjectType(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'


class BookObjectType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'


class ProjectObjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class TodoObjectType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UserObjectType)
    all_todos = graphene.List(TodoObjectType)
    all_projects = graphene.List(ProjectObjectType)
    all_authors = graphene.List(AuthorObjectType)
    def resolve_all_authors(self, info):
        return Author.objects.all()
    

    def resolve_all_users(self, info):
        return User.objects.all()
    
    def resolve_all_todos(self, info):
        return ToDo.objects.all()
    
    def resolve_all_projects(self, info):
        return Project.objects.all()
    
    #Дать всех проекты в которых есть пользователь c определённым id
    projects_by_user_id = graphene.List(ProjectObjectType, user=graphene.Int(required=True))
    def resolve_projects_by_user_id(self, info, user):
        return Project.objects.filter(users=user)
    

    #Дать всех пользователей которые учавствуют в проекте с определенным названием. Вернёт список, если есть одинаковые названия
    users_by_projects_name = graphene.List(ProjectObjectType, name=graphene.String(required=True))
    def resolve_users_by_project_name(self, info, name):
        return Project.objects.filter(name=name)
    
    #Дать всех пользователей которые учавствуют в проекте с определенным названием. Для единичного получения в случае если имена в базе уникальные
    get_users_by_project_name = graphene.Field(ProjectObjectType, name=graphene.String(required=True))
    def resolve_users_by_project_name(self, info, name):
        return Project.objects.get(name=name)
        
    
    """
    так выглядят запросы на чтение 
{
  allTodos  {
    id
    user {
      id
      username
    }
    project {
      id
      name
      users {
        id
      }
    }
  }
  allProjects{
    id
    name
    users{
      username
    }
  }
  allUsers{
    id
    username
    firstName
    lastName
    isActive
    isSuperuser
  }
  
}

рекурсивный запрос с использованием set "название_модели_set"
{
  allUsers{
    username
    projectSet{
      id
      name
      users{
        id
        username
      }
    }
  }
} 

Дать имена всех проектов в которых есть пользователь c определённым id
{
  projectsByUserId(user: 1){
    name
  }
}

Дать всех пользователей которые учавствуют в проекте с определенным названием

{
  usersByProjectsName(name: "test5"){
    name
    users{
      id
      username
    }
  }
}
"""
    

    all_books = graphene.List(BookObjectType)
    def resolve_all_books(self, info, pk):
        # return Author.objects.get(pk=1).book_set.all()
        return Author.objects.all()
    

    #get_author_by_id = graphene.List(AuthorObjectType, pk=graphene.Int(required=True))
    get_author_by_id = graphene.Field(AuthorObjectType, pk=graphene.Int(required=True))
    def resolve_get_author_by_id(self, info, pk):
        return Author.objects.get(pk=pk)
    

    get_author_by_name = graphene.List(AuthorObjectType,
                                    first_name=graphene.String(required=False),
                                    last_name=graphene.String(required=False)
                                    )

    def resolve_get_author_by_name(self, info, first_name=None, last_name=None):
        if not first_name and not last_name:
            return Author.objects.all()
        params = {}
        if first_name:
            params['first_name__icontains'] = first_name
        if last_name:
            params['last_name__icontains'] = last_name
        return Author.objects.filter(**params)


class AuthorCreateMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        birthday_year = graphene.Int(required=True)

    author = graphene.Field(AuthorObjectType)

    @classmethod
    def mutate(cls, root, info, first_name, last_name, birthday_year):
        author = Author(first_name=first_name, last_name=last_name, birthday_year=birthday_year)
        author.save()
        return cls(author)


class AuthorUpdateMutation(graphene.Mutation):
    class Arguments:
        pk = graphene.Int(required=True)
        first_name = graphene.String(required=False)
        last_name = graphene.String(required=False)
        birthday_year = graphene.Int(required=False)

    author = graphene.Field(AuthorObjectType)

    @classmethod
    def mutate(cls, root, info, pk, first_name=None, last_name=None, birthday_year=None):
        author = Author.objects.get(pk=pk)
        if first_name:
            author.first_name = first_name
        if last_name:
            author.last_name = last_name
        if birthday_year:
            author.birthday_year = birthday_year

        if first_name or last_name or birthday_year:
            author.save()
        return cls(author)


class Mutations(graphene.ObjectType):
    create_author = AuthorCreateMutation.Field()
    update_author = AuthorUpdateMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)


