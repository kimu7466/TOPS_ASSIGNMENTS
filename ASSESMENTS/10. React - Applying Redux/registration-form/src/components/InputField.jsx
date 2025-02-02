import React from 'react';

function InputField({ name, value, onChange, placeholder, type = "text", required = false }) {
  return (
    <input
      type={type}
      name={name}
      value={value}
      onChange={onChange}
      placeholder={placeholder}
      required={required}
    />
  );
}

export default InputField;
