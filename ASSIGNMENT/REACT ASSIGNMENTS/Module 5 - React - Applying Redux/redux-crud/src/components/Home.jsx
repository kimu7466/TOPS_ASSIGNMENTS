import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchUsers, deleteUser } from "../actions/userActions";
import { Link } from "react-router-dom";
import "../styles/styles.css";

const Home = () => {
  const dispatch = useDispatch();
  const users = useSelector((state) => state.users.users);

  useEffect(() => {
    dispatch(fetchUsers());
  }, [dispatch]);

  return (
    <div className="container">
      <h2>User List</h2>
      <Link to="/add" className="btn btn-primary">Add User</Link>
      <table>
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
                <button onClick={() => dispatch(deleteUser(user.id))}>Delete</button>
                <Link to={`/edit/${user.id}`}>Edit</Link>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Home;
