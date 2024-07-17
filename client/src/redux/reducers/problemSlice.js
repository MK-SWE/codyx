import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

const initialState = { 
  problemList: [],
  loading: 'idle',
  error: null
};

export const fetchProblems = createAsyncThunk(
  'problems/fetchProblems', 
  async () => {
    const response = await fetch('http://localhost:5000/api/problems');
    if (!response.ok) {
      throw new Error('Failed to fetch problems');
    }
    return await response.json();
  }
);

const problemsSlice = createSlice({
  name: 'problems',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchProblems.pending, (state) => {
        state.loading = 'pending';
        state.error = null;
      })
      .addCase(fetchProblems.fulfilled, (state, action) => {
        state.loading = 'fulfilled';
        state.problemList = action.payload;
      })
      .addCase(fetchProblems.rejected, (state, action) => {
        state.loading = 'rejected';
        state.error = action.error.message || 'Failed to fetch problems';
      });
  },
});

export default problemsSlice.reducer;
