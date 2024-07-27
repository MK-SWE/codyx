import { Link } from "react-router-dom";
import './Navbar.css';
import { useSelector } from "react-redux";
import { useDispatch } from "react-redux";
import { logout } from "../../redux/reducers/authSlice";
import { LuLogOut } from "react-icons/lu";
import { FaUserCircle } from "react-icons/fa";
import useAuth from "../../redux/useAuth";

function Navbar() {
  useAuth();
  const isLoggedIn = useSelector(state => state.user.isAuthenticated);
  const email = useSelector(state => state.user.user?.email)
  const dispatch = useDispatch();
  const handleLogout = () => {
    dispatch(logout());
  }

  return (
    <div className="navbar">
      <h1><Link to="/">codyX</Link></h1>
      <ul className="nav-menu">
        {isLoggedIn? <li><Link to="/problems">Problems</Link></li> :
        <li><Link to="/login">Problems</Link></li>}
        <li><Link to="/about">About</Link></li>
      </ul>
      <div className="login">
        {console.log("isloggedIn",isLoggedIn)}
        {isLoggedIn ? (
          <>
          <Link to="/" onClick={handleLogout}><LuLogOut className="logout-icon"/></Link>
          <FaUserCircle className="user-icon"/>
          <span className="user-email">{email? email : null}</span>
          </>
        ) : (
          <Link to="/login"><button>Login</button></Link>
        )}
      </div>
    </div>
  )
}

export default Navbar;
