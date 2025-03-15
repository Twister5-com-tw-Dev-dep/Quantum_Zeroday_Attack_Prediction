from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np
import pytz
import json
from datetime import datetime

class QASMZeroDayPredictor:
    def __init__(self):
        self.num_qubits = 7  # 7 個 qubits, 映射攻擊特徵
        self.num_parameters = 7  # 7 個可訓練參數
        self.parameters = np.random.rand(self.num_parameters) * 2 * np.pi  # 初始化參數

    def create_quantum_circuit(self, input_data):
        qc = QuantumCircuit(self.num_qubits)

        # **步驟 1: 編碼攻擊特徵**
        for i, data in enumerate(input_data[: self.num_qubits]):  # 限制到 qubits 數量
            qc.rx(data, i)

        # **步驟 2: 參數化旋轉**
        for i, param in enumerate(self.parameters):
            qc.ry(param, i)

        # **步驟 3: 量子糾纏**
        for i in range(self.num_qubits - 1):
            qc.cx(i, i + 1)
        qc.cx(self.num_qubits - 1, 0)  # 閉合循環糾纏

        return qc

    def get_statevector(self, circuit):
        return Statevector.from_instruction(circuit)

    def calculate_probability(self, statevector, qubit_idx=0):
        probabilities = statevector.probabilities([qubit_idx])
        return probabilities[1]  # 取 |1⟩ 機率

    def train_network(self, training_data, labels, epochs=500, learning_rate=0.01):
        for epoch in range(epochs):
            total_loss = 0
            for data, label in zip(training_data, labels):
                circuit = self.create_quantum_circuit(data)
                statevector = self.get_statevector(circuit)
                output_prob = self.calculate_probability(statevector)

                # 均方誤差 (MSE)
                loss = (output_prob - label) ** 2
                total_loss += loss

                # 梯度下降更新參數
                gradient = self.calculate_gradient(data, label)
                self.parameters -= learning_rate * gradient

            if epoch % 100 == 0:
                print(f"Epoch {epoch}, Loss: {total_loss/len(training_data):.4f}")

        self.save_parameters()
        return self.parameters

    def calculate_gradient(self, input_data, label, epsilon=0.01):
        gradient = np.zeros_like(self.parameters)

        for i in range(len(self.parameters)):
            params_plus = self.parameters.copy()
            params_minus = self.parameters.copy()
            params_plus[i] += epsilon
            params_minus[i] -= epsilon

            prob_plus = self.calculate_probability(self.get_statevector(self.create_quantum_circuit(input_data)))
            prob_minus = self.calculate_probability(self.get_statevector(self.create_quantum_circuit(input_data)))

            gradient[i] = (prob_plus - prob_minus) / (2 * epsilon)

        return gradient

    def save_parameters(self, filename="trained_parameters.json"):
        with open(filename, "w") as f:
            json.dump(self.parameters.tolist(), f)
        print("✅ 訓練參數已儲存！")

    def load_parameters(self, filename="trained_parameters.json"):
        try:
            with open(filename, "r") as f:
                self.parameters = np.array(json.load(f))
            print("✅ 訓練參數已加載！")
        except FileNotFoundError:
            print("⚠️ 未找到參數文件，使用隨機初始化參數！")

def get_current_time_in_taipei():
    taipei_tz = pytz.timezone('Asia/Taipei')
    return datetime.now(taipei_tz).strftime("%Y-%m-%d %H:%M:%S")

def simulate_attack_data(num_samples=20):
    """ 模擬零日攻擊與已知攻擊的數據集 """
    training_data = np.random.rand(num_samples, 7) * 2 * np.pi
    labels = np.random.randint(0, 2, num_samples)  # 0=已知攻擊, 1=零日攻擊
    return training_data, labels

def main():
    np.random.seed(42)

    # **載入歷史參數 (如果存在)**
    qnn = QASMZeroDayPredictor()
    qnn.load_parameters()

    # **產生訓練數據**
    training_data, labels = simulate_attack_data(num_samples=50)
    trained_parameters = qnn.train_network(training_data, labels, epochs=500)

    # **測試數據**
    test_data = np.random.rand(7) * 2 * np.pi
    test_circuit = qnn.create_quantum_circuit(test_data)
    test_statevector = qnn.get_statevector(test_circuit)
    prediction = qnn.calculate_probability(test_statevector)

    print(f"\n📍 當前時間 (台北): {get_current_time_in_taipei()}")
    print(f"⚠️  預測零日攻擊機率: {prediction:.4f}")
    print(f"🎯 最終參數: {trained_parameters}")

    # **儲存 QASM**
    final_circuit = qnn.create_quantum_circuit(test_data)
    try:
        qasm_str = final_circuit.qasm()
    except AttributeError:
        print("⚠️ 警告: 無法生成 QASM 字串")
        qasm_str = str(final_circuit)

    with open("Zero_Day_Attack_Prediction.qasm", "w") as f:
        f.write(qasm_str)

    print("\n✅ 最終電路已存儲至 'Zero_Day_Attack_Prediction.qasm'")

if __name__ == "__main__":
    main()


#梯度計算：
您的程式碼使用數值梯度來計算梯度。 這可能比解析梯度慢。
建議： 如果可能，嘗試使用 Qiskit 的自動微分功能或手動計算解析梯度，以提高訓練速度。
參數初始化：
您的程式碼使用隨機初始化參數。
建議： 嘗試不同的參數初始化方法，例如 Xavier 初始化或 He 初始化，以改善訓練效果。