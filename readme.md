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

## 實際測量：

<img width="1280" alt="Screenshot 2025-03-28 at 9 57 53 AM" src="https://github.com/user-attachments/assets/face2e38-d192-4bfe-8fcf-eabfc648db59" />

<img width="361" alt="Screenshot 2025-03-28 at 12 00 11 PM" src="https://github.com/user-attachments/assets/0afade46-34c7-475e-b11a-a3f3d4580c18" />

   # IBM Quantum 測量結果分析(上圖）

## 分析方法
- 該 bitstring 的每個 qubit 值（q[6] ~ q[0]）
  - **qubit[0] 的值（最右邊）** → 是 0 還是 1
  - 根據 qubit[0] 的值，分類為 **Zero-Day** 或 **Known Attack**
  - 顯示該結果的出現次數（Frequency）

## ✅ 逐筆分析結果
| Bitstring | Qubit Values            | Qubit[0] | 判定結果   | 次數 |
|-----------|-------------------------|----------|------------|------|
| 1000101   | q[6]=1 q[5]=0 ... q[0]=1 | 1        | Zero-Day   | 2    |
| 1000011   | q[6]=1 q[5]=0 ... q[0]=1 | 1        | Zero-Day   | 7    |
| 1000001   | q[6]=1 q[5]=0 ... q[0]=1 | 1        | Zero-Day   | 5    |
| 0111111   | q[6]=0 q[5]=1 ... q[0]=1 | 1        | Zero-Day   | 2    |
| 0111101   | q[6]=0 q[5]=1 ... q[0]=1 | 1        | Zero-Day   | 3    |
| 0111011   | q[6]=0 q[5]=1 ... q[0]=1 | 1        | Zero-Day   | 13   |
| 0111000   | q[6]=0 q[5]=1 ... q[0]=0 | 0        | Known      | 10   |
| 0110110   | q[6]=0 q[5]=1 ... q[0]=0 | 0        | Known      | 5    |
| 0110100   | q[6]=0 q[5]=1 ... q[0]=0 | 0        | Known      | 4    |
| 0110001   | q[6]=0 q[5]=1 ... q[0]=1 | 1        | Zero-Day   | 4    |
| 0101111   | q[6]=0 q[5]=1 ... q[0]=1 | 1        | Zero-Day   | 2    |
| 0101100   | q[6]=0 q[5]=1 ... q[0]=0 | 0        | Known      | 3    |
| 0101010   | q[6]=0 q[5]=1 ... q[0]=0 | 0        | Known      | 7    |
| 0101000   | q[6]=0 q[5]=1 ... q[0]=0 | 0        | Known      | 6    |
| 0100110   | q[6]=0 q[5]=1 ... q[0]=0 | 0        | Known      | 1    |
| 0100010   | q[6]=0 q[5]=1 ... q[0]=0 | 0        | Known      | 3    |
| 0011111   | q[6]=0 q[5]=0 ... q[0]=1 | 1        | Zero-Day   | 8    |
| 0011101   | q[6]=0 q[5]=0 ... q[0]=1 | 1        | Zero-Day   | 5    |
| 0011011   | q[6]=0 q[5]=0 ... q[0]=1 | 1        | Zero-Day   | 3    |
| 0011001   | q[6]=0 q[5]=0 ... q[0]=1 | 1        | Zero-Day   | 7    |
| 0010111   | q[6]=0 q[5]=0 ... q[0]=1 | 1        | Zero-Day   | 14   |
| 0010101   | q[6]=0 q[5]=0 ... q[0]=1 | 1        | Zero-Day   | 9    |
| 0010011   | q[6]=0 q[5]=0 ... q[0]=1 | 1        | Zero-Day   | 5    |
| 0010001   | q[6]=0 q[5]=0 ... q[0]=1 | 1        | Zero-Day   | 2    |
| 0001111   | q[6]=0 q[5]=0 ... q[0]=1 | 1        | Zero-Day   | 2    |
| 0001101   | q[6]=0 q[5]=0 ... q[0]=1 | 1        | Zero-Day   | 11   |
| 0001011   | q[6]=0 q[5]=0 ... q[0]=1 | 1        | Zero-Day   | 5    |
| 0001001   | q[6]=0 q[5]=0 ... q[0]=1 | 1        | Zero-Day   | 2    |
| 0000111   | q[6]=0 q[5]=0 ... q[0]=1 | 1        | Zero-Day   | 3    |
| 0000011   | q[6]=0 q[5]=0 ... q[0]=1 | 1        | Zero-Day   | 6    |
| 0000001   | q[6]=0 q[5]=0 ... q[0]=1 | 1        | Zero-Day   | 6    |
| 0000000   | q[6]=0 q[5]=0 ... q[0]=0 | 0        | Known      | 5    |

