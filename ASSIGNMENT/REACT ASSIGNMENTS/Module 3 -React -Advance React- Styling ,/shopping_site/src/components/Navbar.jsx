import styled from "styled-components";


const NavbarContainer = styled.nav`
  background: #333;
  color: white;
  padding: 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
`;

const NavLinks = styled.ul`
  list-style: none;
  display: flex;
  gap: 20px;
  margin: 0;
  padding: 0;
`;

const NavLink = styled.li`
  cursor: pointer;
  &:hover {
    color: #ffcc00;
  }
`;

const Navbar = () => (
  <NavbarContainer>
    <h1>My-E-Shop</h1>
    <NavLinks>
      <NavLink>Home</NavLink>
      <NavLink>Shop</NavLink>
      <NavLink>Contact</NavLink>
      <NavLink>Cart 🛒</NavLink>
    </NavLinks>
  </NavbarContainer>
);

export default Navbar;