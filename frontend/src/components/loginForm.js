import React, { useContext } from 'react'
import { AuthContext } from '../context/AuthCont'
import { Navigate } from 'react-router-dom';


function Login() {

  let {loginUser, user} = useContext(AuthContext)

  return user ? (
    <Navigate to="/" />
  ) : (
    <div className="formLogin">
      <form onSubmit={loginUser}>
        <input type="text" name="username" placeholder="Enter Username" />
        <input type="password" name="password" placeholder="Enter Password" />
        <input type="submit" value="Log In" />
      </form>
    </div>
  );
}
    
  


export default Login

