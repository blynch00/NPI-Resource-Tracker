import express from 'express';
import test_npi from '../test_npi.js';
const router = express.Router();

// middleware that is specific to this router
const timeLog = (req, res, next) => {
  console.log('Time: ', Date.now());
  next();
};
router.use(timeLog);


// Providers general; required for form search and MySQL Queries
router.get('/', (req, res) => {
  res.send('Provider Lookup Homepage');
});


router.get('/test', (req,res) => {
  res.status(200).json(test_npi);
})


router.get('/:id', (req, res) => {
  res.send(`id of ${req.params.id} given.`);
})

export default router;