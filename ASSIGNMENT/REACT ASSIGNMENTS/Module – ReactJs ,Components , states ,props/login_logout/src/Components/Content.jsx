import React from "react";

function Content({ isLoggedIn }) {
  return (
    <div className="content">
      {isLoggedIn ? <h2>Private Views</h2> : <h2>Public Views</h2>}
    </div>
  );
}

export default Content;
