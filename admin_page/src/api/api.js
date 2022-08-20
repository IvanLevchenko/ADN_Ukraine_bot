import axios from "axios"

const _axios = axios.create({baseURL: "http://localhost:3001/api/v1/"})

export const getProducts = async () => {
    return await _axios.get("/get-products", {
        headers: {
          "Content-type": "application/json"
        }
    })
}

export const createProducts = async (data) => {
    return await _axios.post("/create-product", data, {
        headers: {
          "Content-type": "multipart/form-data"
        }
    })
}