import { configureStore } from '@reduxjs/toolkit';
import authSlice from './redux/reducers/authSlice';
import problemSlice from './redux/reducers/problemSlice';
import problemDetailsSlice from './redux/reducers/problemDetailsSlice';
import submitSlice from './redux/reducers/submitSlice';

const store = configureStore({
  reducer: {
    user: authSlice,
    problems: problemSlice,
    problemDetails: problemDetailsSlice,
    submitDetails: submitSlice
  },
});

export default store;