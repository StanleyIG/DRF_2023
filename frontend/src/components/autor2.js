import React from 'react'
import {Link} from 'react-router-dom'
import App from '../App'

const AuthorItem = ({author}) => {
    return (
    <tr>
        <td>
            {author.first_name}
        </td>
        <td>
            <Link to={`/authors/${author.id}`}>{author.last_name} </Link>
        </td>
        <td>
            {author.birthday_year}
        </td>
    </tr>
)
}

const AuthorList = ({authors}) => {
    return (
    <table>
        <th>
            First name
        </th>
        <th>
            Last Name
        </th>
        <th>
            Birthday year
        </th>
        {authors.map((author) => <AuthorItem author={author} />)}
    </table>
    )
}

export default AuthorList