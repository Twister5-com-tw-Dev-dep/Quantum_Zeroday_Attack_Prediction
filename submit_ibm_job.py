from qiskit import QuantumCircuit
from qiskit_ibm_provider import IBMProvider
import sys


def submit_job(qasm_file: str, token: str, backend_name="ibmq_qasm_simulator"):
    with open(qasm_file, "r") as f:
        qasm_str = f.read()

    qc = QuantumCircuit.from_qasm_str(qasm_str)
    provider = IBMProvider(token=token)

    # 列出所有 backend 並檢查 backend_name 是否存在
    available_backends = [b.name for b in provider.backends()]
    print(f"🧠 可用 backend: {available_backends}")

    if backend_name not in available_backends:
        print(f"❌ 找不到 backend: {backend_name}")
        print("✅ 請改用：", available_backends[0])
        backend_name = available_backends[0]

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
