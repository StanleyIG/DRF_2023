import React from 'react';
import logo from './logo.svg';
import './App.css';
import Menu from './components/Menu'
import AuthorList from './components/Author.js'
import UserList from './components/Users';
import BookList from './components/books';
import ProjectList from './components/Project';
import ToDoList from './components/ToDo';
import AuthorBookList from './components/AuthorBook';
import ProjectToDos from './components/ProjectToDos';
import LoginForm from './components/LoginForm.js';
import BookForm from './components/BookForm';
import TodoForm from './components/ToDoForm';
import axios from 'axios'
import {HashRouter, BrowserRouter, Route, Link, Navigate, Routes, useLocation} from 'react-router-dom'


const NotFound = () => {
  let {pathname} = useLocation()

  return (
      <div>
          Page "{pathname}" not found
      </div>
  )

}


class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'authors': [],
      'users': [],
      'books': [],
      'projects': [],
      'todos': [],
      'token': '',
      'redirect': false
    }
  }


  deleteBook(bookId) {
    let headers = this.getHeaders()

    axios
        .delete(`http://127.0.0.1:8000/api/books/${bookId}`, {headers})
        .then(response => {
            this.setState({
                'books': this.state.books.filter((book) => book.id != bookId)
            })
        })
        .catch(error => {
            console.log(error)
        })
//        console.log(bookId)
}


  createBook(name, authors) {
    //        console.log(title, authors)
    
            let headers = this.getHeaders()
    
            axios
                .post('http://127.0.0.1:8000/api/books/', {'name': name, 'authors': authors}, {headers})
                .then(response => {
                    this.setState({
                      'redirect': '/books'
                    }, this.getData)
                })
                .catch(error => {
                    console.log(error)
                })
        }

        createToDo(tagtext, isactive, project, user) {
          //        console.log(title, authors)
          
                  let headers = this.getHeaders()
          
                  axios
                      .post('http://127.0.0.1:8000/api/ToDo_notes/', {'tag_text': tagtext, 'is_active': isactive, 'project': project, 'user': user}, {headers})
                      .then(response => {
                          this.setState({
                              'redirect': '/todos'
                          }, this.getData)
                      })
                      .catch(error => {
                          console.log(error)
                      })
              }

              deleteTodo(todoId) {
                let headers = this.getHeaders()
            
                axios
                    .delete(`http://127.0.0.1:8000/api/ToDo_notes/${todoId}`, {headers})
                    .then(response => {
                        this.setState({
                            'todos': this.state.todos.filter((todo) => todo.id != todoId)
                        })
                    })
                    .catch(error => {
                        console.log(error)
                    })
            //        console.log(bookId)
            }
            
  
  obtainAuthToken(login, password) {
    //console.log('obtainAuthToken', login, password)
    axios
            .post('http://127.0.0.1:8000/api-token-auth/', {
                'username': login,
                'password': password
            })
            .then(response => {
                const token = response.data.token
                console.log('token:', token)
                localStorage.setItem('token', token)

                this.setState({
                    'token': token,
                    'redirect': '/authors'
                }, this.getData)
            })
            .catch(error => console.log(error))
  }


  isAuth() {
    return !!this.state.token
}


componentDidMount() {
  let token = localStorage.getItem('token')
  this.setState({
      'token': token
  }, this.getData)
}

  getHeaders() {
    if (this.isAuth()) {
        return {
            'Authorization': 'Token ' + this.state.token
        }
    }
//        return { 'Accept': 'application/json; version=2.0' }
    return { }
}

