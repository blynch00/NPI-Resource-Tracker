
import express from 'express';
import 'dotenv/config';


// Imported routes from Router handling functions
import providers from './routes/providers.js';
import home from './routes/home.js';
import saved from './routes/savednums.js';

const app = express();
app.use(express.json());
const PORT = Number(process.env.PORT) || 3000;

app.use(express.json());

app.use('/', home);
app.use('/providers', providers);
app.use('/saved', saved);
app.listen(PORT, () => {
  console.log(`Server is running on port http://localhost:${PORT}`);
});