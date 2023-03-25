import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const AuthorItem = ({ author }) => {
  return (
    <tr>
      <td>{author.first_name}</td>
      <td>
        <Link to={`/authors/${author.id}`}>{author.last_name} </Link>
      </td>
      <td>{author.birthday_year}</td>
    </tr>
  );
};

const AuthorList = ({ authors }) => {
  const [searchValue, setSearchValue] = useState('');
  const [filteredAuthors, setFilteredAuthors] = useState(authors);

  const handleSearchInputChange = (event) => {
    setSearchValue(event.target.value);
  };

  const handleSearchButtonClick = () => {
    const filtered = authors.filter(author => author.last_name.toLowerCase().includes(searchValue.toLowerCase()));
    setFilteredAuthors(filtered);
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Search by last name"
        value={searchValue}
        onChange={handleSearchInputChange}
      />
      <button onClick={handleSearchButtonClick}>Поиск</button>
      <table>
        <thead>
          <tr>
            <th>First name</th>
            <th>Last Name</th>
            <th>Birthday year</th>
          </tr>
        </thead>
        <tbody>
          {filteredAuthors.map((author) => (
            <AuthorItem key={author.id} author={author} />
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default AuthorList;