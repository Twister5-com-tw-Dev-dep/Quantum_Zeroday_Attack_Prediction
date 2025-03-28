#!/bin/bash

set -e

echo "🔧 準備環境與 Token..."
export IBMQ_TOKEN="${IBMQ_TOKEN:-YOUR_DEFAULT_TOKEN_HERE}"  # 可覆蓋
if [ -z "$IBMQ_TOKEN" ]; then
  echo "❌ 未設置 IBMQ_TOKEN"; exit 1
fi

echo "🤖 產生 QASM"
python generate_qasm.py --qubits 5 --samples 10 --output for_ibm.qasm

echo "🚀 提交至 IBM Runtime"
echo "import os; os.environ['IBMQ_TOKEN'] = '${IBMQ_TOKEN}'" > patch_submit.py
cat submit_ibm_job_runtime.py >> patch_submit.py
python patch_submit.py for_ibm.qasm

echo "⏳ 等待結果..."
sleep 30

echo "📥 抓取結果"
JOB_ID=$(cat job_id.txt)
echo "import os; os.environ['IBMQ_TOKEN'] = '${IBMQ_TOKEN}'" > patch_fetch.py
cat fetch_result_runtime.py >> patch_fetch.py
python patch_fetch.py "$JOB_ID"

echo "🧠 執行分析"
python auto_decision.py > summary.txt

echo "✅ 完成！分析摘要："
cat summary.txt
