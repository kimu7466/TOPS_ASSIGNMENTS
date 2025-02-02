import React, { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate, useParams } from "react-router-dom";

const Edit = () => {
  const { id } = useParams();
  const [fname, setFname] = useState("");
  const [lname, setLname] = useState("");
  const [email, setEmail] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    axios.get(`http://localhost:5000/users/${id}`)
      .then((response) => {
        setFname(response.data.fname);
        setLname(response.data.lname);
        setEmail(response.data.email);
      })
      .catch(error => console.error("Error fetching user:", error));
  }, [id]);

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.put(`http://localhost:5000/users/${id}`, { fname, lname, email })
      .then(() => navigate("/"))
      .catch(error => console.error("Error updating user:", error));
  };

  return (
    <div className="container">
      <h2>Edit User</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" value={fname} onChange={(e) => setFname(e.target.value)} required />
        <input type="text" value={lname} onChange={(e) => setLname(e.target.value)} required />
        <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
        <button type="submit">Update</button>
      </form>
    </div>
  );
};

export default Edit;
