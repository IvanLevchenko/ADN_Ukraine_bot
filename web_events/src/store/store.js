import { configureStore } from '@reduxjs/toolkit'
import productsSlice from './features/slices/productSlice'
import serverSlice from './features/slices/serverSlice'

export default configureStore({
  reducer: {
    products: productsSlice,
    server: serverSlice
  },
})