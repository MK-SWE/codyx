import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { register } from '../../redux/reducers/authSlice';
import { Link } from 'react-router-dom';
import './Signup.css';
import { useNavigate, useLocation } from 'react-router-dom';


const Signup = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');
  const [errors, setErrors] = useState({});
  const navigate = useNavigate();
  const location = useLocation();

  const validate = () => {
    const newErrors = {};

    if (!name) {
      newErrors.name = 'Name is required.';
    }

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

  const handleNameChange = (e) => {
    setName(e.target.value);
  };

  const dispatch = useDispatch();
  const from = location.state?.from || '/'; 
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (validate()) {
        await dispatch(register({ name, email, password}));
        navigate(from, { replace: true });
      }
    } catch (error) {
      console.error('Login error:', error);
    }
    
  };

  return (
    <div className='signup-form'>
      <h2>Signup</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Name:</label>
          <input 
            type="text" 
            value={name} 
            onChange={handleNameChange}
            placeholder="Enter your Name"
          />
          {errors.name && <p className="error">{errors.name}</p>}
        </div>
        <div>
          <label>Email:</label>
          <input 
            type="email" 
            value={email} 
            onChange={handleEmailChange} 
            placeholder="Enter your Email"
          />
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
        <button type="submit">Sign Up</button>
        <div>
          <p>Already have an account? <Link to='/login'>Log in</Link></p>
        </div>
      </form>
    </div>
  );
};

export default Signup;
