import { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { login } from '../../redux/reducers/authSlice';
import { Link } from 'react-router-dom';
import './Login.css';
import { useNavigate, useLocation } from 'react-router-dom';



const Login = () => {
  const [Username, setUsername] = useState('');
  const [Password, setPassword] = useState('');
  const navigate = useNavigate();
  const location = useLocation();
  const [errors, setErrors] = useState({});
  const login_error = useSelector((state) => state.user.error);

  const validate = () => {
    const newErrors = {};
  
    if (!Username) {
      newErrors.Username = 'Username is required.';
    } else if (!/^[A-Za-z0-9_]{3,20}$/i.test(Username)) {
      newErrors.Username = 'Invalid Username format.';
    }
  
    if (!Password || Password.length < 6) {
      newErrors.password = 'Password must be at least 6 characters long.';
    }
  
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };
  
  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const dispatch = useDispatch();
  const from = location.state?.from || '/problems';

  const handleSubmit = async(e) => {
    e.preventDefault();
    try {
      if (validate()) {
        await dispatch(login({ Username, Password }));
        if (login_error) {
          navigate(from, { replace: true });
        }
      }
    } catch (error) {
      console.error('Login error:', error);
    }

  };

  return (
    <div className='login-form'>
      {login_error && <p className="error">{login_error}</p>}
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Username:</label>
          <input 
            type="text" 
            value={Username} 
            onChange={handleUsernameChange} 
            placeholder="Enter your Email"/>
            {errors.Username && <p className="error">{errors.Username}</p>}
        </div>
        <div>
          <label>Password:</label>
          <input 
            type="password" 
            value={Password} 
            onChange={handlePasswordChange} 
            placeholder="Enter your password"
          />
          {errors.password && <p className="error">{errors.password}</p>}
        </div>
        <button type="submit">Login</button>
        <div>
          <p>Don&apos;t have an account? <Link to='/signup'>Sign up</Link></p>
        </div>
      </form>
    </div>
  );
};

export default Login;