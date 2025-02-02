import { Link } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { toggleTheme } from "../redux/themeSlice";

const Navbar = () => {
  const dispatch = useDispatch();
  const darkMode = useSelector((state) => state.theme.darkMode);

  return (
    <nav className="p-4 bg-gray-200 dark:bg-gray-900 flex justify-between items-center">
      <h1 className="text-xl font-bold">My Portfolio</h1>
      <div className="flex gap-4">
        <Link to="/" className="text-gray-800 dark:text-white">Home</Link>
        <Link to="/skills" className="text-gray-800 dark:text-white">Skills</Link>
        <Link to="/projects" className="text-gray-800 dark:text-white">Projects</Link>
        <button 
          onClick={() => dispatch(toggleTheme())} 
          className="bg-gray-500 text-white px-4 py-1 rounded"
        >
          {darkMode ? "Light Mode" : "Dark Mode"}
        </button>
      </div>
    </nav>
  );
};

export default Navbar;
