import "./Card.scss"
import {useSelector} from "react-redux"

export default function Card({name, description, img}) {
  const serverURL = useSelector(state => state.server.serverURL)

  return (
    <div className="card">
      <img alt="product" src={serverURL + img} />
      <h2>{name}</h2>
      <div>{description}</div>
    </div>
  )
}