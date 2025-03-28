# Quantum Neural Network for Cybersecurity Analysis

## demo:

- https://youtu.be/GAqObPqVGdQ

📌 專案介紹

本專案結合量子運算與量子神經網路（Quantum Neural Network, QNN）來進行網路安全分析，目標為精準識別零日攻擊（Zero-Day Attack）。

專案分為以下核心模組：

使用 OpenQASM 定義量子電路結構

自動產生並提交 QASM 至 IBM Quantum 真實或模擬後端

擷取測量結果並進行 qubit[0] 分析

分類攻擊為 Known Attack 或 Zero-Day Attack

支援 GitHub Actions 排程每日自動提交與分析

🧠 核心概念

🧬 QNN 架構說明

Qubits 數量：使用 5 個 qubit 來建立電路

電路階段設計：

RX 閘：編碼輸入攻擊特徵（模擬生成）

RY 閘：引入隨機/訓練參數（模擬權重）

CNOT：建立量子糾纏（全環狀連接）

測量 qubit[0]：根據其 P(|1⟩) 作為攻擊分類依據

🧪 分類邏輯

若 qubit[0] 測量結果為 1（或 P(|1⟩) 趨近 1）→ 判定為 Zero-Day

若 qubit[0] 為 0（或 P(|1⟩) 趨近 0）→ 判定為 Known Attack

📂 專案目錄結構（Version 2.0）

Quantum_Zeroday_Attack_Prediction/
├── .github/
│ └── workflows/
│ └── ibm_pipeline.yml # GitHub Actions 自動排程任務
├── auto_decision.py # 根據 qubit[0] 分析 Zero-Day 或 Known
├── fetch_result.py # 根據 job ID 抓回 IBM 執行結果 JSON
├── for_ibm.qasm # 每次自動產生的 QASM 電路
├── generate_qasm.py # 使用 RX+RY+CNOT 建立 QASM 電路結構
├── install.sh # 建立虛擬環境並安裝依賴
├── job_id.txt # 暫存 IBM job ID
├── ibm_result.json # 儲存 IBM 測量結果 (counts)
├── main.py # 主程式，讀取 QASM 並模擬 statevector 分析
├── Makefile # 指令列工具：一鍵建構、提交、分析
├── requirements.txt # Python 依賴列表（Qiskit + NumPy）
├── run_ibm_pipeline.sh # 本地端一鍵完整流程腳本
└── submit_ibm_job.py # 上傳 QASM 電路至 IBM Quantum 後端

🧩 每個模組說明

檔案名稱

功能說明

generate_qasm.py

使用隨機 RX + RY gate 產生 QASM 並儲存至 for_ibm.qasm

submit_ibm_job.py

使用 IBM API 將 QASM 電路上傳，並儲存 job ID

fetch_result.py

根據 job ID 擷取測量結果，輸出 ibm_result.json

auto_decision.py

根據 qubit[0] 為 1 的比率，自動判斷攻擊類型

run_ibm_pipeline.sh

本地端自動化整合：產生 → 上傳 → 擷取 → 分析

Makefile

定義 make run-all 等快捷操作

main.py

載入 .qasm 並以 statevector 模擬攻擊預測

🚀 使用方式

🔧 安裝環境（建議使用 venv）

bash install.sh
source .venv/bin/activate

或手動：

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

▶️ 執行一鍵流程（本地）

bash run_ibm_pipeline.sh

或：

make run-all

⚙️ GitHub Actions 自動執行

新增 GitHub Repository Secret 名為 IBMQ_TOKEN

系統會每天自動提交電路並分析結果

使用 workflow_dispatch 可手動觸發

📊 IBM Quantum 結果分析邏輯

IBM 測量回傳的 histogram 結果是一組 bitstring: frequency，例如：

"0010111": 14,
"0000000": 5,

解釋邏輯：

每個 bitstring 長度為 7，代表 7 個 qubit 測量值（q[6] 為左、q[0] 為右）

我們只看最右邊（q[0]）的值：

1 → 推論為 Zero-Day 攻擊

0 → 推論為 Known Attack

使用 auto_decision.py 將自動：

統計 qubit[0] 為 1 的機率

輸出 P(|1⟩) = 0.77 這類結果

自動做出分類判斷

📈 擴充功能與規劃建議

✅ 已實作

🔄 建議功能

📖 參考資料

Qiskit 官方文件

OpenQASM 2.0 規範

IBM Quantum Experience

© 2025 Quantum Cybersecurity Analysis Project
