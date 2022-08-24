import {useState, useEffect} from "react"
import {getProducts} from "../../api/api"
import {useSelector} from "react-redux"
import AdminProduct from "../AdminProduct/AdminProduct"

export default function AdminProducts() {
  const products = useSelector(state => state.products.products)

  return (
    <div className="products-wrapper .container-fluid d-flex justify-content-around mt-1">
      {products.map(prod => <AdminProduct key={prod.id} {...prod}/>)}
    </div>
  )
}