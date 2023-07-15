import React, { createContext } from "react";
import { useContext } from "react";
import { AuthContext } from "../context/AuthCont";
import { Navigate } from "react-router-dom";
import Login from "./loginForm";
import { useState } from "react";
















function Register() {

    let {user,loginUser} = useContext(AuthContext)
    const [response_error,setError] = useState('')





    const Register_api_fetch = async (e) => {


        e.preventDefault();
      

        const response = await fetch('http://127.0.0.1:8000/api/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'username': e.target.username.value,
            'password': e.target.password.value,
            'repeat_password': e.target.repeat_password.value
        })
        });
    
        const data = await response.json();
    
        if (response.status === 200) 
        {

            loginUser(e)


         } 
        else {

        console.log(data['password'])
        setError(data['password'])}
    }

        

        





    
  
    return user ? (
        <Navigate to="/" />
      ) : (

        <div className="formRegister">
          <form onSubmit={Register_api_fetch}>
            <input type="text" name="username" placeholder="Enter Username" />
            <input type="password" name="password" placeholder="Enter Password" />
            <input type="password" name="repeat_password" placeholder="Repeat Password" />
            <input type="submit" value="Register" />
          </form>
          <h1>{response_error}</h1>

        </div>


      );
    }

      
    
  
  
  export default Register