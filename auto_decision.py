import json
import csv
from collections import Counter


def analyze_measurements(results_dict):
    total_shots = sum(results_dict.values())
    count_q0_1 = 0

    rows = []

    for bitstring, freq in results_dict.items():
        q0 = bitstring[-1]  # 最右邊是 qubit[0]
        is_zero_day = (q0 == '1')
        count_q0_1 += freq if is_zero_day else 0

        rows.append({
            "bitstring": bitstring,
            "qubit[0]": q0,
            "判定": "Zero-Day" if is_zero_day else "Known Attack",
            "次數": freq
        })

    prob_q0_1 = count_q0_1 / total_shots
    attack_type = "Zero-Day" if prob_q0_1 >= 0.5 else "Known Attack"

    # 標準輸出
    print(f"\n📊 分析結果：")
    print(f"P(qubit[0] = 1) = {prob_q0_1:.4f}")
    print(f"📈 判定結果：{attack_type}")

    # summary.txt for human
    with open("summary.txt", "w") as f:
        f.write("📊 分析結果：\n")
        f.write(f"P(qubit[0] = 1) = {prob_q0_1:.4f}\n")
        f.write(f"📈 判定結果：{attack_type}\n")

    # summary.md for markdown report
    with open("summary.md", "w") as f:
        f.write("## 🧠 Zero-Day Attack Analysis Report\n\n")
        f.write(f"- **P(qubit[0] = 1)**: `{prob_q0_1:.4f}`\n")
        f.write(f"- **判定結果**: `{attack_type}`\n")
        f.write(f"- **總測量次數**: `{total_shots}`\n")

    # CSV 表格輸出 bitstring 頻率統計
    with open("bitstring_stats.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["bitstring", "qubit[0]", "判定", "次數"])
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    with open("ibm_result.json", "r") as f:
        counts = json.load(f)
    analyze_measurements(counts)
