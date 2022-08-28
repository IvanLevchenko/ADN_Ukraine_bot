import { useEffect } from "react"
import { useNavigate } from "react-router-dom"

export default function AdminRoute({Component}) {
  const navigate = useNavigate()
  const hasToken = !!localStorage.getItem("token")

  useEffect(() => {
    if (!hasToken) {
      navigate("/admin")
    }
  }, [])

  return (
    <>
      {hasToken ? <Component /> : <></>}
    </>
  )
}