import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

const initialState = { 
  user: null,
  token: null,
  isAuthenticated: false,
  loading: false,
  error: null,
};

export const login = createAsyncThunk(
  "auth/login",
  async (userData, { rejectWithValue }) => {
    try {
      const response = await fetch("http://localhost:5000/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams(userData).toString(),
        credentials: 'include'
      });
      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.message || "Something went wrong!");
      }
      const Header = response.headers;
      console.log(Header);

      if (response.headers.has('session_id')) {
        const sessionId = response.headers.get('session_id');
        console.log('Session ID:', sessionId);

        document.cookie = `session_id=${sessionId}; path=/;`;
      }
      console.log(data);
      return data;
    } catch (error) {
      return rejectWithValue(error);
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
      console.log(data);
      return data;
    } catch (error) {
      return rejectWithValue(error);
    }
  }
);



const authSlice = createSlice({
  name: "auth",
  initialState,
  reducers: {
    logout(state) {
      state.user = null;
      state.token = null;
      state.isAuthenticated = false;
      state.error = null; // Clear the error field
      localStorage.clear();
    },
    addToken(state) {
      state.token = localStorage.getItem("token");
    },
    addUser(state) {
      state.user = JSON.parse(localStorage.getItem("user"));
    }

  },
  extraReducers: (builder) => {
    builder
      .addCase(login.pending, (state) => {
        state.loading = true;
      })
      .addCase(login.fulfilled, (state, action) => {
        state.user = action.payload.user;
        state.token = action.payload.token;
        state.isAuthenticated = true;
        state.loading = false;

        localStorage.setItem("user", JSON.stringify(action.payload.user));
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
      });
  }
});

export const authActions = authSlice.actions;

export default authSlice.reducer;

