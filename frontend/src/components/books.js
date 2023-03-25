import React from 'react'
import App from '../App'

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

const BookList = ({books}) => {
    return (
    <table>
        <th>
            name
        </th>
        <th>
            authors
        </th>
       
        {books.map((book) => <BookItem book={book} />)}
    </table>
    )
}

export default BookList