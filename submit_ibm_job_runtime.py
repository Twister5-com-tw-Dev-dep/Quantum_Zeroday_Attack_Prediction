import sys
import json
import os
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler

def submit_job_runtime(qasm_file: str, token: str, backend_name="ibm_brisbane"):
    with open(qasm_file, "r") as f:
        qasm_str = f.read()
    circuit = QuantumCircuit.from_qasm_str(qasm_str)

    try:
        # 建立 service：這裡要改成 ibm_quantum
        service = QiskitRuntimeService(channel="ibm_quantum", token=token)
        print(f"✅ 成功登入 Qiskit Runtime, channel: {service.channel}")
        print("🧠 可用後端：", [b.name for b in service.backends()])
    except Exception as e:
        print("❌ 無法建立 QiskitRuntimeService：", e)
        sys.exit(1)

    try:
        backend = service.backend(backend_name)
        sampler = Sampler(backend=backend)
        job = sampler.run(circuits=[circuit])
        job_id = job.job_id()
        print(f"✅ Runtime Job submitted! Job ID: {job_id}")
        with open("job_id.txt", "w") as f:
            f.write(job_id)
    except Exception as e:
        print("❌ 提交任務失敗：", e)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ 請提供 QASM 檔案，例如 python submit_ibm_job_runtime.py for_ibm.qasm")
        sys.exit(1)

    IBM_TOKEN = os.getenv("IBMQ_TOKEN")
    if not IBM_TOKEN:
        print("❌ IBMQ_TOKEN 未設置")
        sys.exit(1)

    submit_job_runtime(sys.argv[1], IBM_TOKEN)
