import {useEffect, useState, useRef} from "react"
import Form from "react-bootstrap/Form"
import Button from "react-bootstrap/Button"
import {useParams, useNavigate} from "react-router-dom"
import {useSelector} from "react-redux"
import { createProduct, getProduct, editProduct, getProducts } from "../../api/api"

export default function AdminForm() {
  const serverURL = useSelector(state => state.server.serverURL)
  const navigate = useNavigate()
  const params = useParams()
  const form = useRef()
  const previewImage = useRef()
  const [isEditMode] = useState(!!params.id)

  const fillForm = (product) => {
    Array.from(form.current.elements).forEach(field => {
      if (field.id !== "image" && field.id) {
        field.value = product[field.id]
      }
    })
    previewImage.current.src = serverURL + product.image
  }

  const handleImageChange = (e) => {
    if (isEditMode) {
      previewImage.current.src = URL.createObjectURL(e.target.files[0])
    } else {
      return
    }
  }

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

    if (isEditMode) {
      editProduct(formData, params.id).then(response => alert(response.data.status))
      navigate("/admin-page")
    } else {
      createProduct(formData).then(response => alert(response.data.status))
    }
    getProducts()
    e.target.reset()
    // window.location.reload()
  }

  useEffect(() => {
    if (isEditMode) {
      getProduct(params.id).then(response => fillForm(response.data))
    }
  }, [])

  return (
    <Form className="w-50 mt-5 m-auto" ref={form} onSubmit={handleSubmit} >
      <Form.Group className="mb-3" controlId="name">
        <Form.Control
          required={isEditMode ? false : true}
          className="mb-3"
          type="text"
          placeholder="Product name..."
        />
      </Form.Group>
      <Form.Group controlId="description">
        <Form.Control
           required={isEditMode ? false : true}
           className="mb-3"
           as="textarea"
           placeholder="About your product..."
        />
      </Form.Group>
      <Form.Group controlId="image">
        <Form.Control
           required={isEditMode ? false : true}
           className="mb-3"
           max={1}
           type="file"
           onChange={handleImageChange}
        />
      {
        isEditMode
        ? <img src="" ref={previewImage} id="preview-edit-image" className="border my-3 w-50" />
        : <></>
      }
      </Form.Group>
      <Button variant="primary" type="submit">
        {isEditMode ? "Edit" : "Create"}
      </Button>
    </Form>
  )
}