import {useState, useEffect} from "react"
import {getProducts} from "../../api/api"

export default function Goods() {

  const [products, setProducts] = useState()

  useEffect(() => {
    getProducts().then(response => setProducts(response))
  }, [])

  return (
    <></>
  )
}