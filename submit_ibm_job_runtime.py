import sys
import os
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, Session, SamplerV2


def submit_job_runtime(qasm_file: str, token: str, backend_name="ibm_brisbane"):
    # 讀取 QASM 檔案並建立電路
    with open(qasm_file, "r") as f:
        qasm_str = f.read()
    circuit = QuantumCircuit.from_qasm_str(qasm_str)

    # ✅ 登入 Qiskit Runtime
    service = QiskitRuntimeService(channel="ibm_quantum", token=token)
    print("✅ 成功登入 Qiskit Runtime, channel:", service.channel)

    # 🔍 顯示所有支援 Sampler 的 backend（optional）
    print("🧠 可用後端（支援 Sampler）：")
    for backend in service.backends():
        if backend.target.has("sampler"):
            print(f" - {backend.name}")

    backend = service.backend(backend_name)
    print(f"✅ 選擇後端：{backend_name}")

    # ✅ SamplerV2 搭配 Session（使用 shots=512）
    with Session(service=service, backend=backend) as session:
        sampler = SamplerV2(session=session, options={"shots": 512})
        job = sampler.run([circuit])
        print(f"⏳ Job {job.job_id()} submitted，等待完成中...")

        job.wait_for_final_state()
        print(f"✅ Job 狀態：{job.status()}")

        # 儲存 Job ID
        with open("job_id.txt", "w") as f:
            f.write(job.job_id())

        print(f"📦 Job ID 已儲存至 job_id.txt")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ 請提供 QASM 檔案，例如 python submit_ibm_job_runtime.py for_ibm.qasm")
        sys.exit(1)

    IBM_TOKEN = os.getenv("IBMQ_TOKEN")
    if not IBM_TOKEN:
        print("❌ IBMQ_TOKEN 未設置")
        sys.exit(1)

    submit_job_runtime(sys.argv[1], IBM_TOKEN)
