import React, { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { updateUser, fetchUsers } from "../actions/userActions";
import "../styles/styles.css";

const EditUser = () => {
  const { id } = useParams();
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const users = useSelector((state) => state.users.users);
  const [user, setUser] = useState({ name: "", email: "", contact: "", address: "" });

  useEffect(() => {
    console.log("Users:", users); 
    console.log("Current ID from params:", id); 
  
    if (!users || users.length === 0) {
      console.log("Users not found, dispatching fetchUsers...");
      dispatch(fetchUsers());
    } else {
      console.log("Users found, searching for user with id:", id);
     
      const existingUser = users.find((u) => u.id === id);
      console.log("Existing user found:", existingUser);
  
      if (existingUser) {
        setUser(existingUser);
      } else {
        console.log("User not found, navigating to home");
        navigate("/");
      }
    }
  }, [id, users, dispatch, navigate]);
    const handleChange = (e) => {
    setUser({ ...user, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    dispatch(updateUser(id, user));
    navigate("/");
  };

 
  if (!users || users.length === 0) {
    return <div>Loading...</div>;
  }

  return (
    <form onSubmit={handleSubmit} className="form-container">
      <input type="text" name="name" value={user.name} onChange={handleChange} required />
      <input type="email" name="email" value={user.email} onChange={handleChange} required />
      <input type="text" name="contact" value={user.contact} onChange={handleChange} required />
      <input type="text" name="address" value={user.address} onChange={handleChange} required />
      <button type="submit">Update User</button>
    </form>
  );
};

export default EditUser;
