import React from 'react';
import Tasks from './Tasks';

import uuid from 'uuid';

export default class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      // Temporary datastore for tasks
      tasks: [
        {
          id: uuid.v4(),
          name: 'Implement other data structures'
        },
        {
          id: uuid.v4(),
          name: 'Use test data from other sources'
        },
        {
          id: uuid.v4(),
          name: 'Finish the kanban implementation'
        }
      ]
    };
  }

  render() {
    const {tasks} = this.state;

    return (
      <div>
        <button onClick={this.addTask}>+</button>
        <Tasks
          tasks={tasks}
          onTaskClick={this.activateTaskEdit}
          onEdit={this.editTask}
          onDelete={this.deleteTask}
          />
      </div>
    );
  }

  addTask = () => {
    console.log('Adding a new task');
    this.setState({
      tasks: this.state.tasks.concat([{
        id: uuid.v4(),
        name: 'New task'
      }])
    });
  }

  deleteTask = (id, e) => {
    // Avoid bubbling to edit
    e.stopPropagation();

    this.setState({
      tasks: this.state.tasks.filter(task => task.id !== id)
    });
  }

  activateTaskEdit = (id) => {
    this.setState({
      tasks: this.state.tasks.map(task => {
        if(task.id === id) {
          task.editing = true;
        }
        return task;
      })
    });
  }

  editTask = (id, name) => {
    this.setState({
      tasks: this.state.tasks.map(task => {
        if(task.id === id) {
          task.editing = false;
          task.name = name;
        }
        return task;
      })
    });
  }




}
