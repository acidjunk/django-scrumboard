import React from 'react';
import Tasks from './Tasks';

import uuid from 'uuid';

export default class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      // Temporary datastore for notes
      notes: [
        {
          id: uuid.v4(),
          task: 'Implement other data structures'
        },
        {
          id: uuid.v4(),
          task: 'Use test data from other sources'
        },
        {
          id: uuid.v4(),
          task: 'Finish the kanban implementation'
        }
      ]
    };
  }

  render() {
    const {notes} = this.state;

    return (
      <div>
        <button onClick={this.addTask}>+</button>
        <Tasks
          notes={notes}
          onTaskClick={this.activateTaskEdit}
          onEdit={this.editTask}
          onDelete={this.deleteTask}
          />
      </div>
    );
  }

  addTask = () => {
    console.log('Adding a new note');
    this.setState({
      notes: this.state.notes.concat([{
        id: uuid.v4(),
        task: 'New task'
      }])
    });
  }

  deleteTask = (id, e) => {
    // Avoid bubbling to edit
    e.stopPropagation();

    this.setState({
      notes: this.state.notes.filter(note => note.id !== id)
    });
  }

  activateTaskEdit = (id) => {
    this.setState({
      notes: this.state.notes.map(note => {
        if(note.id === id) {
          note.editing = true;
        }
        return note;
      })
    });
  }

  editTask = (id, task) => {
    this.setState({
      notes: this.state.notes.map(note => {
        if(note.id === id) {
          note.editing = false;
          note.task = task;
        }
        return note;
      })
    });
  }




}
