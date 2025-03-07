import React, { useState } from "react";
import { Form, Button, Image, Col, Row, Container, Alert } from "react-bootstrap";
import { Link, useHistory } from "react-router-dom";
import axios from "axios";

import styles from "../../styles/SignInUpForm.module.css";
import btnStyles from "../../styles/Button.module.css";
import appStyles from "../../App.module.css";
import login from "../../assets/login.png";
import { useSetCurrentUser } from "../../contexts/CurrentUserContext";


function SignInForm() {
  const setCurrentUser = useSetCurrentUser();
  const [signInData, setSignInData] = useState({
      username: "",
      password: ""
  });
  const {username, password} = signInData;
  const [errors, setErrors] = useState({});
  const history = useHistory();
  const handleChange = (event) => {
      setSignInData({
          ...signInData,
          [event.target.name]: event.target.value 
      });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const {data} = await axios.post('dj-rest-auth/login/', signInData);
      setCurrentUser(data);
      history.push("/");
    } catch (err) {
      setErrors(err.response?.data);
    }
  };

  return (
    <Row className={styles.Row}>
      <Col className="my-auto p-0 p-md-2" md={6}>
        <Container className={`${appStyles.Content} p-4 `}>
          <h1 className={styles.Header}>sign in</h1>
          <Form onSubmit={handleSubmit}>
            <Form.Group controlId="username">
              <Form.Label className="d-none">Username</Form.Label>
              <Form.Control
              className={styles.Input}
              type="text"
              placeholder="Username"
              name="username"
              value={username}
              onChange={handleChange}
              />
            </Form.Group>
            {errors.username?.map((message, idx) =>
              <Alert variant="warning" key={idx}>{message}</Alert>
              )}
            <Form.Group controlId="password">
              <Form.Label className="d-none">Password</Form.Label>
              <Form.Control
              className={styles.Input}
              type="password"
              placeholder="Password"
              name="password"
              value={password}
              onChange={handleChange}
              />
            </Form.Group>
            {errors.password?.map((message, idx) =>
              <Alert variant="warning" key={idx}>{message}</Alert>
              )}
            <Button 
            className={`${btnStyles.Button} ${btnStyles.Wide} ${btnStyles.Bright}`}
            type="submit">
              Sign in
            </Button>
            {errors.non_field_errors?.map((message, idx) => (
              <Alert key={idx} variant="warning" className="mt-3">
                {message}
              </Alert>
            ))}
          </Form>

        </Container>
        <Container className={`mt-3 ${appStyles.Content}`}>
          <Link className={styles.Link} to="/signup">
            Don't have an account? <span>Sign up now!</span>
          </Link>
        </Container>
      </Col>
      <Col
        md={6}
        className={`my-auto d-none d-md-block p-2 ${styles.SignInCol}`}
      >
        <Image
          className={`${appStyles.FillerImage}`}
          src={login}
        />
      </Col>
    </Row>
  );
}

export default SignInForm;