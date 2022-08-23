import { createSlice } from '@reduxjs/toolkit'

export const productsSlice = createSlice({
  name: 'products',
  initialState: {
    products: [],
  },
  reducers: {
    setProductsAction(state, action) {
      state.products = action.payload
    }
  },
})

export const { setProductsAction } = productsSlice.actions

export default productsSlice.reducer