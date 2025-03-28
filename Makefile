# 用法：
# make install      # 建立虛擬環境與安裝
# make run-all      # 一鍵 QASM + 提交 + 拉回結果 + 分析
# make clean        # 清掉所有暫存結果


.PHONY: install qasm submit fetch analyze run-all clean

install:
	@bash install.sh

qasm:
	@python generate_qasm.py

submit:
	@python submit_ibm_job.py for_ibm.qasm

fetch:
	@python fetch_result.py $$(cat job_id.txt)

analyze:
	@python auto_decision.py

run-all: qasm submit
	@sleep 30
	@make fetch
	@make analyze

clean:
	rm -f for_ibm.qasm job_id.txt ibm_result.json
