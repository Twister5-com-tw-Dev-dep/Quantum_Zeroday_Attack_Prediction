# Quantum Neural Network for Cybersecurity Analysis

## demo:
- https://youtu.be/GAqObPqVGdQ

## 📌 專案說明

本專案使用量子計算與量子神經網絡（Quantum Neural Network, QNN）技術，分析並預測網路安全攻擊模式，尤其專注於識別零日（Zero-day）攻擊行為。

## 📂 專案結構

| 文件名稱                          | 說明                                                            |
| --------------------------------- | --------------------------------------------------------------- |
| `Zero_Day_Attack_Prediction.qasm` | main.py 生成量子電路版本                                        |
| `for_ibm.qasm`                    | 適用於 IBM Quantum 服務的 QASM 格式電路，可用 api 做 cron job。 |
| `main.py`                         | 量子神經網絡的核心程式碼，用於訓練與預測攻擊模式。              |
| `next_phase.py`                   | 下一階段開發計畫的程式碼草稿，包含進階功能規劃。                |
| `requirements.txt`                | 專案 Python 依賴套件列表。                                      |

## 🚀 快速開始

### 環境建置

```bash
pip install -r requirements.txt
```

### 運行程式

```bash
python main.py
```

程式運行後，會在終端機輸出：

- 目前台北時間
- 預測的攻擊模式結果
- 訓練後最終參數

同時，量子電路會保存到以下 QASM 文件：

- `Zero_Day_Attack_Prediction.qasm`

## 🔮 量子電路設計

此量子電路旨在透過量子狀態編碼安全攻擊的特徵，進而識別攻擊模式：

- **量子位元數**：5 量子位元 (Qubits)
- **量子閘設計**：
  - **初始狀態編碼**：`RX` 閘，編碼攻擊特徵。
  - **參數化旋轉**：`RY` 閘，透過訓練學習參數。
  - **量子糾纏**：`CNOT` 閘，建立特徵交互作用。
  - **狀態反轉**：`X` 閘，調整最終狀態以利測量。
- **測量策略**：
  - 測量第 0 個量子位元，根據其量子態機率判定攻擊是否屬於零日攻擊：
    - 若 `P(|1⟩)` 接近 `1`，則可能為零日攻擊。
    - 若 `P(|1⟩)` 接近 `0`，則為已知攻擊。

## 📋 使用特徵說明

| 特徵名稱   | 說明            | 範例                |
| ---------- | --------------- | ------------------- |
| 攻擊時間   | timestamp       | `2025-03-14T03:05Z` |
| 來源 IP    | source_ip       | `238.54.8.212`      |
| 攻擊類型   | attack_type     | `SQL Injection`     |
| 是否被攔截 | blocked         | `true` 或 `false`   |
| 攔截方式   | blocking_method | `IP Blacklisting`   |

## 🧩 下一階段規劃 (`next_phase.py`)

### 📌 特徵擴充（7 維度）

更豐富的特徵向量，提供精準的零日攻擊偵測：

- 攻擊類型（SQL Injection, DDoS, XSS 等）
- 來源 IP
- 時間戳記
- 地理位置
- 攻擊模式（Flooding, Sniffing 等）
- 歷史發生頻率
- 受害端類型（API, Web, Network 等）
- gate 修正

### 📌 參數持久化儲存

- 採用 JSON 格式儲存訓練完成的模型參數。
- 程式啟動時自動讀取歷史參數，加速訓練流程。

### 📌 量子糾纏與非線性互動增強

- 使用 `CNOT` 與額外的旋轉門 (`RY`、`RZ`) 強化量子糾纏效果，提升模型的非線性分類能力。

### 📌 真實攻擊場景應用

- 使用真實的網路攻擊數據替換現有模擬資料。
- 模型輸出可整合至現有的防火牆及入侵偵測系統（IDS）中，協助安全管理決策。

## 📖 參考資料

- [Qiskit 官方文件](https://qiskit.org/documentation/)
- [QASM 2.0 規範](https://arxiv.org/abs/1707.03429)

© 2025 Quantum Cybersecurity Analysis Project
