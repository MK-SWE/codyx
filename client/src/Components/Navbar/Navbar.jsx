import { Link } from "react-router-dom";
import './Navbar.css';
import { useState } from "react";
import { useSelector } from "react-redux";
import { authActions } from "../../redux/reducers/authSlice";
import { useDispatch } from "react-redux";

function Navbar() {
  const isLoggedIn = useState(useSelector(state => state.user.isAuthenticated))[0];
  const dispatch = useDispatch();
  const handleLogout = () => {
    dispatch(authActions.logout());
  }

  return (
    <div className="navbar">
      <h1><Link to="/">codyX</Link></h1>
      <ul className="nav-menu">
        <li><Link to="/problems">Problems</Link></li>
        <li><Link to="/about">About</Link></li>
      </ul>
      <div className="login">
        {isLoggedIn ? (
          <Link to="/" onClick={handleLogout}><button>Logout</button></Link>
        ) : (
          <Link to="/login"><button>Login</button></Link>
        )}
      </div>
    </div>
  )
}

export default Navbar