import React from 'react';
import '../static/css/style.css'
import enter_image from '../static/images/enter_image.png'
import exit_image from '../static/images/exit_image.jpeg'
import register_image from '../static/images/register_image.png'

import { useContext } from 'react';
import { Link } from 'react-router-dom';
import {AuthContext}from '../context/AuthCont';




function Header() {

  let { user,setUser,logoutUser } = useContext(AuthContext);






    
  return (
    <header className="header">


      <h1>TO-DO</h1>

        {user ? (
                <>
                  <img src={exit_image} onClick={logoutUser} alt='exit'/>
                </>
              ) : (
                <>
                <Link to="/login">
                  <img className='login_user' src={enter_image} alt='login'/>
                  </Link>

                  <Link to="/register">
                  <img className='register_user' src={register_image} alt='register'/>

                  </Link>


                </>
              )}
    </header>
  );
}

export default Header;
