import React, { useState } from 'react';
import './App.css';
import Modal from './components/Modal';
import LoginForm from './components/LoginForm';
import RegistrationForm from './components/RegistrationForm';

function App() {
  const [isLoginOpen, setIsLoginOpen] = useState(false);
  const [isRegisterOpen, setIsRegisterOpen] = useState(false);

  return (
    <div className="app-container">
      <button onClick={() => setIsLoginOpen(true)}>Login</button>
      <button onClick={() => setIsRegisterOpen(true)}>Register</button>

      <Modal isOpen={isLoginOpen} onClose={() => setIsLoginOpen(false)} title="Login">
        <LoginForm />
      </Modal>

      <Modal isOpen={isRegisterOpen} onClose={() => setIsRegisterOpen(false)} title="Register">
        <RegistrationForm />
      </Modal>
    </div>
  );
}

export default App;
