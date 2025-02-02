import { Outlet, Link } from "react-router-dom";

const UserLayout = () => {
  return (
    <div>
      <h2>User Dashboard</h2>
      <nav>
        <Link to="/user">Home</Link> | 
        <Link to="/user/profile">Profile</Link>
      </nav>
      <Outlet />
    </div>
  );
};

export default UserLayout;
