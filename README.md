# 💰 現代化簡易記帳網頁

採用現代化後端非同步框架 FastAPI，結合 Docker 容器化技術部署 MySQL 資料庫，並透過原生 JavaScript `fetch` 實現前後端分離的非同步資料交換。

## 🛠️ 使用技術與工具
- **後端框架**: Python 3.14 + FastAPI
- **資料庫與 ORM**: MySQL 8.0 + SQLAlchemy
- **容器化技術**: Docker + Docker Compose (實作資料持久化 `volumes`)
- **前端呈現**: HTML5 / CSS3 / JavaScript (Vanilla JS Fetch API)
- **版本控制**: Git / GitHub

## 🚀 系統架構
1. **前端 (Client)**: 提供直覺的記帳表單（包含食物、服飾、家居、交通等自訂分類）與即時更新的歷史消費紀錄表格。
2. **後端 (API Server)**: 實作 RESTful API，包含 `POST /api/records` (新增記帳) 與 `GET /api/records` (查詢全部)。
3. **資料庫 (Database)**: 透過 Docker Compose 建立獨立的 MySQL 容器，確保本地開發環境乾淨。

## 📦 如何在本地端執行此專案

### 1. 啟動資料庫 (Docker)
確保電腦已安裝並啟動 Docker Desktop，在根目錄執行：
```bash
docker-compose up -d
pip install -r requirements.txt
python -m uvicorn main:app --reload
http://127.0.0.1:8000