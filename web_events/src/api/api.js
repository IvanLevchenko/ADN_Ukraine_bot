import axios from "axios"
import store from "../store/store"
import {setProductsAction} from "../store/features/slices/productSlice"

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

export const createProduct = async (data) => {
    return await _axios.post("/create-product", data, {
        headers: {
          "Content-type": "multipart/form-data"
        }
    })
}