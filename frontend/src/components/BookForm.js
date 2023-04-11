import React from 'react'
import { withRouter } from 'react-router-dom';


class BookForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            name: '',
            selectedAuthors: [],
            showAuthorsList: false
        };
    }

    handleSubmit(event) {
        this.props.createBook(this.state.name, this.state.selectedAuthors)
        event.preventDefault();
        // handle form submission
    }

    handleChange(event) {
        this.setState({ name: event.target.value });
    }

    handleAuthorsSelect(event) {
        const selectedAuthors = Array.from(event.target.selectedOptions, option => option.value);
        this.setState({ selectedAuthors });
    }

    handleAuthorsSelect2(event) {
        if (!event.target.selectedOptions) {
            this.setState({
                'authors': []
            })
            return;
        }

        let authors = []

        for(let option of event.target.selectedOptions) {
            authors.push(option.value)
        }

        this.setState({
            'authors': authors
        })
    }

    toggleAuthorsList() {
        this.setState(prevState => ({ showAuthorsList: !prevState.showAuthorsList }));
    }

    render() {
        return (
            <div className="container">
                <form onSubmit={(event) => this.handleSubmit(event)}>
                    <input type="text" name="name" placeholder="name" value={this.state.name} onChange={(event) => this.handleChange(event)} />
                    <button type="button" onClick={() => this.toggleAuthorsList()}>Select authors</button>
                    {this.state.showAuthorsList && (
                        <select multiple onChange={(event) => this.handleAuthorsSelect(event)} >
                            {this.props.authors.map((author) => <option key={author.id} value={author.id}>{author.first_name} {author.last_name}</option> )}
                        </select>
                    )}
                    <input type="submit" value="Create" />
                </form>
            </div>
        )
    }
}


export default BookForm;