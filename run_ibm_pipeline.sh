#!/bin/bash

set -e

echo "🔧 [1/4] 產生量子電路 QASM..."
python generate_qasm.py --qubits 5 --output for_ibm.qasm

echo "🚀 [2/4] 提交至 IBM Quantum..."
python submit_ibm_job.py for_ibm.qasm

JOB_ID=$(cat job_id.txt)
echo "📦 [3/4] 等待並拉取結果 (Job ID: $JOB_ID)..."
sleep 20  # 等待 IBM 系統處理

python fetch_result.py "$JOB_ID"

echo "🧠 [4/4] 分析 qubit[0] 結果..."
python auto_decision.py

echo "✅ 全流程執行完畢"
