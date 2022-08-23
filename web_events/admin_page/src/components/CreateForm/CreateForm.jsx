import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'

import { createProduct } from '../../api/api'

export default function CreateForm() {

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
    createProduct(formData)
  }

  return (
    <Form className="w-50 mt-5 m-auto" onSubmit={handleSubmit}>
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
      </Form.Group>
      <Button variant="primary" type="submit">
        Create
      </Button>
    </Form>
  )
}