# submit_ibm_job.py
from qiskit import QuantumCircuit
from qiskit_ibm_provider import IBMProvider
import sys


def submit_job(qasm_file: str, token: str, backend_name="ibmq_qasm_simulator"):
    with open(qasm_file, "r") as f:
        qasm_str = f.read()
    
    qc = QuantumCircuit.from_qasm_str(qasm_str)
    provider = IBMProvider(token=token)
    backend = provider.get_backend(backend_name)
    job = backend.run(qc)

    print(f"✅ Job submitted! Job ID: {job.job_id()}")
    with open("job_id.txt", "w") as f:
        f.write(job.job_id())
    return job.job_id()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ 請提供 QASM 檔案路徑，例如 python submit_ibm_job.py for_ibm.qasm")
        sys.exit(1)

    IBM_TOKEN = "ba14f19778ab38a6510465c2892fc4e4658f00e76e68d779840156fafa66896b6c8fa058691f884d24a8f937a1defa40e7b30cfba242247fda4a6e013928c4f4"
    submit_job(sys.argv[1], IBM_TOKEN)


# fetch_result.py
from qiskit_ibm_provider import IBMProvider
import sys
import json
import time


def fetch_result(job_id, token, backend_name="ibmq_qasm_simulator"):
    provider = IBMProvider(token=token)
    backend = provider.get_backend(backend_name)
    job = backend.retrieve_job(job_id)

    print(f"📦 Job status: {job.status()}")
    result = job.result()
    counts = result.get_counts()

    with open("ibm_result.json", "w") as f:
        json.dump(counts, f, indent=2)

    print("✅ 測量結果已儲存至 ibm_result.json")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ 請輸入 job ID：python fetch_result.py <JOB_ID>")
        sys.exit(1)

    IBM_TOKEN = "ba14f19778ab38a6510465c2892fc4e4658f00e76e68d779840156fafa66896b6c8fa058691f884d24a8f937a1defa40e7b30cfba242247fda4a6e013928c4f4"
    fetch_result(sys.argv[1], IBM_TOKEN)


# auto_decision.py
import json
from collections import Counter


def analyze_measurements(results_dict):
    total_shots = sum(results_dict.values())
    count_q0_1 = 0

    for bitstring, freq in results_dict.items():
        q0 = bitstring[-1]  # 最右邊是 qubit[0]
        if q0 == '1':
            count_q0_1 += freq

    prob_q0_1 = count_q0_1 / total_shots
    attack_type = "Zero-Day" if prob_q0_1 >= 0.5 else "Known Attack"

    print(f"\n📊 分析結果：")
    print(f"P(qubit[0] = 1) = {prob_q0_1:.4f}")
    print(f"📈 判定結果：{attack_type}")


if __name__ == "__main__":
    with open("ibm_result.json", "r") as f:
        counts = json.load(f)
    analyze_measurements(counts)