import React, { useContext } from 'react'
import '../static/css/style.css'
import { useState,useEffect } from 'react';
import { AuthContext } from '../context/AuthCont';
import { NoteContext } from '../context/NoteContext';









function Notes() {

    const [noteText, setNoteText] = useState('')

    const {user,authTokens,logoutUser} = useContext(AuthContext)
    let {handleEdit,handleSave,handleCancel,updateNote,updateCheckNote,checkFlag} = useContext(NoteContext)

    let {editing,setEditing,editedText,setEditedText} = useContext(NoteContext)
    
    let [notes, setNotes] = useState([])









    const AddNote = async () => {

      let response = await fetch('http://127.0.0.1:8000/api/notes/create/', {
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify({'body':noteText,
                                 'user':user
          })
        })

        let data = await response.json
        getNotes()

      


    };


    const getNotes = async () =>{
        let response = await fetch('http://127.0.0.1:8000/api/notes/', {
            method:'GET',
            headers:{
                'Content-Type':'application/json',
                'Authorization':'Bearer ' + String(authTokens.access)
            }
        })
        let data = await response.json()

        if(response.status === 200){
            setNotes(data)
        }else if(response.statusText === 'Unauthorized'){
            logoutUser()
        }
        
}


    useEffect(() => {
      getNotes();
    },[checkFlag,editedText]);




    const deleteNote = async (noteId) => {

      let response = await fetch('http://127.0.0.1:8000/api/notes/delete/'+ noteId + '/', {
            method:'Delete',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                                 'user':user
          })
        })

        if (response.status == 200) {
          let data = await response.json
          getNotes()

        }
        else {
        console.log('error')
      }


    }
















    return (
        <div className='todo-container'>



          <div className='notes-container'>

          <ul className='note-list'>
                {notes.map(note => (
                    <li className='note-item' key={note.id} >{note.body}
                          {editing ? (
          <>
             <button  className='cancel-note' onClick={ () => handleCancel()}> Отмена</button>

          </>
        ) : (
          <>
            <input
              type='checkbox'
              checked={note.done}
              onChange={(e) => updateCheckNote(note.id, e.target.checked)} // Предположим, что поле с именем "isCompleted" обозначает статус выполнения} // Обработчик изменения состояния чекбокса
            />
            <button  className='delete-note' onClick={ () => deleteNote(note.id)}> Удалить</button>
            <button  className='change-note' onClick={ () => handleEdit(note)}> Редактировать</button>

          </>
        )}
</li>
                ))}
            </ul>

          
          </div>






          <div className='input_note'>

            {editing ? (
              <>
               <input
              type='text'
              value={editedText}
              onChange={(e) => setEditedText(e.target.value)}
              placeholder='Введите свои изменения'
            />

            <button onClick={handleSave} > Сохранить изменения!</button>
              
              </>
            )

            : (
              <>
              <input
              type='text'
              value={noteText}
              onChange={(e) => setNoteText(e.target.value)}
              placeholder='Введите текст записи...'
            />

            
              <button onClick={AddNote}>Добавить запись!</button>

              </>
            )}

         </div>


          
            </div>
      );
}

export default Notes