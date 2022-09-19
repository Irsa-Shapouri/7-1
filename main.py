from typing import Optional
from fastapi import FastAPI, status, Depends
from pydantic import BaseModel
from fastapi.exceptions import HTTPException
import pandas as pd
from sqlalchemy.orm import Session
import models, schemas, crud, exceptions
from databse import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
        db = SessionLocal()
        try:
                yield db
        finally:
                db.close()




# class login(BaseModel):
#     username: str
#     password: str

# users_df = pd.read_csv("./database/users.csv")

# @app.post("/login")
# async def login_user(req: login):

#     if users_df.loc[users_df["user_name"] == req.username]["user_password"].tolist() == [req.password]:
#             raise HTTPException(status.HTTP_200_OK, detail= "Successful login")
#     else:
#             raise HTTPException(status.HTTP_404_NOT_FOUND, detail= "username or password incorrect")

@app.post("/category/")
async def create_category(req: schemas.create_category, db: Session = Depends(get_db)):
        try:
                newcat = crud.create_category(db, category = req)
                return newcat
        except exceptions.ExceptionHandler as e:
                 raise HTTPException(status.HTTP_404_NOT_FOUND, detail= f"{e}")


@app.get("/category/")
async def get_all_category(db: Session = Depends(get_db)):
        return crud.get_all_category(db)


