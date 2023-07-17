import React, { useContext } from "react";
import { createContext, useState, } from "react";
import jwt_decode from "jwt-decode";
import { useNavigate } from 'react-router-dom';
import { useEffect } from "react";
import { AuthContext } from "./AuthCont";




export const NoteContext = createContext()







const NoteProvider =  ({children}) => {

    let [editedText, setEditedText] = useState('');
    let [editing, setEditing] = useState(false);
    let [noteId, setNoteId] = useState();
    let {authTokens,setAuthTokens}= useContext(AuthContext)
    let [checkFlag,setCheckFlag] = useState(0)


   const handleEdit = (note) => {
        setEditing(true);
        setNoteId(note.id)

        };


  const handleCancel = () => {
    setEditing(false);
  };


  const handleSave = () => {
    updateNote(noteId,editedText)
    setEditing(false);
  };


  const updateNote = async (noteId,editedText) => {

    let response = await fetch('http://127.0.0.1:8000/api/notes/update/'+noteId+'/', {
            method:'PATCH',
            headers:{
                'Content-Type':'application/json',
                'Authorization':'Bearer ' + String(authTokens.access)
            },
            body:JSON.stringify({'body':editedText,
                                })
        })

    let data = await response.json()

    setEditedText('')

    

  }


  const updateCheckNote = async (noteId,check) => {

    let response = await fetch('http://127.0.0.1:8000/api/notes/update/'+noteId+'/', {
            method:'PATCH',
            headers:{
                'Content-Type':'application/json',
                'Authorization':'Bearer ' + String(authTokens.access)
            },
            body:JSON.stringify({'done':check,
                                })
        })

    let data = await response.json()

    setCheckFlag(checkFlag+1)




  }



   let note_functions = {handleEdit : handleEdit,
          handleCancel : handleCancel,
          handleSave : handleSave,
          updateNote:updateNote,
          editing:editing,
          setEditing:setEditing,
          editedText:editedText,
          setEditedText:setEditedText,
          updateCheckNote:updateCheckNote,
          checkFlag:checkFlag,
          setCheckFlag:setCheckFlag

        }




          return (

            <NoteContext.Provider value={note_functions}>
                {children}
            </NoteContext.Provider>
    
    
        )
  



}

export default NoteProvider
