import sys
import json
import os
from qiskit_ibm_runtime import QiskitRuntimeService

def fetch_result_runtime(job_id: str, token: str):
    service = QiskitRuntimeService(channel="cloud", token=token)
    job = service.job(job_id)
    print(f"📦 Job status: {job.status()}")
    
    result = job.result()
    counts = result.quasi_dists[0].binary_probabilities()

    with open("ibm_result.json", "w") as f:
        json.dump(counts, f, indent=2)
    print("✅ 測量結果已儲存至 ibm_result.json")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ 請輸入 job ID，例如：python fetch_result_runtime.py <JOB_ID>")
        sys.exit(1)

    IBM_TOKEN = os.getenv("IBMQ_TOKEN")
    if not IBM_TOKEN:
        print("❌ IBMQ_TOKEN 未設置")
        sys.exit(1)

    fetch_result_runtime(sys.argv[1], IBM_TOKEN)



