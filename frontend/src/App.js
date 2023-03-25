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
      'searchQuery': '' 
    }
  }

  

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/authors/').then(response => {
      const authors = response.data.results
      this.setState(
        {
          'authors': authors
        }
      )
    })
    .catch(error => console.log(error))
    axios.get('http://127.0.0.1:8000/api/user/').then(response => {
      const users = response.data.results
      this.setState(
        {
          'users': users
        }
      )
    })
    .catch(error => console.log(error))
    axios.get('http://127.0.0.1:8000/api/books/').then(response => {
      const books = response.data
      this.setState(
        {
          'books': books
        }
      )
    })
    .catch(error => console.log(error))
    axios.get('http://127.0.0.1:8000/api/Project/').then(response => {
      const projects = response.data.results
      this.setState(
        {
          'projects': projects
        }
      )
    })
    .catch(error => console.log(error))
    axios.get('http://127.0.0.1:8000/api/ToDo_notes/').then(response => {
      const todos = response.data.results
      this.setState(
        {
          'todos': todos
        }
      )
    })
    .catch(error => console.log(error))
  }
  handleChange = (event) => {
    this.setState({ searchQuery: event.target.value })
  }


//http://localhost:3000/#/books 

  render () {
      return (
      <div>
        <BrowserRouter>
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
            <Route exact path='/books' element={<BookList books={this.state.books} />} />
            <Route exact path='/users' element={<UserList users={this.state.users} />} />
            <Route exact path='/projects'>
                <Route index element={<ProjectList projects={this.state.projects} />} />
                <Route path=':todosID' element={<ProjectToDos todos={this.state.todos} />} />
                
            </Route>
            <Route exact path='/todos' element={<ToDoList todos={this.state.todos} />} />
            <Route exact path='/authors' >
                <Route index element={<AuthorList authors={this.state.authors} />} />
                <Route path=':authorID' element={<AuthorBookList books={this.state.books} />} />
            </Route>
            <Route path='*' element={<NotFound />} />
          </Routes>
        </BrowserRouter>
      </div>
      )
    }
  }
    
export default App;

  
