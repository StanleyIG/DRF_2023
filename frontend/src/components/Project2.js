//import React from 'react'
import React, { useState } from 'react';
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

const ProjectList2 = ({projects, searchProject}) => {
    const [searchValue, setSearchValue] = useState('');

    const handleSearch = (event) => {
        const value = event.target.value;
        setSearchValue(value);
        searchProject(searchValue);
      };

    return (
        <div className='container'>
        <input
        type="text"
        placeholder="Введите имя проекта"
        value = {searchValue}
        onChange={handleSearch}
      />
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
        {projects.map((project) => <ProjectItem project={project} searchProject={searchProject} />)}
    </table>
    </div>
    )
}

export default ProjectList2