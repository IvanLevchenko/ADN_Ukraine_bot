import {useEffect, useState, useRef} from "react"
import Form from "react-bootstrap/Form"
import Button from "react-bootstrap/Button"
import {useParams} from "react-router-dom"
import { createProduct, getProduct } from "../../api/api"

export default function AdminForm() {

  const handleSubmit = (e) => {
    e.preventDefault()
    const formData = new FormData()

    Array.from(e.target.elements).forEach(element => {
      if (!element.id) return
      if (element.id === "image") {
        formData.append(element.id, element.files[0])
      } else {
        formData.append(element.id, element.value)
      }
    })
    createProduct(formData).then(response => alert(response.data.status))
    e.target.reset()
  }
  const params = useParams()
  const form = useRef()
  const [isEditMode] = useState(!!params.id)

  const fillForm = (product) => {
    Array.from(form.current.elements).forEach(field => {
        console.log(field)
      if (field.id !== "image" && field.id) {
        field.value = product[field.id]
      }
    })
  }

  useEffect(() => {
    if (isEditMode) {
      getProduct(params.id).then(response => fillForm(response.data))
    }
  }, [])

  return (
    <Form className="w-50 mt-5 m-auto" onSubmit={handleSubmit} ref={form}>
      <Form.Group className="mb-3" controlId="name">
        <Form.Control
          required
          className="mb-3"
          type="text"
          placeholder="Product name..."
        />
      </Form.Group>
      <Form.Group controlId="description">
        <Form.Control
           required
           className="mb-3"
           as="textarea"
           placeholder="About your product..."
        />
      </Form.Group>
      <Form.Group controlId="image">
        <Form.Control
           required
           className="mb-3"
           max={1}
           type="file"
        />
      {isEditMode ? <img src="" id="preview-edit-image" /> : <></>}
      </Form.Group>
      <Button variant="primary" type="submit">
        Create
      </Button>
    </Form>
  )
}