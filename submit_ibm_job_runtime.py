from qiskit import QuantumCircuit
from qiskit_ibm_provider import IBMProvider
from qiskit_ibm_runtime import Sampler
import sys


def submit_job_runtime(qasm_file: str, token: str, backend_name="ibm_brisbane"):
    with open(qasm_file, "r") as f:
        qasm_str = f.read()

    qc = QuantumCircuit.from_qasm_str(qasm_str)

    provider = IBMProvider(token=token)
    backend = provider.get_backend(backend_name)
    sampler = Sampler(session=backend)

    print(f"✅ Submitting to {backend_name} via Qiskit Runtime Sampler...")
    job = sampler.run(circuits=[qc])
    print(f"✅ Job submitted. Job ID: {job.job_id}")

    with open("job_id.txt", "w") as f:
        f.write(job.job_id)

    return job.job_id


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ 請提供 QASM 檔案，例如 python submit_ibm_job_runtime.py for_ibm.qasm")
        sys.exit(1)

    IBM_TOKEN = "你的 IBM API Token"
    submit_job_runtime(sys.argv[1], IBM_TOKEN)
