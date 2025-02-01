import { useState, useEffect } from "react";
import axios from "axios";
import { Container, Button, Typography, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from "@mui/material";
import { Link } from "react-router-dom";

const Home = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    axios.get("https://dummyjson.com/posts/")
      .then((response) => setPosts(response.data.posts.slice(0, 5))) // Get only 5 posts for demo
      .catch((error) => console.error(error));
  }, []);

  return (
    <Container>
      <Typography variant="h4" gutterBottom>Posts</Typography>
      <Button variant="contained" color="primary" component={Link} to="/create">Create New</Button>
      <TableContainer component={Paper} sx={{ marginTop: 2 }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell>Title</TableCell>
              <TableCell>Actions</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {posts.map((post) => (
              <TableRow key={post.id}>
                <TableCell>{post.id}</TableCell>
                <TableCell>{post.title}</TableCell>
                <TableCell>
                  <Button variant="outlined" color="secondary" component={Link} to={`/edit/${post.id}`} sx={{ marginRight: 1 }}>Edit</Button>
                  <Button variant="contained" color="error" onClick={() => handleDelete(post.id)}>Delete</Button>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Container>
  );

  function handleDelete(id) {
    axios.delete(`https://dummyjson.com/posts/${id}`)
      .then(() => setPosts(posts.filter(post => post.id !== id)))
      .catch((error) => console.error(error));
  }
};

export default Home;
