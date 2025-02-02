import { configureStore } from "@reduxjs/toolkit";
import userReducer from "../reducers/userReducer";

const store = configureStore({
  reducer: {
    users: userReducer,
  },
  devTools: process.env.NODE_ENV !== "production",
});

export default store;
