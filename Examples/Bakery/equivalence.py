import sys

if __name__ == "__main__":
    # check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python equivalence.py <processes>")
        sys.exit(1)

    N = int(sys.argv[1])  # number of processes

    def vars_equal(A,B,i):
        return f"(pc_{i}[{A}] = pc_{i}[{B}] & number_{i}[{A}] = number_{i}[{B}] & tmp_{i}[{A}] = tmp_{i}[{B}])"

    print("Forall A . Exists B . G(" + " & ".join([vars_equal("A","B",i) for i in range(N)]) + ")")