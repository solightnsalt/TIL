import React from "react";

function Header(props) {
  return (
    <>
      <Header
        style={{
          margin: "10",
          border: "1px solid pink",
          textAlign: "center",
        }}
      >
        짱구네 가족
      </Header>
      {props.children}
    </>
  );
}

export default Header;
