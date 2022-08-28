import axios from "axios"
import store from "../store/store"
import {setProductsAction} from "../store/features/slices/productSlice"

const token = localStorage.getItem("token")

const _axios = axios.create(
  {baseURL: store.getState().server.serverURL}
)

export const getProducts = async () => {
  const products = await _axios.get("/get-products", {
    headers: {
      "Content-type": "application/json"
    }
  })
  store.dispatch(setProductsAction(products.data))
}

export const getProduct = async (id) => {
  return await _axios.get("/get-product?id=" + id, {
    headers: {
      "Content-type": "application/json"
    }
  })
}

export const createProduct = async (data) => {
    return await _axios.post("/create-product", data, {
        headers: {
          "Content-type": "multipart/form-data",
          "Authorization": "Bearer " + token
        }
    })
}

export const editProduct = async (data, id) => {
    return await _axios.patch("/edit-product?id=" + id, data, {
        headers: {
          "Content-type": "multipart/form-data",
          "Authorization": "Bearer " + token
        }
    })
}

export const deleteProduct = async (id) => {
    return await _axios.delete("/delete-product?id=" + id, {
        headers: {
          "Content-type": "application/json",
          "Authorization": "Bearer " + token
        }
    })
}

export const loginUser = async (data) => {
  return await _axios.post("/login-user", data, {
      headers: {
        "Content-type": "multipart/form-data"
      }
  })
}