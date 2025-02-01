import React from 'react';
import './Form.css';

const LoginForm = () => (
  <form>
    <label>Email address:</label>
    <input type="email" required />

    <label>Password:</label>
    <input type="password" required />

    <div className="checkbox-container">
      <input type="checkbox" id="remember-me" />
      <label htmlFor="remember-me">Remember Me</label>
    </div>

    <button type="submit">LOGIN</button>
    <div className="links">
      <a href="#">Forgot Password?</a>
      <a href="#">Create Account</a>
    </div>
  </form>
);

export default LoginForm;
