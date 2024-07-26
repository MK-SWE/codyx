import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

const initialState = { 
  problemList: [],
  loading: false,
  error: null
};

export const fetchProblems = createAsyncThunk(
  'problems/fetchProblems', 
  async () => {
    try {
      const response = await fetch('http://localhost:5000/challenges', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
      });
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.message || 'Failed to fetch problems');
      }
      return await response.json();
    } catch (error) {
      console.log("errrr");
      console.error('Error fetching problems:', error); 
      throw error;
    }
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