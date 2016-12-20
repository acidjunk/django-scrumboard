import React from 'react';
import Task from './Task';
import Editable from './Editable';

export default ({
  tasks,
  onTaskClick=() => {}, onEdit=() => {}, onDelete=() => {}
}) => (
    <div className="ui list">{tasks.map(({id, editing, name}) =>
      <div className="item" key={id}>
        <Task onClick={onTaskClick.bind(null, id)}>
          <Editable
             editing={editing}
             value={name}
             onEdit={onEdit.bind(null, id)} />
          <button onClick={onDelete.bind(null, id)}>x</button>
        </Task>
      </div>
    )}</div>
)
