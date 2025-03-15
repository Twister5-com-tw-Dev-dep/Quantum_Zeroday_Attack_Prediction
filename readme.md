## 文件說明

- **Ian_Hu_Masterbate_On_7A.M_Daily_Schedule_Estimation_Network.qasm**: 這個文件包含了量子電路的 QASM 代碼，用於估計某人在特定時間段內的行為。
- **for_ibm.qasm**: 這個文件包含了量子電路的 QASM 代碼，用於技術解決方案的評估。
- **main.py**: 這個文件包含了量子神經網絡的實現，用於訓練和測試量子電路。
- **requirements.txt**: 這個文件列出了專案所需的 Python 依賴項。

## 如何使用

1. **安裝依賴項**:
   使用以下命令安裝專案所需的 Python 依賴項：

   ```bash
   pip install -r requirements.txt
   ```

2. **運行主程序**:
   使用以下命令運行主程序：

   ```bash
   python main.py
   ```

3. **查看結果**:
   程序會輸出當前台北時間、測試預測結果以及最終參數。最終的量子電路表示會保存到 `Ian_Hu_Masterbate_On_7A.M_Daily_Schedule_Estimation_Network.qasm` 文件中。

## 量子電路說明

量子電路由以下幾個部分組成：

1. **初始狀態準備**: 使用旋轉門（rx 和 ry）來創建初始量子態。
2. **次要旋轉**: 使用 ry 旋轉門來創建複雜的量子態。
3. **纏結創建**: 使用 CNOT 門來創建量子纏結。
4. **最終狀態修改**: 使用 X 門來翻轉第一個量子比特的狀態。
5. **測量**: 測量所有量子比特並將結果存儲在經典寄存器中。

## main.py 功能

`main.py` 文件包含了量子神經網絡的實現，用於訓練和測試量子電路。以下是其主要功能：

1. **輸入特徵 (Features)**

   - 攻擊時間 (timestamp)
   - 來源 IP (source_ip)
   - 攻擊類型 (attack_type，例如 SQL Injection, DDoS 等)
   - 是否被攔截 (blocked)
   - 攔截方式 (blocking_method)

2. **量子電路設計**

- 使用 5 量子位 來編碼零日攻擊的相關特徵。
- RX 閘: 用來將攻擊特徵編碼到量子態中。
- RY 參數化旋轉閘: 這些參數將經過訓練來最小化損失函數。
- CNOT 閘: 用於糾纏量子位，讓特徵之間可以有交互作用。

3. **預測輸出**

- 計算第 0 個量子位的測量機率，若 P(|1⟩) 接近 1，則攻擊可能是零日攻擊。
- 若 P(|1⟩) 接近 0，則攻擊可能是已知攻擊。

4. **保存最終量子電路**:
   - 將最終的量子電路表示保存到 `Ian_Hu_Masterbate_On_7A.M_Daily_Schedule_Estimation_Network.qasm` 文件中。

## 參考資料

- [Qiskit Documentation](https://qiskit.org/documentation/)
- [QASM 2.0 Specification](https://arxiv.org/abs/1707.03429)

## next_phase.py

擴展點

    擴增輸入特徵
        增加至 7 維特徵，以更貼近攻擊模式：
            攻擊類型 (SQL Injection, DDoS, XSS, etc.)
            來源 IP
            時間戳
            地理位置
            攻擊模式 (Flooding, Sniffing, etc.)
            歷史發生頻率
            受害端類型 (API, Web, Network)

    持久化訓練參數
        使用 JSON 儲存 訓練好的參數。
        每次啟動時，會嘗試讀取歷史參數，否則隨機初始化。

    量子糾纏與參數化控制
        增加 CNOT + 旋轉門，使量子位間產生非線性互動，增強學習能力。

    真實場景應用
        訓練資料可替換為 現實的零日攻擊數據。
        預測結果可用於 防火牆、入侵檢測系統 (IDS) 決策。
