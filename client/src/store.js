import { configureStore } from '@reduxjs/toolkit';
import authSlice from './redux/reducers/authSlice';
import problemSlice from './redux/reducers/problemSlice';
import problemDetailsSlice from './redux/reducers/problemDetailsSlice';

const store = configureStore({
  reducer: {
    user: authSlice,
    problems: problemSlice,
    problemDetails: problemDetailsSlice,
  },
});

export default store;