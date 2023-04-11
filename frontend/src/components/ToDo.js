import React from 'react'
import App from '../App'

const ToDoItem = ({todo, deleteTodo}) => {
    return (
    <tr>
        <td>
            {todo.project}
        </td>
        <td>
            {todo.tag_text}
        </td>
        <td>
            {todo.user}
        </td>
        <td>
            {todo.created}
        </td>
        <td>
            {todo.updated}
        </td>
        <td>
            <button onClick={() => deleteTodo(todo.id) }>Delete</button>
        </td>
    </tr>
)
}

const ToDoList = ({todos, deleteTodo}) => {
    return (
    <table>
        <th>
            project
        </th>
        <th>
            tag_text
        </th>
        <th>
            user
        </th>
        <th>
            created
        </th>
        <th>
            updated
        </th>
        {todos.map((todo) => <ToDoItem todo={todo} deleteTodo={deleteTodo}/>)}
    </table>
    )
}

export default ToDoList