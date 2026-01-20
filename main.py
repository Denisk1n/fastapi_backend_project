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



if __name__ == "__main__":
   uvicorn.run("main:app",reload=True)