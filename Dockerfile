# 使用官方 Python 基礎映像
FROM python:3.9-slim

# 安裝系統依賴
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libmariadb-dev-compat \
    libmariadb-dev \
    pkg-config

# 設定工作目錄
WORKDIR /app

# 複製需求文件
COPY requirements.txt .

# 安裝 Python 依賴
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式檔案
COPY . .

# 設定環境變數
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0

# 暴露埠
EXPOSE 5000

# 啟動應用程式
CMD ["flask", "run"]
