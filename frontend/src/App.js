import React from 'react';
import Header from './block/Header';
import HomePage from './components/HomePage';
import Notes from './components/containerNotes';
import { BrowserRouter, Routes, Route, Outlet } from 'react-router-dom';
import Login from './components/loginForm';
import AuthProvider from './context/AuthCont';
import Register from './components/registerForm';
import NoteProvider from './context/NoteContext';


 




function App() {
  return (

    <div className='BaseDiv'>

      <BrowserRouter>
    
    <AuthProvider>
      <NoteProvider>




      <Header/> 

           <Routes>
            <Route path="/login" element={<Login/>} /> 
            <Route exact path="/" element={<HomePage/>}/>
            <Route path="/register" element={<Register/>}/>

          </Routes>


  


          </NoteProvider>
    </AuthProvider>

    </BrowserRouter>

  
    



    </div>

  );
}

export default App;