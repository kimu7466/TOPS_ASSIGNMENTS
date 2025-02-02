import React from 'react';
import { Link } from 'react-router-dom';

const UserLayout = ({ children }) => {
  return (
    <div>
      <header>
        <nav>
          <ul>
            <li><Link to="/user/home">Home</Link></li>
            <li><Link to="/user/profile">Profile</Link></li>
          </ul>
        </nav>
      </header>
      <main>{children}</main>
    </div>
  );
};

export default UserLayout;
