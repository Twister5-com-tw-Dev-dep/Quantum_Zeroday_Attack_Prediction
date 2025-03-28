import numpy as np
import argparse
import os

try:
    from qiskit.qasm2 import dumps  # Qiskit Terra >= 0.25
except ImportError:
    def dumps(circuit):
        return circuit.qasm()

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


class QNNQASMGenerator:
    def __init__(self, num_qubits=5):
        self.num_qubits = num_qubits
        self.params = np.random.rand(num_qubits) * 2 * np.pi

    def create_circuit(self, input_data):
        qc = QuantumCircuit(self.num_qubits)

        # RX: feature encoding
        for i, x in enumerate(input_data):
            qc.rx(x, i)

        # RY: trainable params
        for i, theta in enumerate(self.params):
            qc.ry(theta, i)

        # Entanglement ring
        for i in range(self.num_qubits - 1):
            qc.cx(i, i + 1)
        qc.cx(self.num_qubits - 1, 0)

        return qc

    def simulate_probability(self, circuit, qubit_index=0):
        state = Statevector.from_instruction(circuit)
        prob = state.probabilities([qubit_index])
        return prob[1]  # P(|1⟩)

    def _estimate_gradient(self, input_data, label, epsilon=0.01):
        grads = np.zeros_like(self.params)

        for i in range(len(self.params)):
            orig = self.params[i]

            self.params[i] = orig + epsilon
            plus_prob = self.simulate_probability(self.create_circuit(input_data))

            self.params[i] = orig - epsilon
            minus_prob = self.simulate_probability(self.create_circuit(input_data))

            grads[i] = (plus_prob - minus_prob) / (2 * epsilon)
            self.params[i] = orig

        return grads

    def train(self, X, y, epochs=100, lr=0.1):
        for epoch in range(epochs):
            loss_total = 0
            for xi, yi in zip(X, y):
                prob = self.simulate_probability(self.create_circuit(xi))
                loss = (prob - yi) ** 2
                loss_total += loss

                gradient = self._estimate_gradient(xi, yi)
                self.params -= lr * gradient

            if epoch % 10 == 0:
                print(f"Epoch {epoch}, Loss: {loss_total / len(X):.4f}")

    def export_qasm(self, input_data, save_path="for_ibm.qasm"):
        qc = self.create_circuit(input_data)
        qc.measure_all()  # Only added for QASM output, not simulation
        qasm_str = dumps(qc)
        with open(save_path, "w") as f:
            f.write(qasm_str)
        print(f"✅ QASM exported to: {save_path}")


def generate_synthetic_data(samples=10, num_qubits=5):
    X = np.random.rand(samples, num_qubits) * 2 * np.pi
    y = np.random.randint(0, 2, size=samples)
    return X, y


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--qubits", type=int, default=5)
    parser.add_argument("--samples", type=int, default=10)
    parser.add_argument("--output", type=str, default="for_ibm.qasm")
    args = parser.parse_args()

    X, y = generate_synthetic_data(args.samples, args.qubits)

    qnn = QNNQASMGenerator(num_qubits=args.qubits)
    qnn.train(X, y, epochs=50)

    test_input = X[0]  # pick one for inference and QASM output
    qnn.export_qasm(test_input, save_path=args.output)
