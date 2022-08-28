import {useState, useEffect} from "react"
import {getProducts} from "../../api/api"
import {useSelector} from "react-redux"
import AdminProduct from "../AdminProduct/AdminProduct"
import Button from "react-bootstrap/Button"

export function AdminProducts() {
  const products = useSelector(state => state.products.products)

  useEffect(() => {
    getProducts()
  }, [])

  return (
    <div className="products-wrapper .container-fluid d-flex mt-1 flex-wrap">
      {products.map(prod => <AdminProduct key={prod.id} {...prod}/>)}
    </div>
  )
}