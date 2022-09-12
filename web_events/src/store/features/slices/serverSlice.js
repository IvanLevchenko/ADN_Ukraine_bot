import { createSlice } from '@reduxjs/toolkit'

export const serverSlice = createSlice({
  name: 'server',
  initialState: {
    serverURL: "https://webevents.ddns.net/api/v1",
    // serverURL: "http://localhost:5000/api/v1"
  },
  reducers: {},
})

export const {} = serverSlice.actions

export default serverSlice.reducer