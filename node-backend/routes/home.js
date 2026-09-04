import express from 'express';

const router = express.Router();


router.get('/', (req,res) => {
    res.send("Route: Home");
})
router.get('/about', (req,res) => {
    res.send("Route: About");
})
router.get('/user', (req,res) => {
    res.send("Route: User. This is where we will mount additional information")
})
export default router;