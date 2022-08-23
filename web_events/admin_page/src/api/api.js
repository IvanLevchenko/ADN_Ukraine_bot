import axios from "axios"

export const baseURL = "http://localhost:3001/api/v1/"
const _axios = axios.create({baseURL})

export const getProducts = async () => {
    return await _axios.get("/get-products", {
        headers: {
          "Content-type": "application/json"
        }
    })
}

export const createProduct = async (data) => {
    return await _axios.post("/create-product", data, {
        headers: {
          "Content-type": "multipart/form-data"
        }
    })
}