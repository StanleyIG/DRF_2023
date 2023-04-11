import React from 'react'

class TodoForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            tagtext: '',
            isactive: true,
            selectedProject: null,
            selectedUser: null,
            showList: false
        };
    }

    handleSubmit(event) {
        event.preventDefault();
        console.log(this.state.tagtext, this.state.isactive, this.state.selectedProject, this.state.selectedUser);
        this.props.createToDo(this.state.tagtext, this.state.isactive, this.state.selectedProject, this.state.selectedUser)
        event.preventDefault();
    }

    handleChange(event) {
        this.setState({ tagtext: event.target.value });
    }

    handleProjectSelect(event) {
        this.setState({ selectedProject: event.target.value });
    }

    handleUserSelect(event) {
        this.setState({ selectedUser: event.target.value });
    }

    toggleList() {
        this.setState(prevState => ({ showList: !prevState.showList }));
    }

    render() {
        return (
            <div className="container">
                <form onSubmit={(event) => this.handleSubmit(event)}>
                    <input type="text" tagtext="tagtext" placeholder="tagtext" value={this.state.tagtext} onChange={(event) => this.handleChange(event)} />
                    <button type="button" onClick={() => this.toggleList()}>Select projects or users</button>
                    {this.state.showList && (
                        <div>
                            <select onChange={(event) => this.handleProjectSelect(event)}>
                                <option value="">Select project</option>
                                {this.props.projects.map((project) => <option key={project.id} value={project.id}>{project.name}</option>)}
                            </select>
                            <select onChange={(event) => this.handleUserSelect(event)}>
                                <option value="">Select user</option>
                                {this.props.users.map((user) => <option key={user.id} value={user.id}>{user.username}</option>)}
                            </select>
                        </div>
                    )}
                    <input type="submit" value="Create" />
                </form>
            </div>
        )
    }
}

export default TodoForm;