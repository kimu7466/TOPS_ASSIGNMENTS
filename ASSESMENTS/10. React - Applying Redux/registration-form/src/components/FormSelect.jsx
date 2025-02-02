import React from 'react';

function FormSelect({ name, value, onChange, options }) {
  return (
    <select name={name} value={value} onChange={onChange}>
      {options.map((option) => (
        <option key={option} value={option}>
          {option}
        </option>
      ))}
    </select>
  );
}

export default FormSelect;
