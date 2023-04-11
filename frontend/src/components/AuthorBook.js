import React from 'react'
import { useLocation, useParams } from 'react-router-dom'
//{book.authors.map(authorID => authors.find(a => a.id === authorID).last_name)}

const BookItem = ({book, authors}) => {
    return (
    <tr>
        <td>
            {book.name}
        </td>
        <td>
            {book.authors.map(authorID => authors.find(a => a.id === authorID).last_name)}
        </td>
    </tr>
)
}

const AuthorBookList = ({books, authors}) => {
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
        {filtered_books.map((book) => <BookItem book={book} authors={authors} key={book.id} />)}
    </table>
    )
}

export default AuthorBookList