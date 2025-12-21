import sys
import itertools

if __name__ == "__main__":
    # check command line arguments
    if len(sys.argv) != 3:
        print("Usage: python equivalence.py <reviewers> <articles>")
        sys.exit(1)

    R = int(sys.argv[1])  # number of reviewers
    A = int(sys.argv[2])  # number of articles

    def init(T):
        constraints = []
        for a in range(A):
            constraints.append("(" + " | ".join([f"assigns_{a}_{r}[{T}]" for r in range(R)]) + ")")
        for r in range(R):
            constraints.append("(" + " | ".join([f"assigns_{a}_{r}[{T}]" for a in range(A)]) + ")")
        return "(" + " & ".join(constraints) + ")"

    def vars_equal(T,U):
        constraints = []

        for a in range(A):
            for r in range(R):
                constraints.append(f"(assigns_{a}_{r}[{T}] <-> assigns_{a}_{r}[{U}])")
                constraints.append(f"(review_{a}_{r}[{T}] = review_{a}_{r}[{U}])")
        for a in range(A):
            constraints.append(f"(decision_{a}[{T}] = decision_{a}[{U}])")

        return " & ".join(constraints)
    
    print("Forall A . Exists B . " + init("A") + " -> G (" + vars_equal("A","B") + ")")
