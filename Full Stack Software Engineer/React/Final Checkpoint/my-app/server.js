const jsonServer = require("json-server");
const auth = require("json-server-auth");

const app = jsonServer.create();
const router = jsonServer.router("db.json");
const middlewares = jsonServer.defaults();

// Set default middlewares (logger, static, cors and no-cache)
app.use(middlewares);

// To handle POST, PUT and PATCH you need to use a body-parser
app.use(jsonServer.bodyParser);

// /!\ Bind the router db to the app
app.db = router.db;

// You must apply the auth middleware before the router
app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "*");
  next();
});
app.use(auth);
app.use(router);

const PORT = 8080;
app.listen(PORT, () => {
  console.log(`JSON Server is running on port ${PORT}`);
});

import React from 'react';
import { TextField, Button, Container, Typography } from '@mui/material';
import { Formik, Form, Field } from 'formik';
import * as Yup from 'yup';
import axios from 'axios';

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
          axios.post('http://localhost:8080/register', values)
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
            <Field as={TextField} name="username" label="Username" fullWidth margin="normal" />
            <Field as={TextField} name="password" label="Password" type="password" fullWidth margin="normal" />
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

npx create-react-app my-app
cd my-app
npm install @mui/material @emotion/react @emotion/styled formik yup axios react-router-dom
