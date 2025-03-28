from qiskit_ibm_provider import IBMProvider
from qiskit_ibm_runtime import Sampler
import sys
import json


def fetch_runtime_result(job_id, token, backend_name="ibm_brisbane"):
    provider = IBMProvider(token=token)
    backend = provider.get_backend(backend_name)
    sampler = Sampler(session=backend)

    job = sampler.retrieve_job(job_id)
    result = job.result()
    counts = result.quasi_dists[0].binary_probabilities()

    with open("ibm_result.json", "w") as f:
        json.dump(counts, f, indent=2)

    print("✅ 測量結果已儲存至 ibm_result.json")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ 請輸入 job ID，例如 python fetch_result_runtime.py <JOB_ID>")
        sys.exit(1)

    IBM_TOKEN = "ba14f19778ab38a6510465c2892fc4e4658f00e76e68d779840156fafa66896b6c8fa058691f884d24a8f937a1defa40e7b30cfba242247fda4a6e013928c4f4"
    fetch_runtime_result(sys.argv[1], IBM_TOKEN)