getData() {
  this.setState({
      'redirect': false
  })

  let headers = this.getHeaders()

    axios.get('http://127.0.0.1:8000/api/authors/', {headers})
      .then(response => {
        const authors = response.data.results
        this.setState({
            'authors': authors
          })
      })
      .catch(error => {
        console.log(error)
        this.setState({ 'authors': [] })
    })
    axios.get('http://127.0.0.1:8000/api/user/', {headers})
    .then(response => {
      const users = response.data.results
      this.setState({
          'users': users
        })
    })
    .catch(error => {
      console.log(error)
      this.setState({ 'users': [] })
  })
    axios.get('http://127.0.0.1:8000/api/books/', {headers})
    .then(response => {
      const books = response.data
      this.setState({
          'books': books
        })
    })
    .catch(error => {
      console.log(error)
      this.setState({ 'books': [] })
  })
    axios.get('http://127.0.0.1:8000/api/Project/', {headers})
    .then(response => {
      const projects = response.data.results
      this.setState({
          'projects': projects
        })
    })
    .catch(error => {
      console.log(error)
      this.setState({ 'projects': [] })
  })
    axios.get('http://127.0.0.1:8000/api/ToDo_notes/', {headers})
    .then(response => {
      const todos = response.data.results
      this.setState({
          'todos': todos
        })
    })
    .catch(error => {
      console.log(error)
      this.setState({ 'todos': [] })
  })
}

  logOut() {
    localStorage.setItem('token', '')
    this.setState({
        'token': '',
        'redirect': false
        
    }, this.getData)
}



//http://localhost:3000/#/books 

  render () {
      return (
      <div>
        <BrowserRouter>
           {this.state.redirect ? <Navigate to={this.state.redirect} /> : <div/>}
        <div className="container2">
          <span>
            <a className="navbar-brand" rel="nofollow" href="https://www.django-rest-framework.org/">
                    Django REST framework
                    </a>
          </span>
          <ul className="login-logout">
            <li>
              {this.isAuth() ? <submit className="logout" onClick={() => this.logOut()}>Logout</submit> : <Link className="login" to='/login'>Login</Link>}
            </li>
          </ul>
        </div>
        <nav>
        <ul>
          <li> <Link to='/'>Authors</Link> </li>
          <li> <Link to='/books'>Books</Link> </li>
          <li> <Link to='/create_book'>Create book</Link> </li>
          <li> <Link to='/create_todo'>Create todo</Link> </li>
          <li> <Link to='/users'>Users</Link> </li>
          <li> <Link to='/projects'>Projects</Link> </li>
          <li> <Link to='/todos'>ToDos</Link> </li>
        </ul>   
        </nav>
          <Routes>
            <Route exact path='/' element={<Navigate to='/authors'/>} />
            <Route exact path='/books' element={<BookList books={this.state.books} authors={this.state.authors} deleteBook={(bookId) => this.deleteBook(bookId)} />} />
            <Route exact path='/create_book' element={<BookForm authors={this.state.authors} createBook={(name, authors) => this.createBook(name, authors)} />} />
            <Route exact path='/create_todo' element={<TodoForm projects={this.state.projects} users={this.state.users} createToDo={(tagtext, isactive, project, user) => this.createToDo(tagtext, isactive, project, user)} />} />
            <Route exact path='/login' element={<LoginForm obtainAuthToken={(login, password) => this.obtainAuthToken(login, password)}/>} />
            <Route exact path='/users' element={<UserList users={this.state.users} />} />
            <Route exact path='/projects'>
                <Route index element={<ProjectList projects={this.state.projects} token={this.state.token} />} />
                <Route path=':todosID' element={<ProjectToDos todos={this.state.todos} />} />
                
            </Route>
            <Route exact path='/todos' element={<ToDoList todos={this.state.todos} deleteTodo={(todoId) => this.deleteTodo(todoId)} />} />
            <Route exact path='/authors' >
                <Route index element={<AuthorList token={this.state.token}/>} />
                <Route path=':authorID' element={<AuthorBookList books={this.state.books} authors={this.state.authors} />} />
            </Route>
            <Route path='*' element={<NotFound />} />
          </Routes>
        </BrowserRouter>
        <footer className="footer">
            © https://t.me/Zmeinih_del_master
        </footer>
      </div>
      )
    }
  }
  
    
export default App;