import './App.css';
import { useEffect, useState } from 'react';

function App() {

  useEffect(() => {
    init(window.Telegram)
  }, [])
  
  function init(telegram) {
    telegram.WebApp.ready()
    telegram.WebApp.MainButton.isVisible = true
    console.log(telegram)
  }

  return (
    <div className="App">
       <h1>Hello!!!!</h1>
    </div>
  );
}

export default App;
