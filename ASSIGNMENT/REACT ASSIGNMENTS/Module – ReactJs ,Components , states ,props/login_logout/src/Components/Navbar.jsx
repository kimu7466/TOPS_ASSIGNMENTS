import React from "react";

function Navbar({ isLoggedIn, setIsLoggedIn }) {
  return (
    <div className="navbar">
      <span>Navigation</span>
      <button onClick={() => setIsLoggedIn(!isLoggedIn)}>
        {isLoggedIn ? "Logout" : "Login"}
      </button>
    </div>
  );
}

export default Navbar;
