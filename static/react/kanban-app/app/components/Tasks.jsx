import React from 'react';
import Task from './Task';
import Editable from './Editable';

export default ({
  tasks,
  onTaskClick=() => {}, onEdit=() => {}, onDelete=() => {}
}) => (
    <ul>{tasks.map(({id, editing, name}) =>
      <li key={id}>
        <Task onClick={onTaskClick.bind(null, id)}>
          <Editable
             editing={editing}
             value={name}
             onEdit={onEdit.bind(null, id)} />
          <button onClick={onDelete.bind(null, id)}>x</button>
        </Task>
      </li>
    )}</ul>
)
