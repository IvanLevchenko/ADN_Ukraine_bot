import './App.scss';
import { useEffect, useState } from 'react'
import { Routes, Route, Link } from "react-router-dom"
import {useSelector} from "react-redux"
import {getProducts} from "./api/api"
import WebApp from "./components/WebApp/WebApp"
import AdminPage from "./components/AdminPage/AdminPage"
import AdminForm from "./components/AdminForm/AdminForm"

function App() {
  const productsSelector = useSelector(state => state.products.products)

  useEffect(() => {
    init(window.Telegram)
    getProducts()
    console.log(productsSelector)
  }, [productsSelector.length])


  function init(telegram) {
    telegram.WebApp.ready()
    telegram.WebApp.MainButton.isVisible = true
  }

  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<WebApp />} />
        <Route path="/admin" element={<AdminPage />} />
        <Route path="/edit/product/:id" element={<AdminForm />} />
      </Routes>

    </div>
  );
}

export default App;
