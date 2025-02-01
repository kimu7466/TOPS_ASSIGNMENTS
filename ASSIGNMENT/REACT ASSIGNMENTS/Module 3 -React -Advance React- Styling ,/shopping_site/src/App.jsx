import React from "react";
import styled from "styled-components";
import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import Footer from "./components/Footer";
import ProductList from "./components/ProductList";


const Container = styled.div`
  font-family: Arial, sans-serif;
`;

const HomePage = () => {
  return (
    <Container>
      <Navbar />
      <Hero />
      <ProductList />
      <Footer />
    </Container>
  );
};

export default HomePage;
