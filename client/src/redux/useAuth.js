import { useDispatch } from "react-redux";
import { authActions } from "./reducers/authSlice";
import { useEffect } from "react";

const useAuth = () => {
  const dispatch = useDispatch();

  useEffect(() => {
    const safeParseJSON = (str) => {
      try {
        return JSON.parse(str);
      } catch (error) {
        return null;
      }
    };

    const userJson = localStorage.getItem('user');
    const user = safeParseJSON(userJson);
    
    if (user) {
      dispatch(authActions.loginSuccess({ user }));
    }
  }, [dispatch]);
};

export default useAuth;
