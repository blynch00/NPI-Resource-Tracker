import express from 'express';
const router =  express.Router();
import { fileURLToPath } from 'url';
import path from 'path';

// 1. Converts 'file:///Users/username/project/src/app.js' to a standard file path
const __filename = fileURLToPath(import.meta.url);

// 2. Extracts just the folder path, effectively recreating __dirname
const __dirname = path.dirname(__filename); 

// middleware that is specific to this router
const timeLog = (req, res, next) => {
  console.log('Time: ', Date.now());
  next();
};
router.use(timeLog);
// Saved information
router.get('/', (req,res) => {
    res.status(200).send("Will return list of user's saved info from DB");
})

router.delete('/:id', (req,res) => {
    res.status(200).send("Will delete provider from table, if applicable.");
})


export default router