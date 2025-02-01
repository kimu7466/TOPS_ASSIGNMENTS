import React from 'react';
import './Form.css';

const RegistrationForm = () => (
  <form>
    <label>Full Name:</label>
    <input type="text" required />

    <label>Email:</label>
    <input type="email" required />

    <label>Password:</label>
    <input type="password" required />

    <button type="submit">REGISTER</button>
  </form>
);

export default RegistrationForm;
