import { useState } from "react";
import { Container, TextField, Button, Typography } from "@mui/material";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Create = () => {
  const [title, setTitle] = useState("");
  const [body, setBody] = useState("");
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post("https://dummyjson.com/posts", { title, body })
      .then(() => navigate("/"))
      .catch((error) => console.error(error));
  };

  return (
    <Container>
      <Typography variant="h4" gutterBottom>Create Post</Typography>
      <form onSubmit={handleSubmit}>
        <TextField fullWidth label="Title" margin="normal" value={title} onChange={(e) => setTitle(e.target.value)} required />
        <TextField fullWidth label="Body" margin="normal" value={body} onChange={(e) => setBody(e.target.value)} required />
        <Button variant="contained" color="primary" type="submit" sx={{ marginTop: 2 }}>Submit</Button>
      </form>
    </Container>
  );
};

export default Create;
