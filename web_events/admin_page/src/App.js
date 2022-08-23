import './App.css'
import { Routes, Route, Link } from "react-router-dom"
import Home from './components/Home/Home'
import {default as Form} from './components/CreateForm/CreateForm'

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/edit" element={<Form />} />
      </Routes>
    </div>
  );
}

export default App
