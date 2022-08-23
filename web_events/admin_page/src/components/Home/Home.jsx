import 'bootstrap/dist/css/bootstrap.min.css'
import Tabs from 'react-bootstrap/Tabs'
import Tab from 'react-bootstrap/Tab'
import {default as Form} from '../CreateForm/CreateForm'
import Products from '../Products/Products'

export default function Home() {
  return (
    <div className="container mt-5">
      <Tabs defaultActiveKey="products">
        <Tab eventKey="products" title="Products">
          <Products />
        </Tab>
        <Tab className="d-flex justify-content-center" eventKey="form" title="Form">
          <Form />
        </Tab>
      </Tabs>
    </div>
  )
}