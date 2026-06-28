from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. 設定資料庫連線字串 (URL)
# 格式：mysql+pymysql://帳號:密碼@主機位置:連接埠/資料庫名稱
DATABASE_URL = "mysql+pymysql://root:rootpassword@127.0.0.1:3306/accounting_db"

# 2. 建立資料庫引擎
engine = create_engine(DATABASE_URL)

# 3. 建立一個 Session 類別，這就像是每次要跟資料庫講話時建立的「對話視窗」
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. 建立基礎類別，之後我們定義的「資料表」都會繼承它
Base = declarative_base()

# 5. 這是提供給 FastAPI 使用的工具函式，用來管理資料庫連線的開啟與關閉
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from sqlalchemy import Column, Integer, String, Float

class Record(Base):
    # 告訴資料庫，這張資料表的名字叫做 records
    __tablename__ = "records"

    # 定義欄位
    id = Column(Integer, primary_key=True, index=True, autoincrement=True) # 流水號
    item = Column(String(100), nullable=False)                            # 消費項目（例如：午餐、高鐵票）
    amount = Column(Float, nullable=False)                                # 金額
    category = Column(String(50), nullable=False)                         # 分類（例如：食、衣、住、行）