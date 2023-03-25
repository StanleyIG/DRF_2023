import React from 'react'
import { useLocation, useParams } from 'react-router-dom'


const BookItem = ({book}) => {
    return (
    <tr>
        <td>
            {book.name}
        </td>
        <td>
            {book.authors}
        </td>
    </tr>
)
}

const AuthorBookList = ({books}) => {
    //var params = useParams();
    //console.log(params.authorID)
    //var  filtered_books = books.filter((book) => book.authors.includes(parseInt(params.authorID)))
    let {authorID} = useParams()
    let filtered_books = books.filter((book) => book.authors.includes(parseInt(authorID)))
    return (
    <table>
        <th>
            name
        </th>
        <th>
            authors
        </th>
       
        {filtered_books.map((book) => <BookItem book={book} />)}
    </table>
    )
}

export default AuthorBookList