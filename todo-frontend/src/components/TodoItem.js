import React from 'react';
import './TodoItem.css';

function TodoItem({ todo, onToggle, onDelete }) {
  const getPriorityBadge = (priority) => {
    switch (priority) {
      case 'HIGH':
        return <span className="priority-badge priority-high">🔴 High</span>;
      case 'LOW':
        return <span className="priority-badge priority-low">🟢 Low</span>;
      default:
        return <span className="priority-badge priority-medium">🟡 Medium</span>;
    }
  };

  return (
    <li className={`todo-item ${todo.completed ? 'completed' : ''}`}>
      <div className="todo-content">
        <input
          type="checkbox"
          checked={todo.completed}
          onChange={() => onToggle(todo.id)}
          className="todo-checkbox"
        />
        <div className="todo-text">
          <div className="todo-header">
            {getPriorityBadge(todo.priority)}
            <h3 className="todo-title">{todo.title}</h3>
          </div>
          {todo.description && <p className="todo-description">{todo.description}</p>}
        </div>
      </div>
      <button
        className="delete-btn"
        onClick={() => onDelete(todo.id)}
        title="Delete todo"
      >
        🗑️
      </button>
    </li>
  );
}

export default TodoItem;
