from qiskit_ibm_provider import IBMProvider
import sys
import json
import time


def fetch_result(job_id, token, backend_name="ibmq_qasm_simulator"):
    provider = IBMProvider(token=token)
    backend = provider.get_backend(backend_name)
    job = backend.retrieve_job(job_id)

    print(f"📦 Job status: {job.status()}")

    # 若 job 還在 queue，中止流程
    if job.status().name != "DONE":
        print("⏳ Job 尚未完成，請稍後再試")
        return

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
