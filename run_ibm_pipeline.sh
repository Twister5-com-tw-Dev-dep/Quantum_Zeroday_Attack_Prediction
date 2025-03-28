#!/bin/bash
set -euo pipefail

echo "🚀 啟動 IBM Runtime 自動流程"
echo "📅 時間：$(date)"

# 設定 Token：優先用環境變數，否則從本地檔案讀取
export IBMQ_TOKEN="${IBMQ_TOKEN:-$(cat .ibm_token 2>/dev/null)}"
if [ -z "$IBMQ_TOKEN" ]; then
    echo "❌ 無法取得 IBMQ_TOKEN，請設定環境變數或 .ibm_token 檔案"
    exit 1
fi

# 產生 QASM 電路
echo "🤖 產生 QASM（使用 ML 訓練參數）"
python generate_qasm.py --qubits 5 --samples 10 --output for_ibm.qasm

# 提交到 IBM Runtime
echo "🚀 提交至 IBM Quantum Runtime（請等待隊列中...）"
python submit_ibm_job_runtime.py for_ibm.qasm

# 等待 queue 排隊
echo "⏳ 等待 1 分鐘進入佇列 ..."
sleep 60

JOB_ID=$(cat job_id.txt)
echo "📨 取得 Job ID：$JOB_ID"

# 等待運行完成（IBM Quantum 通常要排 30-60 分鐘）
echo "⏳ 等待 30 分鐘以獲得完整結果 ..."
sleep 1800

# 擷取結果
echo "📥 抓取測量結果"
python fetch_result_runtime.py "$JOB_ID"

# 執行自動決策邏輯
echo "📊 分析結果並生成報表"
python auto_decision.py > summary.txt

echo "✅ 完整流程結束！時間：$(date)"
