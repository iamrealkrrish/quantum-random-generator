from qiskit_aer import Aer
# Note: Newer Qiskit versions use QiskitRuntimeService instead of IBMQ
# You may need to update this based on your Qiskit version

def get_backend():
    print("\nChoose backend mode:")
    print("1. Simulation (local PC)")
    print("2. Hardware (IBM Quantum)")
    mode_choice = input("Enter 1 or 2: ").strip()

    if mode_choice == "2":
        # Hardware logic goes here (use QiskitRuntimeService)
        pass 
    
    print("Using local simulation backend.")
    return Aer.get_backend("qasm_simulator")
