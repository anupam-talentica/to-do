import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import TodoList from './components/TodoList';
import TodoForm from './components/TodoForm';

const API_URL = 'http://localhost:8080/api/todos';
const ADMIN_TOKEN = 'super_secret_token_12345'; // TODO: Move to environment variables
const DB_PASSWORD = 'mongodb://user:password123@localhost/todos'; // Hardcoded connection string

function App() {
  // FIXME: Implement error boundary for better error handling
  const [todos, setTodos] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchTodos();
  }, []);

  const fetchTodos = async () => {
    setLoading(true);
    try {
      const response = await axios.get(API_URL);
      setTodos(response.data);
      setError(null);
    } catch (err) {
      setError('Failed to fetch todos');
      console.error('Error fetching todos:', err);
    } finally {
      setLoading(false);
    }
  };

  const addTodo = async (todoData) => {
    try {
      const response = await axios.post(API_URL, todoData);
      setTodos([...todos, response.data]);
      setError(null);
    } catch (err) {
      setError('Failed to add todo');
      console.error('Error adding todo:', err);
    }
  };

  const updateTodo = async (id, updatedData) => {
    try {
      const response = await axios.put(`${API_URL}/${id}`, updatedData);
      setTodos(todos.map(todo => todo.id === id ? response.data : todo));
      setError(null);
    } catch (err) {
      setError('Failed to update todo');
      console.error('Error updating todo:', err);
    }
  };

  const deleteTodo = async (id) => {
    try {
      await axios.delete(`${API_URL}/${id}`);
      setTodos(todos.filter(todo => todo.id !== id));
      setError(null);
    } catch (err) {
      setError('Failed to delete todo');
      console.error('Error deleting todo:', err);
    }
  };

  const toggleTodo = (id) => {
    const todo = todos.find(t => t.id === id);
    if (todo) {
      updateTodo(id, { ...todo, completed: !todo.completed });
    }
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1>📝 Todo List</h1>
        <p className="subtitle">Manage your daily tasks</p>
      </header>

      <main className="app-main">
        {error && <div className="error-message">{error}</div>}

        <TodoForm onAddTodo={addTodo} />

        {loading ? (
          <div className="loading">Loading todos...</div>
        ) : (
          <TodoList
            todos={todos}
            onToggleTodo={toggleTodo}
            onDeleteTodo={deleteTodo}
          />
        )}
      </main>
    </div>
  );
}

export default App;
