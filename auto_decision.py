import json
from collections import Counter
import csv

def analyze_measurements(results_dict):
    is_float = any(isinstance(v, float) for v in results_dict.values())
    total = sum(results_dict.values())

    bitstring_stats = []
    count_q0_1 = 0

    for bitstring, value in results_dict.items():
        freq = float(value)
        q0 = bitstring[-1]  # 最右邊是 qubit[0]
        if q0 == "1":
            count_q0_1 += freq

        bitstring_stats.append((bitstring, freq, q0, "Zero-Day" if q0 == "1" else "Known"))

    prob_q0_1 = count_q0_1 / total
    attack_type = "Zero-Day" if prob_q0_1 >= 0.5 else "Known Attack"

    # Print summary
    print(f"\n📊 測量總次數（或總機率和）: {total:.2f}")
    print(f"P(qubit[0] = 1) = {prob_q0_1:.4f}")
    print(f"📈 最終判定：{attack_type}")

    # Save markdown summary
    with open("summary.md", "w") as f_md:
        f_md.write("### Summary of IBM Quantum Result\n\n")
        f_md.write(f"- Total shots: {total:.2f}\n")
        f_md.write(f"- P(qubit[0] = 1): `{prob_q0_1:.4f}`\n")
        f_md.write(f"- Final Decision: **{attack_type}**\n")

    # Save CSV
    with open("bitstring_stats.csv", "w", newline="") as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow(["Bitstring", "Freq/Prob", "Qubit[0]", "Class"])
        for row in bitstring_stats:
            writer.writerow(row)

if __name__ == "__main__":
    with open("ibm_result.json", "r") as f:
        counts = json.load(f)
    analyze_measurements(counts)
