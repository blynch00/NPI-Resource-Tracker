import './App.css'
import { HashRouter as HRouter, Routes, Route } from 'react-router-dom'
import { NumberLookup } from './pages/NumberLookup'
import { StoredNumbers } from './pages/StoredNumbers'
import { UserPage } from './pages/UserPage'
import { Layout } from './Layout'
import { AboutPage } from './pages/AboutPage'

function App() {

    return (
        <div>
            <HRouter>
                <Routes>
                    <Route element = {<Layout/>}>
                        <Route path="/NumberLookup" element={<NumberLookup/>}/>
                        <Route path="/StoredNumbers" element={<StoredNumbers/>}/>
                        <Route path="/UserPage" element={<UserPage/>}/>
                        <Route path='/About' element={<AboutPage/>}/>
                    </Route>
                    
                </Routes>
            </HRouter>
        </div>
    )
    

}

export default App
