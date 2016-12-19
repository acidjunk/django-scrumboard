import React from 'react';

import uuid from 'uuid';

const notes = [
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
];

console.log(notes);

export default () => (
  <ul>{notes.map(note =>
    <li key={note.id}>{note.task}</li>
  )}</ul>
)