## 🔢 Qubit[0] 結果分佈統計
| Qubit[0] | 意義          | 出現次數 |
|----------|---------------|----------|
| 1        | Zero-Day      | 165      |
| 0        | Known Attack  | 49       |
| **總計** |               | **214**  |

## 最終模型判斷
- **P(|1⟩) = 0.771** → 高於 0.5  
- **推斷結果**：**「Zero-Day 攻擊」🚨**
### 環境建置


## 🚀 快速開始

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

# 🛠️ 功能強化方向與建議

## 必須：
1. openQASM改善/cd cron to IBM 

## 已完成功能
1. ✅ **自動判斷攻擊類型**
   - 根據 `qubit[0]` 測量結果直接輸出：
     - `1` → **Zero-Day Attack**
     - `0` → **Known Attack**
   - 支援統計 `P(|1⟩)` 機率
   - 可根據閾值（例如 0.5）決定模型輸出

2. 📊 **完整測量結果分析**
   - 對每個測量 bitstring 進行：
     - 拆解 qubit 狀態
     - 判定攻擊類型
     - 顯示出現次數
   - 統整：
     - `qubit[0]` 為 1 和 0 的次數
     - 機率分佈
     - 最終推論結果

## 🔄 後續可擴充功能建議
3. 🔍 **支援多 qubit 輸出分析（多分類模型）**
   - 目前僅使用 `qubit[0]` 做二元分類（Zero-Day / Known）
   - 可擴充為：
     - `qubit[0–1]` → 4 類型分類（例如 DDoS、XSS、SQLi、未知）
     - 使用 qubit 向量進行 **soft decision**

4. 🧠 **將測量結果作為輸出向量輸入傳統機器學習模型**
   - 將多次測量結果的統計分佈（Histogram）視為特徵向量
   - 使用經典 ML 模型（例如 SVM、RandomForest）進一步分類強化

5. 📂 **輸出格式自動化**
   - 自動生成：
     - `summary.txt` / `report.csv`
     - 內容包含每筆 bitstring、次數、分類、`P(|1⟩)`
   - 可整合 log 系統，記錄時間戳與模型參數版本

6. 📈 **視覺化結果 Dashboard**
   - 使用 `matplotlib` 或 `Plotly` 生成：
     - `qubit[0]` 機率曲線
     - bitstring 出現次數直方圖
     - 攻擊類型比例圖
   - 可選擇 CLI 或 Web UI 呈現

7. 🧪 **改進訓練機制**
   - 增加：
     - 參數微調工具（grid search, adaptive rate）
     - 損失函數視覺化
     - 多筆輸入 batch 處理訓練（取代逐筆方式）

8. 🔐 **真實攻擊資料整合**
   - 將模擬資料替換為實際 **IDS logs / threat feeds**
   - 支援轉換來源格式：CSV、JSON、pcap
   - 將攻擊事件特徵對應至 RX 角度映射表

9. 📌 **前處理與特徵工程模組化**
   - 將目前的 `input_data`（`np.random.rand()`）改為：
     - 經過處理的「攻擊事件特徵向量」
     - 加入 normalization、embedding（例如 IP → Geo → Angle）

## 🔄 更新優先順序建議
| 優先等級 | 功能項目                     |
|----------|------------------------------|
| ⭐ **高** | openQASM改善/cd cron to IBM      |
| ⭐ **高** | 自動分類輸出 / 報告輸出      |
| ⭐ **高** | `qubit[0]` 統計機率與分類    |
| 🌟 **中** | 將測量結果餵給傳統 ML 模型    |
| 🌟 **中** | 多 qubit 分類擴展            |
| ✨ **中** | 真實攻擊資料特徵映射          |
| 💡 **低** | 圖形化 UI、Web dashboard      |

## 📖 參考資料

- [Qiskit 官方文件](https://qiskit.org/documentation/)
- [QASM 2.0 規範](https://arxiv.org/abs/1707.03429)

© 2025 Quantum Cybersecurity Analysis Project
