import React, { useEffect, useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

const Home = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:5000/users")
      .then((response) => setUsers(response.data))
      .catch((error) => console.error("Error fetching users:", error));
  }, []);

  const deleteUser = (id) => {
    axios
      .delete(`http://localhost:5000/users/${id}`)
      .then(() => setUsers(users.filter((user) => user.id !== id)))
      .catch((error) => console.error("Error deleting user:", error));
  };

  return (
    <div className="container">
      <h2>User List</h2>
      <Link to="/create" className="link">
        Add User
      </Link>
      
      <table className="user-table" border={1}>
        <thead>
          <tr>
            <th className="cell">User Firstname</th>
            <th className="cell">User Lastname</th>
            <th className="cell">User Email</th>
            <th className="cell">Actions</th>
          </tr>
        </thead>
        <tbody>
          {users.map((user) => (
            <tr key={user.id}>
              <td>{user.fname}</td>
              <td>{user.lname}</td>
              <td>{user.email}</td>
              <td>
                <Link to={`/edit/${user.id}`} className="link">Edit</Link>
                <button onClick={() => deleteUser(user.id)}>Delete</button>
                <Link to={`/view/${user.id}`} className="link">view</Link>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Home;
