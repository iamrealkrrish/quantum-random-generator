from src.backend import get_backend
from src.generators import quantum_password, quantum_key

def main():
    backend = get_backend()
    print("\nChoose an option:")
    print("1. Generate Password")
    print("2. Generate Key")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        length = int(input("Enter password length (default 16): ") or 16)
        print("Quantum Password:", quantum_password(length, backend))
    elif choice == "2":
        bits = int(input("Enter key size in bits (default 128): ") or 128)
        print("Quantum Key:", quantum_key(bits, backend))
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
