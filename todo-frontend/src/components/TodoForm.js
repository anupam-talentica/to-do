import React, { useState } from 'react';
import './TodoForm.css';

function TodoForm({ onAddTodo }) {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!title.trim()) {
      setError('Title is required');
      return;
    }

    onAddTodo({
      title: title.trim(),
      description: description.trim(),
      completed: false
    });

    setTitle('');
    setDescription('');
    setError('');
  };

  return (
    <form className="todo-form" onSubmit={handleSubmit}>
      <div className="form-group">
        <input
          type="text"
          placeholder="Add a new todo..."
          value={title}
          onChange={(e) => {
            setTitle(e.target.value);
            setError('');
          }}
          className="form-input"
        />
      </div>

      <div className="form-group">
        <textarea
          placeholder="Add description (optional)"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          className="form-textarea"
          rows="3"
        />
      </div>

      {error && <div className="form-error">{error}</div>}

      <button type="submit" className="submit-btn">
        ✅ Add Todo
      </button>
    </form>
  );
}

export default TodoForm;
