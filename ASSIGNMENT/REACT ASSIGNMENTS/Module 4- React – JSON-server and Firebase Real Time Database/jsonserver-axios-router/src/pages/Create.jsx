import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Create = () => {
  const [fname, setFname] = useState("");
  const [lname, setLname] = useState("");
  const [email, setEmail] = useState("");
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post("http://localhost:5000/users", { fname,lname,email })
      .then(() => navigate("/"))
      .catch(error => console.error("Error adding user:", error));
  };

  return (
    <div className="container">
      <h2>Add user</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="">First name : </label>
        <input type="text" value={fname} onChange={(e) => setFname(e.target.value)} placeholder="Enter First name" required />
        <label htmlFor="">Last name : </label>
        <input type="text" value={lname} onChange={(e) => setLname(e.target.value)} placeholder="Enter Last name" required />
        <label htmlFor="">Email : </label>
        <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Enter Email"  required />
        <button type="submit">Update</button>
      </form>
    </div>
  );
};

export default Create;
