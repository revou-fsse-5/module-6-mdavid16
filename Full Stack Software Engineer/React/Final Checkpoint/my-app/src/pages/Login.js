// src/pages/Login.js
import React from 'react';
import { Formik, Form, Field } from 'formik';
import * as Yup from 'yup';
import axios from 'axios';
import { TextField, Button, Container, Typography } from '@mui/material';

const LoginSchema = Yup.object().shape({
  username: Yup.string().required('Required'),
  password: Yup.string().required('Required'),
});

const Login = () => {
  return (
    <Container>
      <Typography variant="h4">Login</Typography>
      <Formik
        initialValues={{ username: '', password: '' }}
        validationSchema={LoginSchema}
        onSubmit={(values, { setSubmitting }) => {
          axios.post('https://github.com/revou-fsse-5/module-4-server/login', values)
            .then(response => {
              console.log(response.data);
              localStorage.setItem('token', response.data.token);
              setSubmitting(false);
            })
            .catch(error => {
              console.error(error);
              setSubmitting(false);
            });
        }}
      >
        {({ isSubmitting }) => (
          <Form>
            <Field name="username" as={TextField} label="Username" fullWidth margin="normal" />
            <Field name="password" as={TextField} label="Password" type="password" fullWidth margin="normal" />
            <Button type="submit" variant="contained" color="primary" disabled={isSubmitting}>
              Login
            </Button>
          </Form>
        )}
      </Formik>
    </Container>
  );
};

export default Login;