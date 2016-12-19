import React from 'react';
import Notes from './Notes';

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
        <button onClick={this.addNote}>+</button>
        <Notes
          notes={notes}
          onNoteClick={this.activateNoteEdit}
          onEdit={this.editNote}
          onDelete={this.deleteNote}
          />
      </div>
    );
  }

  addNote = () => {
    console.log('Adding a new note');
    this.setState({
      notes: this.state.notes.concat([{
        id: uuid.v4(),
        task: 'New task'
      }])
    });
  }

  deleteNote = (id, e) => {
    // Avoid bubbling to edit
    e.stopPropagation();

    this.setState({
      notes: this.state.notes.filter(note => note.id !== id)
    });
  }

  activateNoteEdit = (id) => {
    this.setState({
      notes: this.state.notes.map(note => {
        if(note.id === id) {
          note.editing = true;
        }
        return note;
      })
    });
  }

  editNote = (id, task) => {
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
