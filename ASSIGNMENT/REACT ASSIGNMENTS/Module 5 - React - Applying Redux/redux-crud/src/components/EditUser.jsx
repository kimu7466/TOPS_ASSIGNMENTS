import React, { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { updateUser } from "../actions/userActions";

const EditUser = () => {
  const { id } = useParams();
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const users = useSelector((state) => state.users);

  const [user, setUser] = useState({ name: "", email: "", contact: "", address: "" });

  useEffect(() => {
    const existingUser = users.find((u) => u.id === parseInt(id));
    if (existingUser) {
      setUser(existingUser);
    } else {
      navigate("/"); 
    }
  }, [id, users, navigate]);

  const handleChange = (e) => {
    setUser({ ...user, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    dispatch(updateUser(id, user)); 
    navigate("/");
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" name="name" value={user.name} onChange={handleChange} required />
      <input type="email" name="email" value={user.email} onChange={handleChange} required />
      <input type="text" name="contact" value={user.contact} onChange={handleChange} required />
      <input type="text" name="address" value={user.address} onChange={handleChange} required />
      <button type="submit">Update User</button>
    </form>
  );
};

export default EditUser;
