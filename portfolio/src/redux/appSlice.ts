import { createSlice } from '@reduxjs/toolkit';

const appSlice = createSlice({
  name: 'app',
  initialState: {
    torusColor: '#FF6347', // Default color
  },
  reducers: {
    setTorusColor: (state: { torusColor: any; }, action: { payload: any; }) => {
      state.torusColor = action.payload;
    },
  },
});

export const { setTorusColor } = appSlice.actions;
export default appSlice.reducer;