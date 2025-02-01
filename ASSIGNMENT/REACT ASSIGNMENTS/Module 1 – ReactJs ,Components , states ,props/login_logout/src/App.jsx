import React, { useState } from "react";
import Navbar from "./Components/Navbar";
import Content from "./Components/Content";
import Footer from "./Components/Footer";
import "./App.css";

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  return (
    <div className="container">
      <Navbar isLoggedIn={isLoggedIn} setIsLoggedIn={setIsLoggedIn} />
      <Content isLoggedIn={isLoggedIn} />
      <Footer />
    </div>
  );
}

export default App;
