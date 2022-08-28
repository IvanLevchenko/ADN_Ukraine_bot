import './App.scss';
import { useEffect } from 'react'
import { Routes, Route } from "react-router-dom"
import { getProducts } from './api/api';
import WebApp from "./components/WebApp/WebApp"
import AdminPage from "./components/AdminPage/AdminPage"
import AdminForm from "./components/AdminForm/AdminForm"
import LoginForm from './components/LoginForm/LoginForm';
import AdminRoute from './components/AdminRoute/AdminRoute';

function App() {

  useEffect(() => {
    init(window.Telegram)
    getProducts()
  }, [])

  function init(telegram) {
    telegram.WebApp.ready()
    telegram.WebApp.MainButton.isVisible = true
  }
  localStorage.clear()

  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<WebApp />} />
        <Route path="/admin" element={<LoginForm />} />
        <Route path="/admin-page" element={<AdminRoute Component={AdminPage} />} />
        <Route path="/edit/product/:id" element={<AdminRoute Component={AdminForm} />} />
      </Routes>
    </div>
  );
}

export default App;
