import sys

if __name__ == "__main__":
    # check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python symmetric.py <processes>")
        sys.exit(1)

    N = int(sys.argv[1])  # number of processes

    print("Forall A . Exists B . G(" + " & ".join([f"pc_{i}[A] = pc_{(i+1) % N}[B]" for i in range(N)]) + ")")