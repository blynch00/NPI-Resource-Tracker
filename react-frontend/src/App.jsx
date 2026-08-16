import './App.css'
import { HashRouter as HRouter, Routes, Route } from 'react-router-dom'
import { Home } from './pages/HomePage'
import { NumberLookup } from './pages/NumberLookup'
import { StoredNumbers } from './pages/StoredNumbers'
import { UserPage } from './pages/UserPage'
import { Layout } from './Layout'

function App() {

    return (
        <div>
            <HRouter>
                <Routes>
                    <Route element = {<Layout/>}>
                        <Route path="/" element={<Home/>}/>
                        <Route path="/NumberLookup" element={<NumberLookup/>}/>
                        <Route path="/StoredNumbers" element={<StoredNumbers/>}/>
                        <Route path="/UserPage" element={<UserPage/>}/>
                    </Route>
                    
                </Routes>
            </HRouter>
        </div>
    )
    

}

export default App
