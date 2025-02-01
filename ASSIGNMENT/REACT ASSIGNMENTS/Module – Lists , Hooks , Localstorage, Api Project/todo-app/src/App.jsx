import React, { useState, useEffect } from "react";
import TodoForm from "./components/TodoForm";
import TodoList from "./components/TodoList";
import "./App.css";

function App() {
  const [tasks, setTasks] = useState(() => JSON.parse(localStorage.getItem("tasks")) || []);
  const [editTask, setEditTask] = useState(null);

  useEffect(() => {
    localStorage.setItem("tasks", JSON.stringify(tasks));
  }, [tasks]);

  const addTask = (taskText) => {
    if (editTask) {
      setTasks(tasks.map(task => task.id === editTask.id ? { ...task, text: taskText } : task));
      setEditTask(null);
    } else {
      setTasks([...tasks, { id: Date.now(), text: taskText }]);
    }
  };

  const deleteTask = (id) => {
    setTasks(tasks.filter((task) => task.id !== id));
  };

  const clearList = () => {
    setTasks([]);
  };

  return (
    <div className="container">
      <h1>Grocery Shopping</h1>
      <TodoList tasks={tasks} deleteTask={deleteTask} setEditTask={setEditTask} />
      <TodoForm addTask={addTask} editTask={editTask} setEditTask={setEditTask} />
      {tasks.length > 0 && <button className="clear-btn" onClick={clearList}>Delete List</button>}
    </div>
  );
}

export default App;
