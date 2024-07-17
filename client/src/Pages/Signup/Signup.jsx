import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { register } from '../../redux/reducers/authSlice';
import { Link } from 'react-router-dom';

const Signup = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');

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
  const handleSubmit = (e) => {
    e.preventDefault();
    dispatch(register({ name, email, password}));
  };

  return (
    <div>
      <h2>Signup</h2>
      <form onSubmit={handleSubmit}>
        <label>Name:</label>
        <input type="text" value={name} onChange={handleNameChange} />
        <label>Email:</label>
        <input type="email" value={email} onChange={handleEmailChange} />
        <label>Password:</label>
        <input type="password" value={password} onChange={handlePasswordChange} />
        <button type="submit">Sign Up</button>
        <div>
          <p>Already have an account? <Link to='/login'>Log in</Link></p>
        </div>
      </form>
    </div>
  );
};

export default Signup;
