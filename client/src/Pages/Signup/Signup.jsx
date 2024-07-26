import { useState } from 'react';
import { useDispatch} from 'react-redux';
import { register } from '../../redux/reducers/authSlice';
import { Link } from 'react-router-dom';
import './Signup.css';
import { useNavigate, useLocation } from 'react-router-dom';


const Signup = () => {
  const [Username, setUsername] = useState('');
  const [Email, setEmail] = useState('');
  const [Password, setPassword] = useState('');
  const [Name, setName] = useState('');
  const [errors, setErrors] = useState({});
  const navigate = useNavigate();
  const location = useLocation();

  const validate = () => {
    const newErrors = {};

    if (!Name) {
      newErrors.name = 'Name is required.';
    }

    if (!Email) {
      newErrors.Email = 'Email is required.';
    } else if (!/^\S+@\S+\.\S+$/.test(Email)) {
      newErrors.email = 'Invalid email format.';
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
  const from = location.state?.from || '/login'; 
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (validate()) {
        await dispatch(register({ Username, Name, Email, Password}));
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
          <label>Username:</label>
          <input 
            type="text" 
            value={Username} 
            onChange={handleUsernameChange}
            placeholder="Enter your Username"
          />
          {errors.Username && <p className="error">{errors.Username}</p>}
        </div>
        <div>
          <label>Name:</label>
          <input 
            type="text" 
            value={Name} 
            onChange={handleNameChange}
            placeholder="Enter your Name"
          />
          {errors.name && <p className="error">{errors.name}</p>}
        </div>
        <div>
          <label>Email:</label>
          <input 
            type="email" 
            value={Email} 
            onChange={handleEmailChange} 
            placeholder="Enter your Email"
          />
          {errors.email && <p className="error">{errors.email}</p>}
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
        <button type="submit">Sign Up</button>
        <div>
          <p>Already have an account? <Link to='/login'>Log in</Link></p>
        </div>
      </form>
    </div>
  );
};

export default Signup;
