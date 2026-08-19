import { Link } from "react-router-dom"
import './Navbar.css'

export function Navbar(){
    return (
        <nav className="navbar">
            <Link to="/" className="navbar-link">
            Home 
            </Link>
            <Link to="/UserPage" className="navbar-link"> 
            Account
            </Link>
            <Link to="/StoredNumbers" className="navbar-link">
            Personal List 
             </Link>
            <Link to="/NumberLookup" className="navbar-link"> 
            NPI Lookup 
            </Link>
        </nav>
    )
}
