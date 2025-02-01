import React, { useState, useEffect } from 'react';

const MouseTracker = () => {
  const [position, setPosition] = useState({ x: 0, y: 0 });

  useEffect(() => {
    const handleMouseMove = (event) => {
      setPosition({
        x: event.clientX,
        y: event.clientY
      });
    };

    window.addEventListener('mousemove', handleMouseMove);

    return () => {
      window.removeEventListener('mousemove', handleMouseMove);
    };
  }, []);

  return (
    <div style={{ height: '100vh' }}>
      <div
        style={{
          position: 'absolute',
          backgroundColor: '#ff5722',
          borderRadius: '50%',
          width: '50px',
          height: '50px',
          left: position.x - 25,
          top: position.y - 25,
          transition: 'all 0.1s ease',
        }}
      />
    </div>
  );
};

export default MouseTracker;
