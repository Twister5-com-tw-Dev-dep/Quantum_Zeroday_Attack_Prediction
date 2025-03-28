import sys
import os
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, Session, SamplerV2

def submit_job_runtime(qasm_file: str, token: str, backend_name="ibm_brisbane"):
    # 讀取 QASM 並解析為電路
    with open(qasm_file, "r") as f:
        qasm_str = f.read()
    circuit = QuantumCircuit.from_qasm_str(qasm_str)

    # ✅ 登入 Qiskit Runtime（新版 API）
    service = QiskitRuntimeService(channel="ibm_quantum", token=token)
    print("✅ 成功登入 Qiskit Runtime, channel:", service.channel)
    print("🧠 可用後端：", [b.name for b in service.backends()])
    backend = service.backend(backend_name)

    # ✅ 使用 Session + SamplerV2 正確寫法
    with Session(service=service, backend=backend) as session:
        sampler = SamplerV2(session=session)  # 傳入 session！
        job = sampler.run([circuit])          # 傳入 circuit list
        job_id = job.job_id()

        print(f"✅ Runtime Job submitted! Job ID: {job_id}")
        with open("job_id.txt", "w") as f:
            f.write(job_id)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ 請提供 QASM 檔案，例如 python submit_ibm_job_runtime.py for_ibm.qasm")
        sys.exit(1)

    IBM_TOKEN = os.getenv("IBMQ_TOKEN")
    if not IBM_TOKEN:
        print("❌ IBMQ_TOKEN 未設置")
        sys.exit(1)

    submit_job_runtime(sys.argv[1], IBM_TOKEN)
