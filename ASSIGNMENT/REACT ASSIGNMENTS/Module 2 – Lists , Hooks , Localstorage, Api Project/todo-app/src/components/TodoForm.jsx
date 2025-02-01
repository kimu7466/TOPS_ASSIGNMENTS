import React, { useState, useEffect } from "react";

function TodoForm({ addTask, editTask, setEditTask }) {
  const [input, setInput] = useState("");

  useEffect(() => {
    if (editTask) {
      setInput(editTask.text);
    } else {
      setInput("");
    }
  }, [editTask]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (input.trim() === "") return;
    addTask(input);
    setInput("");
  };

  return (
    <form className="input-container" onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Add something to your list"
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <button type="submit">{editTask ? "Update" : "Add"}</button>
    </form>
  );
}

export default TodoForm;

