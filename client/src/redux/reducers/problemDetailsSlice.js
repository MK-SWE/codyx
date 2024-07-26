import { createSlice, createAsyncThunk, createSelector } from "@reduxjs/toolkit";

// Initial state
const initialState = {
  problem: null,
  loading: false,
  error: null,
};

// Async thunk to fetch problem details
export const fetchProblemDetails = createAsyncThunk(
  "problemDetails/fetchProblemDetails",
  async (problemId, { rejectWithValue }) => {
    try {
      const response = await fetch(`http://localhost:5000/challenges/${problemId}`);
      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.message || "Something went wrong!");
      }
      return data;
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

// Slice
const problemDetailsSlice = createSlice({
  name: "problemDetails",
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchProblemDetails.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchProblemDetails.fulfilled, (state, action) => {
        state.problem = action.payload;
        state.loading = false;
        state.error = null;
      })
      .addCase(fetchProblemDetails.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      });
  },
});

export default problemDetailsSlice.reducer;

// Memoized selector
const selectProblemDetailsState = (state) => state.problemDetails;

export const selectProblemDetails = createSelector(
  selectProblemDetailsState,
  (problemDetails) => problemDetails
);