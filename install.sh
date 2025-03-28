#!/bin/bash
set -e

echo "📦 建立虛擬環境 .venv"
python3 -m venv .venv
source .venv/bin/activate

echo "⬇️ 安裝套件..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ 安裝完成！使用方法："
echo "source .venv/bin/activate"
