import React from "react";
import { Navbar, Container, Nav } from "react-bootstrap";
import logo from "../assets/logo.png";
import styles from '../styles/NavBar.module.css';
import { NavLink } from 'react-router-dom';
import { useCurrentUser, useSetCurrentUser } from "../contexts/CurrentUserContext";
import Avatar from "./Avatar";
import axios from "axios";
import useClickOutsideToggle from "../hooks/useClickOutsideToggle";

const NavBar = () => {
  const currentUser = useCurrentUser();
  const setCurrentUser = useSetCurrentUser();
  const {expanded, setExpanded, ref} = useClickOutsideToggle();

  const handleSignOut = async () => {
    try {
      await axios.post("dj-rest-auth/logout/");
      setCurrentUser(null);
    } catch (err) {
      console.log(err);
    }
  };

  const addPostIcon = (
    <NavLink
    className={styles.NavLink}
    activeClassName={styles.Active}
    to="/posts/create"
  >
    <i className="fas fa-plus-square"></i>Spill the Tea!
  </NavLink>
  )
  const loggedInIcons = <>
    <NavLink
      className={styles.NavLink}
      activeClassName={styles.Active}
      to="/feed"
    >
      <i className="fas fa-stream"></i>Blend
    </NavLink>
    <NavLink
      className={styles.NavLink}
      activeClassName={styles.Active}
      to="/chatrooms"
    >
      <i className="fa-solid fa-person-booth"></i>TeaRooms
    </NavLink>
    <NavLink
      className={styles.NavLink}
      activeClassName={styles.Active}
      to="/liked"
    >
      <i className="fa-solid fa-mug-hot"></i>Tea-lightful
    </NavLink>
    <NavLink
      className={styles.NavLink}
      to="/"
      onClick={handleSignOut}
    >
      <i className="fas fa-sign-out-alt"></i>Sign Out
    </NavLink>
    <NavLink
      className={styles.NavLink}
      to={`/profiles/${currentUser?.profile_id}`}
    >
      <Avatar src={currentUser?.profile_image} text='My Blend' height={40}/>
    </NavLink>
  </>;
  const loggedOutIcons = (
  <> 
    <NavLink
    className={styles.NavLink}
    activeClassName={styles.Active}
    to="/signin"
  >
    <i className="fas fa-sign-in-alt"></i>Re-steep
  </NavLink>
  <NavLink
    to="/register"
    className={styles.NavLink}
    activeClassName={styles.Active}
  >
    <i className="fas fa-user-plus"></i>Register
  </NavLink>
</>
  );

  return (
    <Navbar expanded={expanded} className={styles.NavBar} expand="md" fixed="top">
      <Container>
      <NavLink to="/">
          <Navbar.Brand>
            <img src={logo} alt="logo" height="45" />
          </Navbar.Brand>
        </NavLink>
        {currentUser && addPostIcon}
        <Navbar.Toggle
          ref={ref}
          onClick={() => setExpanded(!expanded)} 
          aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="ml-auto text-left">
            <NavLink
              exact
              className={styles.NavLink}
              activeClassName={styles.Active}
              to="/"
            >
              <i className="fas fa-home"></i>Home
            </NavLink>
            {currentUser ? loggedInIcons : loggedOutIcons}
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default NavBar;