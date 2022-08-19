import './App.css';
import { useEffect, useState } from 'react';

function App() {

  useEffect(() => {
    const script = document.createElement('script')
    script.src = 'https://telegram.org/js/telegram-web-app.js'
    script.async = true
    document.head.append(script)
    script.onload = () => init(window.Telegram)
  }, [])
  
  function init(telegram) {
    telegram.WebApp.ready()
    telegram.WebApp.MainButton
      .setText('Ok')
      .onClick()
  }

  return (
    <div className="App">
      12
    </div>
  );
}

export default App;
