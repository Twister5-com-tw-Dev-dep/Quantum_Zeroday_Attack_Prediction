
from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
import numpy as np
import pytz
import json
from datetime import datetime

class QASMZeroDayPredictor:
    def __init__(self, qasm_file="for_ibm.qasm"):
        self.num_qubits = 5  # 5 個 qubits, 來自 for_ibm.qasm
        self.num_parameters = 0  # for_ibm.qasm 沒有可訓練參數
        self.qasm_file = qasm_file
        self.circuit = self.load_qasm_circuit()

    def load_qasm_circuit(self):
        try:
            with open(self.qasm_file, "r") as f:
                qasm_str = f.read()
            circuit = QuantumCircuit.from_qasm_str(qasm_str)
            return circuit
        except FileNotFoundError:
            print(f"⚠️ 未找到 QASM 文件: {self.qasm_file}")
            return None
        except Exception as e:
            print(f"⚠️ 載入 QASM 檔案時發生錯誤: {e}")
            return None

    def create_quantum_circuit(self, input_data=None):
        if self.circuit is None:
            print("⚠️ 無法建立電路，因為 QASM 檔案載入失敗。")
            return None
        return self.circuit

    def get_statevector(self, circuit):
        if circuit is None:
            return None
        return Statevector.from_instruction(circuit)

    def calculate_probability(self, statevector, qubit_idx=0):
        if statevector is None:
            return 0.0
        probabilities = statevector.probabilities([qubit_idx])
        return probabilities[1]  # 取 |1⟩ 機率

    def train_network(self, training_data, labels, epochs=500, learning_rate=0.01):
        print("⚠️  此模型不包含訓練步驟，因為它使用固定的 QASM 電路。")
        return None

    def calculate_gradient(self, input_data, label, epsilon=0.01):
        print("⚠️  此模型不包含梯度計算，因為它使用固定的 QASM 電路。")
        return None

    def save_parameters(self, filename="trained_parameters.json"):
        print("⚠️  此模型不包含參數儲存，因為它使用固定的 QASM 電路。")

    def load_parameters(self, filename="trained_parameters.json"):
        print("⚠️  此模型不包含參數載入，因為它使用固定的 QASM 電路。")

def get_current_time_in_taipei():
    taipei_tz = pytz.timezone('Asia/Taipei')
    return datetime.now(taipei_tz).strftime("%Y-%m-%d %H:%M:%S")

def simulate_attack_data(num_samples=20):
    """ 模擬零日攻擊與已知攻擊的數據集 """
    # 由於我們使用固定的 QASM 電路，因此不需要訓練數據
    return None, None

def main():
    np.random.seed(42)

    # **載入歷史參數 (如果存在)**
    qnn = QASMZeroDayPredictor()

    # **產生訓練數據**
    # training_data, labels = simulate_attack_data(num_samples=50)  # 不再需要
    # trained_parameters = qnn.train_network(training_data, labels, epochs=500)  # 不再需要

    # **測試數據**
    test_data = None  # 不再需要
    test_circuit = qnn.create_quantum_circuit()
    if test_circuit is None:
        print("⚠️ 無法進行預測，因為電路載入失敗。")
        return
    test_statevector = qnn.get_statevector(test_circuit)
    prediction = qnn.calculate_probability(test_statevector)

    print(f"\n📍 當前時間 (台北): {get_current_time_in_taipei()}")
    print(f"⚠️  預測零日攻擊機率: {prediction:.4f}")
    # print(f"🎯 最終參數: {trained_parameters}")  # 不再需要

    # **儲存 QASM**
    # final_circuit = qnn.create_quantum_circuit()  # 不再需要
    # if final_circuit is None:
    #     print("⚠️ 無法生成 QASM 字串")
    #     return
    # try:
    #     qasm_str = final_circuit.qasm()
    # except AttributeError:
    #     print("⚠️ 警告: 無法生成 QASM 字串")
    #     qasm_str = str(final_circuit)
    #
    # with open("Zero_Day_Attack_Prediction.qasm", "w") as f:
    #     f.write(qasm_str)
    #
    # print("\n✅ 最終電路已存儲至 'Zero_Day_Attack_Prediction.qasm'")

if __name__ == "__main__":
    main()