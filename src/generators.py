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
        # Passwords only need 8 bits at a time, which is safe for any hardware
        bits = get_random_bitstring(8, backend)
        number = int(bits, 2)
        password += characters[number % len(characters)]
    return password

def quantum_key(total_bits=128, backend=None):
    """
    Generates a key by chunking bits based on the hardware's qubit limit.
    """
    key = ""
    # Get the max qubits supported by the chosen backend
    # Fallback to 8 if num_qubits attribute is missing
    max_qubits = getattr(backend, 'num_qubits', 8)
    
    # Cap chunk size to 32 to ensure efficient execution and prevent errors
    chunk_size = min(max_qubits, 32)
    
    print(f"Generating {total_bits} bits using {chunk_size} qubits per circuit.")
    
    while len(key) < total_bits:
        bits_needed = total_bits - len(key)
        current_chunk = min(chunk_size, bits_needed)
        
        # Get bits for the current chunk
        chunk = get_random_bitstring(current_chunk, backend)
        key += chunk
        
    return key
