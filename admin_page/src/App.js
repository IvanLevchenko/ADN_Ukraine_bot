import './App.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import Tabs from 'react-bootstrap/Tabs'
import Tab from 'react-bootstrap/Tab'
import {default as Form} from './components/CreateForm/CreateForm'
import Products from './components/Products/Products'

function App() {
  return (
    <div className="App">
      <div className="container mt-5">
        <Tabs defaultActiveKey="goods">
          <Tab eventKey="goods" title="Goods">
            <Products />
          </Tab>
          <Tab className="d-flex justify-content-center" eventKey="form" title="Form">
            <Form />
          </Tab>
        </Tabs>
      </div>
    </div>
  );
}

export default App
