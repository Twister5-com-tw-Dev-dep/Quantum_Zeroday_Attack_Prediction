import json
import csv
from collections import defaultdict

def analyze_measurements(results_dict, output_csv="bitstring_stats.csv", output_md="summary.md"):
    total_shots = sum(results_dict.values())
    count_q0_1 = 0

    bit_details = []

    for bitstring, freq in results_dict.items():
        q0 = bitstring[-1]  # 最右邊是 qubit[0]
        is_zero_day = (q0 == '1')
        label = "Zero-Day" if is_zero_day else "Known Attack"
        if is_zero_day:
            count_q0_1 += freq

        bit_details.append({
            "bitstring": bitstring,
            "q0": q0,
            "label": label,
            "freq": freq
        })

    prob_q0_1 = count_q0_1 / total_shots
    verdict = "Zero-Day Attack 🚨" if prob_q0_1 >= 0.5 else "Known Attack ✅"

    # ✅ summary.txt 輸出
    print("📊 分析結果：")
    print(f"P(qubit[0] = 1) = {prob_q0_1:.4f}")
    print(f"📈 判定結果：{verdict}")

    # ✅ summary.md Markdown 報告
    with open(output_md, "w") as f:
        f.write("# 🧠 Quantum Attack Classification Report\n\n")
        f.write(f"**P(qubit[0] = 1)** = `{prob_q0_1:.4f}`\n\n")
        f.write(f"**最終判定**：`{verdict}`\n\n")
        f.write("## 📌 Bitstring 分析表格\n\n")
        f.write("| Bitstring | qubit[0] | 預測類型 | 次數 |\n")
        f.write("|-----------|----------|----------|------|\n")
        for d in sorted(bit_details, key=lambda x: -x["freq"]):
            f.write(f"| `{d['bitstring']}` | `{d['q0']}` | {d['label']} | {d['freq']} |\n")

    # ✅ bitstring_stats.csv 輸出
    with open(output_csv, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["bitstring", "q0", "label", "freq"])
        writer.writeheader()
        writer.writerows(sorted(bit_details, key=lambda x: -x["freq"]))


if __name__ == "__main__":
    with open("ibm_result.json", "r") as f:
        results = json.load(f)
    analyze_measurements(results)
