import React, { useState } from 'react';
import TodoForm from './components/TodoForm';
import TodoItem from './components/TodoItem';
import './App.css';

function App() {
  const [todos, setTodos] = useState([
    { id: 1, text: 'test task', completed: false },
  ]);

  const handleAddTodo = (text) => {
    const newTodo = {
      id: Date.now(),
      text,
      completed: false,
    };
    setTodos([...todos, newTodo]);
  };

  const handleToggleComplete = (id) => {
    setTodos(todos.map((todo) =>
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    ));
  };

  const handleDeleteTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };

  const handleEditTodo = (id, newText) => {
    setTodos(todos.map((todo) =>
      todo.id === id ? { ...todo, text: newText } : todo
    ));
  };

  return (
    <div className="App">
      <h1>My Todo List</h1>
      <TodoForm onAddTodo={handleAddTodo} />
      <ul>
        {todos.map((todo) => (
          <TodoItem
            key={todo.id}
            todo={todo}
            onToggleComplete={handleToggleComplete}
            onDeleteTodo={handleDeleteTodo}
            onEditTodo={handleEditTodo}
          />
        ))}
      </ul>
    </div>
  );
}

export default App;
