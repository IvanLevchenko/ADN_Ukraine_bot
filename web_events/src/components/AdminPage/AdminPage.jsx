import 'bootstrap/dist/css/bootstrap.min.css'
import { useEffect } from 'react'
import Tab from 'react-bootstrap/Tab'
import Tabs from 'react-bootstrap/Tabs'
import {default as Form} from '../AdminForm/AdminForm'
import {AdminProducts} from '../AdminProducts/AdminProducts'
import { useNavigate } from "react-router-dom"

export default function AdminPage() {
  const navigate = useNavigate()

  return (
    <div className="container mt-5">
      <Tabs defaultActiveKey="products">
        <Tab eventKey="products" title="Products">
          <AdminProducts />
        </Tab>
        <Tab className="d-flex justify-content-center" eventKey="form" title="Form">
          <Form />
        </Tab>
      </Tabs>
    </div>
  )
}