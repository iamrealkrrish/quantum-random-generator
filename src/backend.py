from qiskit_aer import Aer
from qiskit_ibm_provider import QiskitIBMProvider

def get_backend():
    print("\nChoose backend mode:")
    print("1. Simulation (local PC)")
    print("2. Hardware (IBM Quantum)")
    mode_choice = input("Enter 1 or 2: ").strip()

    if mode_choice == "2":
        token = input("Enter your IBM Quantum API token: ").strip()
        if token:
            try:
                # Modern way to save and load account
                QiskitIBMProvider.save_account(token=token, overwrite=True)
                provider = QiskitIBMProvider()
                
                backends = provider.backends()
                print("\nAvailable IBM Quantum backends:")
                for i, b in enumerate(backends):
                    print(f"{i+1}. {b.name}")
                
                idx = int(input("Select backend number: ").strip())
                return backends[idx-1]
            except Exception as e:
                print(f"Hardware error: {e}. Falling back to simulator.")
    
    print("Using local simulation backend.")
    return Aer.get_backend("qasm_simulator")
