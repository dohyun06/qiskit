from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator # Qiskit 0.46.0부터 qiskit.providers.aer 대신 사용
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt # 시각화를 위해 필요할 수 있음

# 2큐비트 양자 회로와 2클래식 비트 생성
circuit = QuantumCircuit(2, 2)

# H 게이트를 0번 큐비트에 적용
circuit.h(0)

# CX (CNOT) 게이트를 0번 큐비트(제어)와 1번 큐비트(타겟)에 적용
circuit.cx(0, 1)

# 0번 큐비트를 0번 클래식 비트에, 1번 큐비트를 1번 클래식 비트에 측정
circuit.measure([0, 1], [0, 1])

# Aer 시뮬레이터 사용
simulator = AerSimulator()

# 시뮬레이터를 위해 회로 트랜스파일
compiled_circuit = transpile(circuit, simulator)

# 시뮬레이터에서 회로 실행 (1000번 반복)
job = simulator.run(compiled_circuit, shots=1000)

# 결과 가져오기
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:", counts)

# 히스토그램 그리기 (터미널에서 실행 시 별도 창으로 표시)
plot_histogram(counts)
plt.show() # Matplotlib 그래프를 보여주기 위해 필요