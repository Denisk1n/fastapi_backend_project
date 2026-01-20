from fastapi import FastAPI
import uvicorn
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
   CORSMiddleware,
   allow_origins=["*"]
)

notes = [
   {
      "id": 1, 
      "title": 'Вообще топ',
      "content": 'Это крутая заметка !!'
   },
   {
      "id": 2, 
      "title": 'Вторая, но не по значимости',
      "content": 'Эта заметка не очень !'
   }
]


@app.get("/notes", summary="Пробуем отдать записи на frontend")
def get_all_notes():
   return notes

@app.get("/notes/{note_id}")
def get_note(note_id: int):
   for note in notes:
      if note["id"] == note_id:
         return note
   return {"error": "Note not found"}



if __name__ == "__main__":
   uvicorn.run("main:app",reload=True)