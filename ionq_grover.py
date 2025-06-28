import math
import os
from qiskit_ionq import IonQProvider
from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import GroverOperator, MCMTGate, ZGate


provider = IonQProvider(os.getenv("IONQ_API_KEY"))
simulater_backend = provider.get_backend("simulator")
simulater_backend.set_options(noise_model="aria-1")

def grover_oracle(marked_states):
	if not isinstance(marked_states, list):
		marked_states = [marked_states]

	num_qubits = len(marked_states[0])
	qc = QuantumCircuit(num_qubits)
    
	for target in marked_states:
		rev_target = target[::-1]
		if rev_target != "111":
			zero_inds = [ind for ind in range(num_qubits) if rev_target.startswith("0", ind)]
			qc.x(zero_inds)
			qc.compose(MCMTGate(ZGate(), num_qubits - 1, 1), inplace=True)
			qc.x(zero_inds)
	return qc

marked_states = ["100", "101", "000"] # 데이터 집단
oracle = grover_oracle(marked_states)
grover_op = GroverOperator(oracle)
optimal_num_iterations = math.floor(math.pi / 4 * math.sqrt(2 ** grover_op.num_qubits / len(marked_states)))

qc = QuantumCircuit(grover_op.num_qubits)
qc.h(range(grover_op.num_qubits))
qc.compose(grover_op.power(optimal_num_iterations), inplace=True)
qc.measure_all()

transpiled_qc = transpile(qc, backend=simulater_backend)

job = simulater_backend.run(transpiled_qc, shots=10000)

print(job.get_counts())