import {BrowserRouter, Routes, Route} from 'react-router-dom'
import './App.css'
import HomePage from './Pages/HomePage'
import Problems from './Pages/Problems'
import ProblemWorkspace from './Pages/ProblemWorkspace'
import Navbar from './Components/Navbar/Navbar'
import About from './Pages/About';
import store from './store';
import { Provider } from 'react-redux';
import Login from './Pages/Login/Login'
import Signup from './Pages/Signup/Signup';

function App() {
  
  return (
    <div className='app'>
      <Provider store={store}>
        <BrowserRouter>
          <Navbar />
          <Routes>
            <Route path='/' element={<HomePage />}/>
            <Route path='/problems' element={<Problems />} />
            <Route path='/problems/:problemId' element={<ProblemWorkspace />}/>
            <Route path='/about' element={<About/>}/>
            <Route path='/login' element={<Login />}/>
            <Route path='/signup' element={<Signup />}/>
            <Route path='*' element={<h1>404 Not Found</h1>} />
          </Routes>
        </BrowserRouter>
      </Provider>
    </div>
  )
}

export default App
