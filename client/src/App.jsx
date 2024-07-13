import {BrowserRouter, Routes, Route} from 'react-router-dom'
import './App.css'
import HomePage from './Pages/HomePage'
import Problems from './Pages/Problems'
import LoginSignup from './Pages/LoginSignup'
import ContentLearn from './Pages/ContentLearn'
import ProblemWorkspace from './Pages/ProblemWorkspace'
import Navbar from './Components/Navbar/Navbar'

function App() {
  

  return (
    <div className='app'>
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path='/' element={<HomePage />}/>
          <Route path='/problems' element={<Problems />} />
          <Route path='/problems/:problemId' element={<ProblemWorkspace />}/>
          <Route path='/content' element={<ContentLearn />}/>
          <Route path='/auth' element={<LoginSignup />}/>
        </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App
