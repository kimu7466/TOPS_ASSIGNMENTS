  import axios from "axios";

  const API_URL = "http://localhost:5000/users";

  export const fetchUsers = () => async (dispatch) => {
    try {
      const response = await axios.get(API_URL);
      dispatch({ type: "FETCH_USERS", payload: response.data });
    } catch (error) {
      console.error("Error fetching users:", error);
    }
  };

  export const addUser = (user) => async (dispatch) => {
    try {
      await axios.post(API_URL, user);
      dispatch(fetchUsers());
    } catch (error) {
      console.error("Error adding user:", error);
    }
  };

  export const deleteUser = (id) => async (dispatch) => {
    try {
      await axios.delete(`${API_URL}/${id}`);
      dispatch(fetchUsers());
    } catch (error) {
      console.error("Error deleting user:", error);
    }
  };

  export const updateUser = (id, user) => async (dispatch) => {
    try {
      await axios.put(`${API_URL}/${id}`, user);
      dispatch(fetchUsers());
    } catch (error) {
      console.error("Error updating user:", error);
    }
  };
