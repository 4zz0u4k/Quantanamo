from qiskit import QuantumCircuit

def quantum_rotation_program(angles):
    qc = QuantumCircuit(1, 1)
    
    for angle in angles:
        qc.rx(angle, 0)
        qc.ry(angle * 2, 0)
    
    qc.measure(0, 0)
    return qc

# Example usage
angles = [0.1, 0.2, 0.3]
circuit = quantum_rotation_program(angles)