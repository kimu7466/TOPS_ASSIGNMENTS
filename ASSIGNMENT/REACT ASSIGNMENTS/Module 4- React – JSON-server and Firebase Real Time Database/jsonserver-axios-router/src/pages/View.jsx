import React, { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate, useParams } from "react-router-dom";

const View = () => {
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


  return (
    <div className="container">
      <h2>View User details</h2>
        <p htmlFor="">First name : <span>{fname}</span></p>
        <p htmlFor="">Last name : <span>{lname}</span></p>
        <p htmlFor="">Email : <span>{email}</span></p>
        <button onClick={()=>{navigate("/")}}>back</button>
    </div>
  );
};

export default View;
