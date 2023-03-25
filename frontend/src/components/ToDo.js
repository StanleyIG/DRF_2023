import React from 'react'
import App from '../App'

const ToDoItem = ({todo}) => {
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
            {todo.is_active}
        </td>
    </tr>
)
}

const ToDoList = ({todos}) => {
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
        <th>
            is_active
        </th>
        {todos.map((todo) => <ToDoItem todo={todo} />)}
    </table>
    )
}

export default ToDoList