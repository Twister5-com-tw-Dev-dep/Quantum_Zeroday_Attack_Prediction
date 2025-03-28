from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np
import json

print("✅ Qiskit path:", qiskit.__file__)
class TrainableQNN:
    def __init__(self, num_qubits=5):
        self.num_qubits = num_qubits
        self.parameters = np.random.rand(num_qubits) * 2 * np.pi  # 可訓練參數（RY）
        self.input_data = None  # 儲存 RX 特徵

    def create_circuit(self, input_data):
        self.input_data = input_data
        qc = QuantumCircuit(self.num_qubits)

        # 特徵輸入（RX）
        for i, x in enumerate(input_data):
            qc.rx(x, i)

        # 可訓練參數（RY）
        for i, theta in enumerate(self.parameters):
            qc.ry(theta, i)

        # 糾纏（環狀）
        for i in range(self.num_qubits - 1):
            qc.cx(i, i + 1)
        qc.cx(self.num_qubits - 1, 0)

        qc.measure_all()
        return qc

    def simulate_probability(self, circuit, qubit_idx=0):
        state = Statevector.from_instruction(circuit)
        prob = state.probabilities([qubit_idx])
        return prob[1]

    def train(self, dataset, labels, epochs=100, lr=0.1):
        for epoch in range(epochs):
            loss_total = 0
            for x, y in zip(dataset, labels):
                self.input_data = x
                gradient = self._estimate_gradient(x, y)
                self.parameters -= lr * gradient

                prob = self.simulate_probability(self.create_circuit(x), 0)
                loss = (prob - y) ** 2
                loss_total += loss

            if epoch % 10 == 0:
                print(f"Epoch {epoch} - Avg Loss: {loss_total / len(dataset):.4f}")

    def _estimate_gradient(self, x, y, eps=0.01):
        grad = np.zeros_like(self.parameters)
        for i in range(len(self.parameters)):
            plus = self.parameters.copy()
            minus = self.parameters.copy()
            plus[i] += eps
            minus[i] -= eps

            self.parameters = plus
            prob_plus = self.simulate_probability(self.create_circuit(x), 0)

            self.parameters = minus
            prob_minus = self.simulate_probability(self.create_circuit(x), 0)

            grad[i] = (prob_plus - prob_minus) / (2 * eps)

        self.parameters = np.clip(self.parameters, 0, 2 * np.pi)
        return grad

    def save_qasm(self, filename="for_ibm.qasm"):
        if self.input_data is None:
            raise ValueError("⚠️ 尚未設定 input_data，請先呼叫 create_circuit(input_data)")

        qc = self.create_circuit(self.input_data)
        try:
            from qiskit.qasm2 import dumps
            qasm_str = dumps(qc)
        except ImportError:
            qasm_str = qc.qasm()

        with open(filename, "w") as f:
            f.write(qasm_str)
        print(f"✅ 儲存 QASM 至 {filename}")


if __name__ == "__main__":
    np.random.seed(42)

    qnn = TrainableQNN(num_qubits=5)

    # 模擬資料集（例如 10 筆樣本）
    X = np.random.rand(10, 5) * 2 * np.pi
    y = np.random.randint(0, 2, size=10)

    qnn.train(X, y, epochs=50)

    # 將最後一筆 input_data 的電路儲存
    qnn.create_circuit(X[-1])
    qnn.save_qasm("for_ibm.qasm")

    with open("trained_parameters.json", "w") as f:
        json.dump(qnn.parameters.tolist(), f)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Train QNN and export QASM")
    parser.add_argument("--qubits", type=int, default=5)
    parser.add_argument("--samples", type=int, default=10)
    parser.add_argument("--output", type=str, default="for_ibm.qasm")

    args = parser.parse_args()

    model = TrainableQNN(num_qubits=args.qubits)
    X = np.random.rand(args.samples, args.qubits) * 2 * np.pi
    y = np.random.randint(0, 2, args.samples)
    model.train(X, y, epochs=50)
    model.create_circuit(X[-1])
    model.save_qasm(args.output)