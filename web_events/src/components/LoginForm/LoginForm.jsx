import Form from "react-bootstrap/Form"
import Button from "react-bootstrap/Button"
import { loginUser } from "../../api/api"
import { useNavigate } from "react-router-dom"

export default function LoginForm() {
  const navigate = useNavigate()

  if (localStorage.getItem("token")) {
    navigate("/admin-page")
  }

  function handleLogin(e) {
    e.preventDefault()

    const formData = new FormData()
    Array.from(e.target.elements).forEach(el => {
      if (el.id) {
        formData.append(el.id, el.value)
      }
    })
    loginUser(formData).then(response => {
      if (response.data.status) {
        localStorage.setItem("token", response.data.token)
        navigate("/admin-page")
      } else {
        alert(response.data.token)
      }
    })
  }

  return (
    <Form className="mt-5 w-25" onSubmit={handleLogin}>
      <Form.Group>
        <Form.Label>Login</Form.Label>
        <Form.Control id="login" type="text" placeholder="my-login" />
      </Form.Group>
      <Form.Group className="mt-3">
        <Form.Label>Password</Form.Label>
        <Form.Control id="password" type="password" placeholder="qwerty123" />
      </Form.Group>
      <Button type="submit" className="mt-3 w-100">Login</Button>
    </Form>
  )
}