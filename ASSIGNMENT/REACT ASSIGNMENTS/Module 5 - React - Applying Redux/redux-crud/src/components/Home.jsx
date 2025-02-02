import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchUsers, deleteUser } from "../actions/userActions";
import { Link } from "react-router-dom";
import { useState } from "react";
import axios from "axios";

const Home = () => {
  const dispatch = useDispatch();
  const [users, setUsers] = useState([]); 
  
  useEffect(() => {
    axios.get("http://localhost:5000/users")
      .then((response) => {
        console.log("API Response:", response.data); 
        setUsers(Array.isArray(response.data) ? response.data : []); 
      })
      .catch((error) => console.error("Error fetching users:", error));
  }, []);
  
  return (
    <div className="container">
      <h2>User List</h2>
      <Link to="/add" className="btn btn-primary">Add User</Link>
      <table border="1">
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Contact</th>
            <th>Address</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {users.map((user) => (
            <tr key={user.id}>
              <td>{user.name}</td>
              <td>{user.email}</td>
              <td>{user.contact}</td>
              <td>{user.address}</td>
              <td>
                <button onClick={() => dispatch(deleteUser(user.id))} className="btn btn-danger">Delete</button>
                <Link to={`/edit/${user.id}`} className="btn btn-primary">Edit</Link>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Home;
