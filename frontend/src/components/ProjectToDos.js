import React from 'react'
import { useLocation, useParams } from 'react-router-dom'


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

const ProjectToDos = ({todos}) => {
    let {todosID} = useParams()
    let filtered_todos = todos.filter((todo) => todo.project === parseInt(todosID))
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
        {filtered_todos.map((todo) => <ToDoItem todo={todo} />)}
    </table>
    )
}

export default ProjectToDos