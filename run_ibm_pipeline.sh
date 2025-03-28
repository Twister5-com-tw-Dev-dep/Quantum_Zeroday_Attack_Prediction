#!/bin/bash
set -e

echo "🔧 [1/4] 產生訓練後的 QASM 電路..."
python generate_qasm.py --qubits 5 --samples 10 --output for_ibm.qasm

echo "🚀 [2/4] 使用 Runtime 提交至 IBM Quantum..."
python submit_ibm_job_runtime.py for_ibm.qasm

JOB_ID=$(cat job_id.txt)
echo "⏳ [3/4] 等待後端執行完成 (Job ID: $JOB_ID)..."
sleep 30

echo "📥 [4/4] 拉取測量結果並進行分析"
python fetch_result_runtime.py "$JOB_ID"
python auto_decision.py

echo "✅ 流程完成！"
