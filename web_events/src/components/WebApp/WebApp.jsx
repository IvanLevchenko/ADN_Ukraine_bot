import Card from "../Card/Card"
import {useSelector} from "react-redux"

export default function WebbApp() {
  const productsSelector = useSelector(state => state.products.products)

  return (
    <div>
      {productsSelector.map(prod => <Card key={prod.name} {...prod} />)}
    </div>
  )
}