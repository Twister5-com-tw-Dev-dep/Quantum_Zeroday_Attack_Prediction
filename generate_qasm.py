from qiskit import QuantumCircuit
import numpy as np
import os

# --- 相容新版與舊版 Qiskit 的 QASM 匯出 ---
try:
    from qiskit.qasm2 import dumps  # For Qiskit Terra >= 0.25
except ImportError:
    # fallback to .qasm() method for older versions
    def dumps(circuit):
        return circuit.qasm()


def generate_qasm(save_path="for_ibm.qasm"):
    num_qubits = 5
    input_data = np.random.rand(num_qubits) * 2 * np.pi
    params = np.random.rand(num_qubits) * 2 * np.pi

    qc = QuantumCircuit(num_qubits)

    # RX: input features
    for i, x in enumerate(input_data):
        qc.rx(x, i)

    # RY: trainable params (simulated)
    for i, theta in enumerate(params):
        qc.ry(theta, i)

    # Entanglement ring
    for i in range(num_qubits - 1):
        qc.cx(i, i + 1)
    qc.cx(num_qubits - 1, 0)

    qc.measure_all()

    qasm_str = dumps(qc)
    with open(save_path, "w") as f:
        f.write(qasm_str)
    print(f"✅ QASM generated and saved to {save_path}")


if __name__ == "__main__":
    generate_qasm()
