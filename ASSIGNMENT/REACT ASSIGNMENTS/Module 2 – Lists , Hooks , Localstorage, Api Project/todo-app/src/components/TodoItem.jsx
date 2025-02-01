import React from "react";

function TodoItem({ task, deleteTask, setEditTask }) {
  return (
    <li style={{ display: "grid", gridTemplateColumns: "1fr auto", alignItems: "center", gap: "10px" }}>
    <div style={{textAlign:"left"}}>
      {task.text}
    </div>
    <div>
      <button onClick={() => deleteTask(task.id)}>
        <i className="fa-solid fa-trash-can"></i>
      </button>
      <button onClick={() => setEditTask(task)}>
        <i className="fa-solid fa-pen-to-square"></i>
      </button>
    </div>
  </li>
  
  );
}

export default TodoItem;
