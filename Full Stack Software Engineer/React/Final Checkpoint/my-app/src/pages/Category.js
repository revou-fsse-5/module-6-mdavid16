// src/pages/Category.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Formik, Form, Field } from 'formik';
import * as Yup from 'yup';
import { TextField, Button, Container, Typography, List, ListItem, ListItemText, IconButton } from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';
import EditIcon from '@mui/icons-material/Edit';

const CategorySchema = Yup.object().shape({
  name: Yup.string().required('Required'),
});

const Category = () => {
  const [categories, setCategories] = useState([]);
  const [editingCategory, setEditingCategory] = useState(null);

  useEffect(() => {
    fetchCategories();
  }, []);

  const fetchCategories = () => {
    axios.get('https://github.com/revou-fsse-5/module-4-server/categories')
      .then(response => {
        setCategories(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };

  const handleDelete = (id) => {
    axios.delete(`https://github.com/revou-fsse-5/module-4-server/categories/${id}`)
      .then(() => {
        fetchCategories();
      })
      .catch(error => {
        console.error(error);
      });
  };

  const handleEdit = (category) => {
    setEditingCategory(category);
  };

  return (
    <Container>
      <Typography variant="h4">Categories</Typography>
      <Formik
        initialValues={{ name: editingCategory ? editingCategory.name : '' }}
        validationSchema={CategorySchema}
        enableReinitialize
        onSubmit={(values, { setSubmitting, resetForm }) => {
          const apiCall = editingCategory
            ? axios.put(`https://github.com/revou-fsse-5/module-4-server/categories/${editingCategory.id}`, values)
            : axios.post('https://github.com/revou-fsse-5/module-4-server/categories', values);

          apiCall
            .then(() => {
              fetchCategories();
              resetForm();
              setEditingCategory(null);
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
            <Field name="name" as={TextField} label="Category Name" fullWidth margin="normal" />
            <Button type="submit" variant="contained" color="primary" disabled={isSubmitting}>
              {editingCategory ? 'Update' : 'Add'} Category
            </Button>
          </Form>
        )}
      </Formik>
      <List>
        {categories.map(category => (
          <ListItem key={category.id}>
            <ListItemText primary={category.name} />
            <IconButton edge="end" onClick={() => handleEdit(category)}>
              <EditIcon />
            </IconButton>
            <IconButton edge="end" onClick={() => handleDelete(category.id)}>
              <DeleteIcon />
            </IconButton>
          </ListItem>
        ))}
      </List>
    </Container>
  );
};

export default Category;