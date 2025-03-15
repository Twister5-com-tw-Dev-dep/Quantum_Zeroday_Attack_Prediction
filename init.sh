#!/bin/zsh

chmod +x setup.sh
./setup.zsh


# 移除alias避免干擾
unalias python 2>/dev/null || true

# 刪除並重建虛擬環境
rm -rf zeroday-prediction
/opt/homebrew/bin/python3.10 -m venv zeroday-prediction

# 啟動虛擬環境
source zeroday-prediction/bin/activate

# 確認python版本
echo "Python version after activating venv:"
python --version

# 升級 pip
python -m pip install --upgrade pip

# 安裝套件
pip install -r requirements.txt

# 檢查Qiskit安裝是否正常
python -c "from qiskit import QuantumCircuit; print(QuantumCircuit(2))"

echo "環境設定完成"
