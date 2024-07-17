import { configureStore } from '@reduxjs/toolkit';
import authSlice from './redux/reducers/authSlice';
import problemSlice from './redux/reducers/problemSlice';

const store = configureStore({
  reducer: {
    user: authSlice,
    problems: problemSlice
  },
});

export default store;