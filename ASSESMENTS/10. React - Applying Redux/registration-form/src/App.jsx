import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { setField } from './actions';
import './App.css';
import InputField from './components/InputField';
import FormSelect from './components/FormSelect';

function App() {
  const dispatch = useDispatch();
  const formData = useSelector((state) => state);

  const handleChange = (e) => {
    const { name, value } = e.target;
    dispatch(setField(name, value));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    
    if (!validateEmail(formData.email)) {
      alert('Please enter a valid email address.');
      return;
    }

    if (formData.password !== formData.retypePassword) {
      alert('Passwords do not match. Please try again.');
      return;
    }

    
    console.log('Form submitted:', formData);
  };

  const validateEmail = (email) => {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
  };

  return (
    <div className="App">
      <h1>Registration Form</h1>
      <form onSubmit={handleSubmit}>
        <InputField
          name="email"
          value={formData.email}
          onChange={handleChange}
          placeholder="Email"
          type="email"
          required
        />
        <InputField
          name="password"
          value={formData.password}
          onChange={handleChange}
          placeholder="Password"
          type="password"
          required
        />
        <InputField
          name="retypePassword"
          value={formData.retypePassword}
          onChange={handleChange}
          placeholder="Retype Password"
          type="password"
          required
        />
        <InputField
          name="firstName"
          value={formData.firstName}
          onChange={handleChange}
          placeholder="First Name"
          required
        />
        <InputField
          name="lastName"
          value={formData.lastName}
          onChange={handleChange}
          placeholder="Last Name"
          required
        />
        <InputField
          name="phoneNumber"
          value={formData.phoneNumber}
          onChange={handleChange}
          placeholder="Phone Number"
          type="tel"
          required
        />
        <InputField
          name="address"
          value={formData.address}
          onChange={handleChange}
          placeholder="Address"
          required
        />
        <InputField
          name="town"
          value={formData.town}
          onChange={handleChange}
          placeholder="Town"
          required
        />
        <InputField
          name="region"
          value={formData.region}
          onChange={handleChange}
          placeholder="Region"
          required
        />
        <InputField
          name="postcode"
          value={formData.postcode}
          onChange={handleChange}
          placeholder="Postcode"
          required
        />
        <FormSelect
          name="country"
          value={formData.country}
          onChange={handleChange}
          options={['India', 'United States', 'United kingdom', 'Canada']} 
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default App;
