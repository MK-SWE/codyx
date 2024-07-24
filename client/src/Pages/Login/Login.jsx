import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { login } from '../../redux/reducers/authSlice';
import { Link } from 'react-router-dom';
import './Login.css';
import { useNavigate, useLocation } from 'react-router-dom';


const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();
  const location = useLocation();
  const [errors, setErrors] = useState({});

  const validate = () => {
    const newErrors = {};
  
    if (!email) {
      newErrors.email = 'Email is required.';
    } else if (!/^\S+@\S+\.\S+$/.test(email)) {
      newErrors.email = 'Invalid email format.';
    }
  
    if (!password || password.length < 6) {
      newErrors.password = 'Password must be at least 6 characters long.';
    }
  
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };
  
  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const dispatch = useDispatch();
  const from = location.state?.from || '/'; 
  const handleSubmit = async(e) => {
    e.preventDefault();
    try {
      if (validate()) {
        await dispatch(login({ email, password }));
        navigate(from, { replace: true });
      }
    } catch (error) {
      console.error('Login error:', error);
    }

  };

  return (
    <div className='login-form'>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Email:</label>
          <input 
            type="email" 
            value={email} 
            onChange={handleEmailChange} 
            placeholder="Enter your Email"/>
            {errors.email && <p className="error">{errors.email}</p>}
        </div>
        <div>
          <label>Password:</label>
          <input 
            type="password" 
            value={password} 
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