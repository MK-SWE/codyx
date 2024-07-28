import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from 'axios';

const initialState = { 
  user: null,
  isAuthenticated: false,
  loading: false,
  error: null,
};

export const login = createAsyncThunk(
  "auth/login",
  async (userData, { rejectWithValue }) => {
    try {
      const response = await axios.post(
        "http://localhost:5000/login",
        new URLSearchParams(userData).toString(),
        {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
          withCredentials: true,
        }
      );

      const data = response.data;

      if (response.status !== 200) {
        throw new Error(data.message || "Something went wrong!");
      }
      return data;
    } catch (error) {
      return rejectWithValue(error.response ? error.response.data : error.message);
    }
  }
);

export const register = createAsyncThunk(
  "auth/signup",
  async (userData, { rejectWithValue }) => {
    try {
      const response = await fetch("http://localhost:5000/signup", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams(userData).toString(),
      });
      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.message || "Something went wrong!");
      }
      return data;
    } catch (error) {
      return rejectWithValue(error);
    }
  }
);
export const logout = createAsyncThunk(
  "auth/logout",
  async (_, { rejectWithValue }) => {
    try {
      const response = await axios.get("http://localhost:5000/logout", {
        withCredentials: true,
      });
      if (response.status !== 200) {
        throw new Error("Logout failed!");
      }
      return response.data;
    } catch (error) {
      return rejectWithValue(error.response ? error.response.data : error.message);
    }
  }
);


const authSlice = createSlice({
  name: "auth",
  initialState,
  reducers: {
    loginSuccess(state, action) {
      state.user = action.payload.user;
      state.isAuthenticated = true;
    },
    logoutSuccess(state) {
      state.user = null;
      state.isAuthenticated = false;
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(login.pending, (state) => {
        state.loading = true;
      })
      .addCase(login.fulfilled, (state, action) => {
        state.user = action.payload.user;
        state.isAuthenticated = true;
        state.loading = false;
        localStorage.setItem('user', JSON.stringify(state.user));
      })
      .addCase(login.rejected, (state, action) => {
        state.error = action.payload.message;
        state.loading = false;
      })
      .addCase(register.pending, (state) => {
        state.loading = true;
      })
      .addCase(register.fulfilled, (state, action) => {
        state.user = action.payload.full_name;
        state.loading = false;
      })
      .addCase(register.rejected, (state, action) => {
        state.error = action.payload.message;
        state.loading = false;
      })
      .addCase(logout.pending, (state) => {
        state.loading = true;
      })
      .addCase(logout.fulfilled, (state) => {
        state.user = null;
        state.isAuthenticated = false;
        state.loading = false;
        localStorage.removeItem('user');
      })
      .addCase(logout.rejected, (state, action) => {
        state.error = action.payload.message;
        state.loading = false;
      });
  }
});

export const authActions = authSlice.actions;

export default authSlice.reducer;

