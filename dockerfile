# 使用官方 Python 映像作為基礎映像
FROM python:3.10-slim-buster

# 設定工作目錄
WORKDIR /app

# 將 requirements.txt 複製到工作目錄
COPY requirements.txt .

# 安裝 Python 依賴項
RUN pip install --no-cache-dir -r requirements.txt

# 將專案程式碼複製到工作目錄
COPY . .

# 設置環境變數 (可選)
# ENV NAME=World

# 執行 main.py
CMD ["python", "main.py"]