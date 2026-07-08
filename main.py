from src.backend import get_backend
from src.generators import quantum_password, quantum_key

def main():
    backend = get_backend()
    print("\n1. Generate Password\n2. Generate Key")
    choice = input("Enter choice: ").strip()
    
    if choice == "1":
        print("Password:", quantum_password(backend=backend))
    elif choice == "2":
        print("Key:", quantum_key(backend=backend))

if __name__ == "__main__":
    main()
