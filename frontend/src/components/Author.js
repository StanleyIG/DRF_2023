import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import './AuthorList.css';

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

const AuthorList = ({ token }) => {
  const [page, setPage] = useState(1);
  const [limit, setLimit] = useState(3);
  const [totalPages, setTotalPages] = useState(1);
  const [authorsList, setAuthorsList] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');

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

  const handlePrevClick = () => {
    setPage(page - 1);
  };

  const handleNextClick = () => {
    setPage(page + 1);
  };

  const handlePageClick = (pageNumber) => {
    setPage(pageNumber);
  };

  const handleSearch = (event) => {
    setSearchTerm(event.target.value);
    setPage(1);
  };

  useEffect(() => {
    const fetchAuthors = async () => {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/api/authors/?offset=${(page - 1) * limit}&limit=${limit}&last_name=${searchTerm}`,
          { headers }
        );
        const data = response.data;
        setAuthorsList(data.results);
        setTotalPages(Math.ceil(data.count / limit));
      } catch (error) {
        console.log(error);
        if (error.response && error.response.status === 403) {
          setAuthorsList([]);
        }
      }
    };
    fetchAuthors();
  }, [page, limit, searchTerm, token]);

  const pageButtons = [];
  for (let i = 1; i <= totalPages; i++) {
    pageButtons.push(
      <button key={i} onClick={() => handlePageClick(i)} disabled={page === i}>
        {i}
      </button>
    );
  }

  return (
    <div className="container">
      <div className="container">
        <h1>made on Django REST/React</h1>
        <input type="text" placeholder="введите фамилию" onChange={handleSearch} />
      </div>
      <table>
        <thead>
          <tr>
            <th>First name</th>
            <th>Last Name</th>
            <th>Birthday year</th>
          </tr>
        </thead>
        <tbody>
          {authorsList.map((author) => (
            <AuthorItem key={author.id} author={author} />
          ))}
        </tbody>
      </table>
      <div className="pagination">
        <button onClick={handlePrevClick} disabled={page === 1}>
          назад
        </button>
        {pageButtons}
        <span>{`страница ${page} / ${totalPages}`}</span>
        <button onClick={handleNextClick} disabled={page === totalPages}>
          вперёд
        </button>
        <p></p>
      </div>
    </div>
  );
};

export default AuthorList;