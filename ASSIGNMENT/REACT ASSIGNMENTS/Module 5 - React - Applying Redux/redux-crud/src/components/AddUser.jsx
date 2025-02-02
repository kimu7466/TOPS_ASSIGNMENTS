import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { addUser } from "../actions/userActions";
import { useNavigate } from "react-router-dom";
import "../styles/styles.css";

const AddUser = () => {
  const [user, setUser] = useState({ name: "", email: "", contact: "", address: "" });
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleChange = (e) => {
    setUser({ ...user, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    dispatch(addUser(user));
    navigate("/");
  };

  return (
    <form onSubmit={handleSubmit} className="form-container">
      <input type="text" name="name" placeholder="Name" onChange={handleChange} required />
      <input type="email" name="email" placeholder="Email" onChange={handleChange} required />
      <input type="text" name="contact" placeholder="Contact" onChange={handleChange} required />
      <input type="text" name="address" placeholder="Address" onChange={handleChange} required />
      <button type="submit">Add User</button>
    </form>
  );
};

export default AddUser;
