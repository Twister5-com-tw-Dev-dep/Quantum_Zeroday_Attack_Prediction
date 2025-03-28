#!/bin/bash

set -e

QASM_FILE="for_ibm.qasm"
JOB_ID_FILE="job_id.txt"

echo "🚀 [1/4] 提交 QASM 至 IBM Quantum..."
python submit_ibm_job.py $QASM_FILE

echo "🕒 [2/4] 等待 30 秒讓任務開始執行..."
sleep 30

JOB_ID=$(cat $JOB_ID_FILE)
echo "🔍 Job ID: $JOB_ID"

echo "📥 [3/4] 下載執行結果..."
python fetch_result.py $JOB_ID

echo "📈 [4/4] 自動攻擊判斷中..."
python auto_decision.py
