import {BrowserRouter, Routes, Route} from 'react-router-dom'
import './App.css'
import HomePage from './Pages/HomePage'
import Problems from './Pages/Problems'
import LoginSignup from './Pages/LoginSignup'
import ProblemWorkspace from './Pages/ProblemWorkspace'
import Navbar from './Components/Navbar/Navbar'
import About from './Pages/About'

function App() {
  

  return (
    <div className='app'>
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path='/' element={<HomePage />}/>
          <Route path='/problems' element={<Problems />} />
          <Route path='/problems/:problemId' element={<ProblemWorkspace />}/>
          <Route path='/about' element={<About/>}/>
          <Route path='/auth' element={<LoginSignup />}/>
        </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App
