// const mongoose = require('mongoose');
import mongoose from 'mongoose';
import { success, error } from "consola";


mongoose.connect('mongodb://localhost/<your_database_name>', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

const db = mongoose.connection;
db.on('error', function() {
    error('Error connecting to MongoDB');
});
db.once('open', function() {
  success({message:'Connected to MongoDB', badge: true,});
});
