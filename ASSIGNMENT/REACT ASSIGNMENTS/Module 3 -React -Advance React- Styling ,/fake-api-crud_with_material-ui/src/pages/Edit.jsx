import { useState, useEffect } from "react";
import { Container, TextField, Button, Typography } from "@mui/material";
import axios from "axios";
import { useParams, useNavigate } from "react-router-dom";

const Edit = () => {
  const { id } = useParams();
  const [title, setTitle] = useState("");
  const [body, setBody] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    axios.get(`https://dummyjson.com/posts/${id}`)
      .then((response) => {
        setTitle(response.data.title);
        setBody(response.data.body);
      })
      .catch((error) => console.error(error));
  }, [id]);

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.put(`https://dummyjson.com/posts/${id}`, { title, body })
      .then(() => navigate("/"))
      .catch((error) => console.error(error));
  };

  return (
    <Container>
      <Typography variant="h4" gutterBottom>Edit Post</Typography>
      <form onSubmit={handleSubmit}>
        <TextField fullWidth label="Title" margin="normal" value={title} onChange={(e) => setTitle(e.target.value)} required />
        <TextField fullWidth label="Body" margin="normal" value={body} onChange={(e) => setBody(e.target.value)} required />
        <Button variant="contained" color="primary" type="submit" sx={{ marginTop: 2 }}>Update</Button>
      </form>
    </Container>
  );
};

export default Edit;
