import { createSlice } from '@reduxjs/toolkit'

export const serverSlice = createSlice({
  name: 'server',
  initialState: {
    serverURL: "http://localhost:3001/api/v1/",
    // serverURL: "https://effortless-kitsune-c04cd7.netlify.app/api/v1"
  },
  reducers: {},
})

export const {} = serverSlice.actions

export default serverSlice.reducer