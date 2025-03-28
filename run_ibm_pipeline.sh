#!/bin/bash
set -e

echo "🔧 [1/4] 產生量子電路 QASM..."
python generate_qasm.py --qubits 5 --output for_ibm.qasm

echo "🚀 [2/4] 使用 Runtime 提交至 IBM Quantum..."
python submit_ibm_job_runtime.py for_ibm.qasm

JOB_ID=$(cat job_id.txt)
echo "⏳ [3/4] 等待後端執行完成 (Job ID: $JOB_ID)..."
sleep 30  # 避免 job 還沒完成就拉結果

echo "📥 [4/4] 拉取測量結果並進行分析"
python fetch_result_runtime.py "$JOB_ID"
python auto_decision.py

echo "✅ 完整流程執行完畢"
