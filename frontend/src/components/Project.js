import React from 'react'
import {Link} from 'react-router-dom'
import App from '../App'


const ProjectItem = ({project}) => {
    return (
    <tr>
        <td>
            <Link to={`/projects/${project.id}`}>{project.name} </Link>
        </td>
        <td>
            {project.repository_link}
        </td>
        <td>
            {project.users}
        </td>
    </tr>
)
}

const ProjectList = ({projects}) => {
    return (
    <table>
        <th>
            name
        </th>
        <th>
            repository_link
        </th>
        <th>
            users
        </th>
        {projects.map((project) => <ProjectItem project={project} />)}
    </table>
    )
}

export default ProjectList