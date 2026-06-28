from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from pydantic import BaseModel
import database

app = FastAPI()

# 設定 HTML 模板資料夾的位置（指向專案內部的 templates 資料夾）
templates = Jinja2Templates(directory="templates")

# 自動建表
database.Base.metadata.create_all(bind=database.engine)

class RecordCreate(BaseModel):
    item: str
    amount: float
    category: str

# 【新加入】當使用者瀏覽網頁首頁時，把 index.html 畫面渲染並顯示出來
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 新增 API
@app.post("/api/records")
def create_record(record_data: RecordCreate, db: Session = Depends(database.get_db)):
    new_record = database.Record(
        item=record_data.item,
        amount=record_data.amount,
        category=record_data.category
    )
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return {"status": "success", "data": new_record}

# 查詢 API
@app.get("/api/records")
def get_all_records(db: Session = Depends(database.get_db)):
    return db.query(database.Record).all()