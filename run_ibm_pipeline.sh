#!/bin/bash
set -e

echo "準備環境與 Token..."
export IBMQ_TOKEN="${IBMQ_TOKEN:-$(cat .ibm_token)}"

echo "🤖 產生 QASM"
python generate_qasm.py --qubits 5 --samples 10 --output for_ibm.qasm

echo "🚀 提交至 IBM Runtime"
python submit_ibm_job_runtime.py for_ibm.qasm

echo "⏳ 等待 1分鐘 ..."
sleep 60

echo "📥 取得結果"
JOB_ID=$(cat job_id.txt)
python fetch_result_runtime.py "$JOB_ID"

echo "⏳ 等待 30分鐘 以獲得完整結果 ..."
sleep 180

echo "📊 分析結果"
python auto_decision.py > summary.txt
