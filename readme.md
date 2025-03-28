# Quantum Neural Network for Cybersecurity Analysis
<img width="1280" alt="Screenshot 2025-03-28 at 9 57 53 AM" src="https://github.com/user-attachments/assets/136ca519-ee19-4896-b866-880b43da3cd9" />

<img width="361" alt="Screenshot 2025-03-28 at 12 00 11 PM" src="https://github.com/user-attachments/assets/da615791-6dd8-49a2-a7b1-b91f6cf11a65" />



## 🎥 Demo
- [YouTube Demo 連結](https://youtu.be/GAqObPqVGdQ)

## 📌 專案介紹
本專案結合量子運算與**量子神經網路（Quantum Neural Network, QNN）**，用於網路安全分析，目標是精準識別**零日攻擊（Zero-Day Attack）**。專案包含以下核心模組：
- 使用 **OpenQASM** 定義量子電路結構
- 自動產生並提交 QASM 至 **IBM Quantum** 真實或模擬後端
- 擷取測量結果並進行 `qubit[0]` 分析
- 分類攻擊為 **Known Attack** 或 **Zero-Day Attack**
- 支援 **GitHub Actions** 排程每日自動提交與分析

---

## 🔧 QASM CLI 使用說明
量子電路不像傳統機器學習模型只需幾行程式碼即可生成。在量子世界中，每個 qubit 的角度、旋轉方式以及與其他 qubit 的糾纏順序都會影響整體結果。因此，我們提供 **`generate_qasm.py`** 作為核心工具，讓使用者自訂 qubit 數量與輸出位置，動態產生 QASM 格式的量子電路，並上傳至 IBM Quantum 平台執行。

### 什麼是 QASM？
**QASM（Quantum Assembly Language）** 是一種用來描述量子電路的低階語言，類似傳統電腦的組合語言。IBM 的雲端量子平台支援 **OpenQASM 2.0**，我們透過此格式定義每一個操作與測量。

### 電路結構說明
使用 `generate_qasm.py` 產生的電路包含以下階段：
1. **特徵編碼 (Feature Encoding)**  
   - 每個 qubit 使用 **RX 閘** 進行旋轉，模擬將攻擊行為特徵映射至量子狀態。
2. **參數化學習層 (Trainable Layer)**  
   - 使用 **RY 閘** 將內部參數應用於每個 qubit（類似神經網路中的可訓練權重）。  
   - 目前參數為隨機生成，未來可導入訓練步驟。
3. **量子糾纏 (Entanglement)**  
   - 所有 qubit 以環狀結構串接 **CNOT gate**，使 qubit 狀態互相影響，模擬多特徵交互作用。
4. **測量 (Measurement)**  
   - 將所有 qubit 進行測量，以 `qubit[0]` 的結果（0 或 1）作為分類依據。

### 使用方法
```bash
python generate_qasm.py --qubits 7 --output my_custom.qasm


上述指令會產生一個 7 qubit 的電路，並儲存至 my_custom.qasm 檔案，可直接提交至 IBM Quantum。

參數說明
參數	說明	預設值
--qubits	要使用的 qubit 數量，每個參與特徵編碼與旋轉	5
--output	輸出的 .qasm 檔案名稱，可自訂儲存位置與檔名	for_ibm.qasm
使用情境範例
情境	指令
產生 5 qubit 電路（預設檔案）	python generate_qasm.py
產生 8 qubit 電路並儲存為 q8.qasm	python generate_qasm.py --qubits 8 --output q8.qasm
自動化腳本（搭配 GitHub Actions）	每日自動執行並提交新 QASM
為什麼這麼設計？

這種電路結構參考 Variational Quantum Circuit（VQC） 架構，旨在模擬非線性決策邊界。以 qubit[0] 作為輸出，簡化初期分類模型結構，使測量結果更穩定且易於分析。
🛠️ 功能強化方向
已完成功能

    ✅ 自動判斷攻擊類型
        根據 qubit[0] 測量結果：
            1 → Zero-Day Attack
            0 → Known Attack
        支援統計 P(|1⟩) 機率
        可根據閾值（例如 0.5）決定輸出
    📊 完整測量結果分析
        對每個 bitstring：
            拆解 qubit 狀態
            判定攻擊類型
            顯示次數
        統整：qubit[0] 的 1 和 0 次數、機率分佈、最終推論

🔄 後續可擴充功能建議

    🔍 支援多 qubit 輸出分析（多分類模型）
        目前僅用 qubit[0] 做二元分類
        可擴充至 qubit[0–1] → 4 類型（例如 DDoS、XSS、SQLi、未知）
    🧠 結合傳統機器學習模型
        將測量結果的統計分佈（Histogram）作為特徵向量，輸入 SVM 或 RandomForest
    📂 輸出格式自動化
        自動生成 summary.txt / report.csv，含 bitstring、次數、分類、P(|1⟩)
        整合 log 系統記錄時間戳與參數版本
    📈 視覺化 Dashboard
        使用 matplotlib 或 Plotly 生成機率曲線、bitstring 直方圖、攻擊類型比例圖
        支援 CLI 或 Web UI
    🧪 改進訓練機制
        增加參數微調（如 grid search）、損失函數視覺化、batch 訓練
    🔐 真實攻擊資料整合
        替換模擬資料為 IDS logs / threat feeds（支援 CSV、JSON、pcap）
        將攻擊特徵映射至 RX 角度
    📌 前處理與特徵工程模組化
        將 np.random.rand() 改為處理後的攻擊特徵向量，加入 normalization 與 embedding

🔄 更新優先順序建議
優先等級	功能項目
⭐ 高	自動分類輸出 / 報告輸出
⭐ 高	qubit[0] 統計機率與分類
🌟 中	結合傳統 ML 模型
🌟 中	多 qubit 分類擴展
✨ 中	真實攻擊資料特徵映射
💡 低	圖形化 UI、Web dashboard
