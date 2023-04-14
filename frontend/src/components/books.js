import React from 'react'
import App from '../App'

const BookItem = ({book, authors, deleteBook}) => {
    return (
    <tr>
        <td>
            {book.name}
        </td>
        <td>
        {book.authors.map(authorId => {
    const author = authors.find(a => a.id === authorId);
    return author ? author.last_name : "";
})}
        </td>
        <td>
            <button onClick={() => deleteBook(book.id) }>Delete</button>
        </td>
    </tr>
)
}

const BookList = ({books, authors, deleteBook}) => {
    return (
    <table>
        <th>
            name
        </th>
        <th>
            authors
        </th>
        {books.map((book) => <BookItem book={book} authors={authors} deleteBook={deleteBook}/> )}
    </table>
    )
}

export default BookList