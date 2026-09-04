import { Link } from "react-router-dom"
import './Navbar.css'

export function Navbar(){
    return (
        <nav className="navbar">
            <Link to="/UserPage" className="navbar-link"> 
            User
            </Link>
            <Link to="/StoredNumbers" className="navbar-link">
            Personal List 
             </Link>
            <Link to="/NumberLookup" className="navbar-link"> 
            NPI Lookup 
            </Link>
            <Link to="/About" className="navbar-link"> 
            About
            </Link>
        </nav>
    )
}
