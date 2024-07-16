import { Link } from "react-router-dom";
import './Navbar.css'

function Navbar() {
  return (
    <div className="navbar">
      <h1><Link to="/">
      codyX
      </Link></h1>
      <ul className="nav-menu">
        <li><Link to="/problems">Problems</Link></li>
        <li><Link to="/about">About</Link></li>
      </ul>
      <div className="login">
        <Link to="/auth"><button>Login</button></Link>
      </div>
    </div>
  )
}

export default Navbar