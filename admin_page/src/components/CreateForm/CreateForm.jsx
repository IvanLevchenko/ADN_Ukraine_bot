import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'

export default function CreateForm() {

  const handleSubmit = (e) => {
    e.preventDefault()
    const formData = new FormData()
  }

  return (
    <Form className="w-50 mt-5" onSubmit={handleSubmit}>
      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Control className="mb-3" type="text" placeholder="Product name..." />
        <Form.Control className="mb-3" as="textarea" placeholder="About your product..." />
      </Form.Group>
      <Form.Group>
        <Form.Control className="mb-3" max={1} type="file" />
      </Form.Group>
      <Button variant="primary" type="submit">
        Create
      </Button>
    </Form>
  )
}