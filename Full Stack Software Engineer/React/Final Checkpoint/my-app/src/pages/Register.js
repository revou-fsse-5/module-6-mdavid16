// src/pages/Register.js
import React from 'react';
import { Formik, Form, Field } from 'formik';
import * as Yup from 'yup';
import axios from 'axios';
import { TextField, Button, Container, Typography } from '@mui/material';

const RegisterSchema = Yup.object().shape({
  username: Yup.string().required('Required'),
  password: Yup.string().required('Required'),
});

const Register = () => {
  return (
    <Container>
      <Typography variant="h4">Register</Typography>
      <Formik
        initialValues={{ username: '', password: '' }}
        validationSchema={RegisterSchema}
        onSubmit={(values, { setSubmitting }) => {
          axios.post('https://github.com/revou-fsse-5/module-4-server/register', values)
            .then(response => {
              console.log(response.data);
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
              Register
            </Button>
          </Form>
        )}
      </Formik>
    </Container>
  );
};

export default Register;