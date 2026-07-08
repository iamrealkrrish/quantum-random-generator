from qiskit import QuantumCircuit, transpile
import string

def get_random_bitstring(bits, backend):
    qc = QuantumCircuit(bits, bits)
    qc.h(range(bits))
    qc.measure(range(bits), range(bits))
    # Transpilation maps the circuit to the hardware's specific architecture
    qc_t = transpile(qc, backend=backend)
    job = backend.run(qc_t, shots=1)
    return list(job.result().get_counts().keys())[0]

def quantum_password(length=12, backend=None):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    while len(password) < length:
        bits = get_random_bitstring(8, backend)
        number = int(bits, 2)
        password += characters[number % len(characters)]
    return password

def quantum_key(bits=128, backend=None):
    return get_random_bitstring(bits, backend)
