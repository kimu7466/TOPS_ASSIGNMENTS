import React from "react";
import TodoItem from "./TodoItem";

function TodoList({ tasks, deleteTask, setEditTask }) {
  return (
    <ul>
      {tasks.map((task) => (
        <TodoItem key={task.id} task={task} deleteTask={deleteTask} setEditTask={setEditTask} />
      ))}
    </ul>
  );
}

export default TodoList;
