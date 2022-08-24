import {useEffect, useState} from "react"
import { useNavigate } from "react-router-dom"
import {useSelector} from "react-redux"
import Button from 'react-bootstrap/Button'
import {getProduct, deleteProduct} from "../../api/api"

export default function AdminProduct({id, name, description, img}) {
  const navigate = useNavigate()
  const serverURL = useSelector(state => state.server.serverURL)
  const [product, setProduct] = useState()

  function handleEdit() {
      navigate("/edit/product/" + id)
  }

  function handleDelete() {
    deleteProduct(id)
  }

  return (
    <div className="product border p-3">
      <img src={serverURL + img} alt="product" className="mt-3" />
      <div className="product__buttons my-3 d-flex justify-content-evenly">
        <Button
          className="btn-warning w-50 mx-3"
          onClick={handleEdit}
        >Edit</Button>
        <Button
          className="btn-danger w-50 mx-3"
          onClick={handleDelete}
        >Delete</Button>
      </div>
      <div className="product__info">
        <h5>{name}</h5>
        <div>{description}</div>
      </div>
    </div>
  )
}