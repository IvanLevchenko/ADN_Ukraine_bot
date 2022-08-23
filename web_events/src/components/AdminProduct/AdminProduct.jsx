import {useEffect} from "react"
import { useNavigate } from "react-router-dom"
import {useSelector} from "react-redux"
import Button from 'react-bootstrap/Button'

export default function AdminProduct({name, description, img}) {
  const navigate = useNavigate()
  const serverURL = useSelector(state => state.server.serverURL)
  function handleEdit() {
    navigate("/edit/")
  }

  return (
    <div className="product">
      <img src={serverURL + img} alt="product" className="mt-3" />
      <div className="product__buttons my-3 d-flex justify-content-evenly">
        <Button
          className="btn-warning w-50 mx-3"
          onClick={handleEdit}
        >Edit</Button>
        <Button
          className="btn-danger w-50 mx-3"
        >Delete</Button>
      </div>
      <div className="product__info">
        <h5>{name}</h5>
        <div>{description}</div>
      </div>
    </div>
  )
}