import React from 'react'
import App from '../App'

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

const BookList = ({books, authors}) => {
    return (
    <table>
        <th>
            name
        </th>
        <th>
            authors
        </th>
       
        {books.map((book) => <BookItem book={book} authors={authors} />)}
    </table>
    )
}

export default BookList