from qiskit_aer import Aer
from qiskit import IBMQ

def get_backend():
    print("\nChoose backend mode:")
    print("1. Simulation (local PC)")
    print("2. Hardware (IBM Quantum, requires API token)")
    mode_choice = input("Enter 1 or 2: ").strip()

    if mode_choice == "2":
        token = input("Enter your IBMQ API token (or press Enter to cancel): ").strip()
        if token:
            try:
                IBMQ.save_account(token, overwrite=True)
                provider = IBMQ.load_account()
                backends = provider.backends()
                print("\nAvailable IBM Quantum backends:")
                for i, b in enumerate(backends):
                    status = provider.get_backend(b.name()).status()
                    print(f"{i+1}. {b.name()} (operational={status.operational}, pending_jobs={status.pending_jobs})")
                
                idx = int(input("Select backend number: ").strip())
                return provider.get_backend(backends[idx-1].name())
            except Exception as e:
                print(f"Hardware error: {e}. Falling back to simulation.")
    
    print("Using local simulation backend.")
    return Aer.get_backend("qasm_simulator")
