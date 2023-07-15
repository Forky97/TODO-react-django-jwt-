import React, { useContext } from 'react'
import '../static/css/style.css'
import { AuthContext } from '../context/AuthCont'
import Notes from './containerNotes'

function HomePage() {

    const {user,setUser} = useContext(AuthContext)




  return (
    <div className='welcome_user'>


    {user? (
        <>
     <h2>Welcome, {user.user}! here is your Notes </h2>
     <Notes />
     </>
    ) : (
      <h2> Please login or register to see your Notes </h2>

    )}
    
    </div>
  )
}

export default HomePage