import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

const initialState = { 
  data: {},
  loading: false,
  error: null
};

export const submitProblem = createAsyncThunk(
  'problems/submitProblem', 
  async (data) => {
    const response = await fetch('http://localhost:5000/submit', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data),
      credentials: 'include',
    }
    );
    if (!response.ok) {
      throw new Error('Failed to fetch problems');
    }
    return await response.json();
  }
);

const submitSlice = createSlice({
  name: 'submit',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(submitProblem.pending, (state) => {
        state.loading = 'pending';
        state.error = null;
      })
      .addCase(submitProblem.fulfilled, (state, action) => {
        state.loading = 'fulfilled';
        state.data = action.payload;
      })
      .addCase(submitProblem.rejected, (state, action) => {
        state.loading = 'rejected';
        state.error = action.error.message || 'Failed to submit the code';
      });
  },
});

export default submitSlice.reducer;
