import styled from "styled-components";

const HeroSection = styled.section`
  height: 50vh;
  background: url("https://source.unsplash.com/1600x900/?shopping") center/cover;
  display: flex;
  justify-content: center;
  align-items: center;
  color: black;
  font-size: 2rem;
  font-weight: bold;
`;

const Hero = () => <HeroSection>Welcome to My-E-Shop - Your Fashion Hub</HeroSection>;

export default Hero;