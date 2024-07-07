import express from 'express';
import http from 'http';
import bodyParser from 'body-parser';
import cookieParser from 'cookie-parser';
import compression from 'compression';
import cors from 'cors';
import mongoose from 'mongoose';
require('dotenv').config();

import router from './router';

const PORT = process.env.API_PORT || 8080;
const app = express();

app.use(
  cors({
    credentials: true,
  }),
);

app.use(compression());
app.use(cookieParser());
app.use(bodyParser.json());

const server = http.createServer(app);

server.listen(PORT, () => {
  console.log(`Server running on http://${process.env.API_URL}:${PORT}`);
});

mongoose.Promise = Promise;

mongoose.connect(process.env.MONGO_URL);
mongoose.connection.on('error', (err: Error) => console.log(err));

app.use('/', router());
