//import React from 'react'
import {Link} from 'react-router-dom'
import React, { useState, useEffect } from 'react';
import axios from 'axios';
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

const ProjectList = ({ token }) => {
    const [searchTerm, setSearchTerm] = useState('');
    const [projectList, setProjectList] = useState([]);

    const handleSearch = (event) => {
        setSearchTerm(event.target.value);
      };

      const isAuth = () => {
        return !!token;
      };
    
      const getHeaders = () => {
        if (isAuth()) {
          return {
            Authorization: 'Token ' + token,
          };
        }
        return {};
      };
    
      const headers = getHeaders();
    


    useEffect(() => {
        const fetchProject = async () => {
          try {
            const response = await axios.get(
                `http://127.0.0.1:8000/api/Project/?name=${searchTerm}`,
                { headers }
            );
            const data = response.data;
            setProjectList(data.results);
          } catch (error) {
            console.log(error);
            if (error.response && error.response.status === 403) {
              setProjectList([]);
            }
          }
        };
        fetchProject();
      }, [searchTerm, token]);

    
    return (
        <div className='container'>
        <input type="text" placeholder="введите название проекта" onChange={handleSearch} />
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
        {projectList.map((project) => <ProjectItem key={project.id} project={project} />)}
    </table>
    </div>
    )
}

export default ProjectList