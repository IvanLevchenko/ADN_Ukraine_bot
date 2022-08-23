import {useState, useEffect} from "react"
import {getProducts} from "../../api/api"
import Product from "../AdminProduct/AdminProduct"

export default function AdminProducts() {

  const [products, setProducts] = useState([])

  useEffect(() => {
    getProducts().then(response => setProducts(response.data))
  }, [])

  return (
    <div className="products-wrapper .container-fluid border mt-1 w-25">
      {products.map(prod => <Product key={prod.name} {...prod}/>)}
    </div>
  )
}