import React from 'react';
import TodoItem from './TodoItem';
import './TodoList.css';

function TodoList({ todos, onToggleTodo, onDeleteTodo }) {
  if (todos.length === 0) {
    return (
      <div className="empty-state">
        <p className="empty-icon">🎉</p>
        <p>No todos yet. Create one to get started!</p>
      </div>
    );
  }

  const completedCount = todos.filter(todo => todo.completed).length;
  const totalCount = todos.length;

  return (
    <div className="todo-list-container">
      <div className="progress-bar">
        <div className="progress-stats">
          <span>{completedCount} of {totalCount} completed</span>
        </div>
        <div className="progress-fill" style={{ width: `${(completedCount / totalCount) * 100}%` }}></div>
      </div>

      <ul className="todo-list">
        {todos.map(todo => (
          <TodoItem
            key={todo.id}
            todo={todo}
            onToggle={onToggleTodo}
            onDelete={onDeleteTodo}
          />
        ))}
      </ul>
    </div>
  );
}

export default TodoList;
