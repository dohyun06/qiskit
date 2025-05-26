from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_multivector, plot_histogram

# 예시 회로 생성
qc = QuantumCircuit(3, 3)
qc.h(0)
qc.cx(0, 1)
qc.ccx(0, 1, 2) # 토폴리 게이트 (CCX) 추가
qc.measure_all() # 모든 큐비트를 측정하고 결과를 해당 고전 비트에 저장

# 회로 그리기 (Matplotlib 사용)
# Jupyter Notebook 또는 GUI 환경에서 실행 시 유용
# qc.draw(output='mpl') # 이 줄의 주석을 해제하고 실행해 보세요.

# (이전 예제와 같이 시뮬레이션 후)
# 결과 시각화
# simulator = AerSimulator()
# compiled_circuit = transpile(qc, simulator)
# job = simulator.run(compiled_circuit, shots=1024)
# result = job.result()
# counts = result.get_counts(qc)
# plot_histogram(counts) # 히스토그램 시각화

# 큐비트 상태 시각화 (시뮬레이션 필요)
# from qiskit import Aer
# backend_statevector = Aer.get_backend('statevector_simulator')
# out_state = backend_statevector.run(qc.remove_final_measurements(inplace=False)).result().get_statevector()
# plot_bloch_multivector(out_state) # 블로흐 구면으로 큐비트 상태 시각화

print("회로 구조 (텍스트):")
print(qc.draw(output='text'))