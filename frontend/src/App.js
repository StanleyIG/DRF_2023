import React from 'react';
import logo from './logo.svg';
import './App.css';
//import Menu from './components/Menu'
import AuthorList from './components/Author.js'
import UserList from './components/Users';
import BookList from './components/books';
import ProjectList from './components/Project';
import ToDoList from './components/ToDo';
import AuthorBookList from './components/AuthorBook';
import ProjectToDos from './components/ProjectToDos';
import LoginForm from './components/LoginForm.js';
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
    }
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
      const books = response.data.results
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
    }, this.getData)
}



//http://localhost:3000/#/books 

  render () {
      return (
      <div>
        <BrowserRouter>
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
          <li> <Link to='/users'>Users</Link> </li>
          <li> <Link to='/projects'>Projects</Link> </li>
          <li> <Link to='/todos'>ToDos</Link> </li>
        </ul>   
        </nav>
          <Routes>
            <Route exact path='/' element={<Navigate to='/authors'/>} />
            <Route exact path='/books' element={<BookList books={this.state.books} authors={this.state.authors} />} />
            <Route exact path='/login' element={<LoginForm obtainAuthToken={(login, password) => this.obtainAuthToken(login, password)}/>} />
            <Route exact path='/users' element={<UserList users={this.state.users} />} />
            <Route exact path='/projects'>
                <Route index element={<ProjectList projects={this.state.projects} />} />
                <Route path=':todosID' element={<ProjectToDos todos={this.state.todos} />} />
                
            </Route>
            <Route exact path='/todos' element={<ToDoList todos={this.state.todos} />} />
            <Route exact path='/authors' >
                <Route index element={<AuthorList token={this.state.token}/>} />
                <Route path=':authorID' element={<AuthorBookList books={this.state.books} />} />
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

  
