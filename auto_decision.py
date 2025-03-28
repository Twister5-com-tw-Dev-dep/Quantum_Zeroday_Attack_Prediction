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