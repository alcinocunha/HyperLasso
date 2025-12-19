import sys
import itertools

if __name__ == "__main__":
    # check command line arguments
    if len(sys.argv) != 4:
        print("Usage: python equivalence.py <transactions> <keys> <values>")
        sys.exit(1)

    T = int(sys.argv[1])  # number of transactions
    K = int(sys.argv[2])  # number of keys
    V = int(sys.argv[3])  # number of values

    def init(A):
        constraints = []

        for t in range(T):
            constraints.append("(" + " | ".join([f"writes_{t}_{k}[{A}] > 0" for k in range(K)]) + ")")

        for k in range(K):
            for t1,t2 in itertools.combinations(range(T),2):
                constraints.append(f"(writes_{t1}_{k}[{A}] = 0 | writes_{t2}_{k}[{A}] = 0 | writes_{t1}_{k}[{A}] != writes_{t2}_{k}[{A}])")
        
        return "(" + " & ".join(constraints) + ")"

    def vars_equal(A,B):
        constraints = []
        for t in range(T):
            constraints.append(f"installed_{t}[{A}] = installed_{t}[{B}]")
        for k in range(K):
            constraints.append(f"value_{k}[{A}] = value_{k}[{B}]")
        for t in range(T):
            for k in range(K):
                constraints.append(f"(reads_{t}_{k}[{A}] = reads_{t}_{k}[{B}])")
                constraints.append(f"(writes_{t}_{k}[{A}] = writes_{t}_{k}[{B}])")
        return " & ".join(constraints)
    
    print("Forall A . Exists B . " + init("A") + " -> G (" + vars_equal("A","B") + ")")
