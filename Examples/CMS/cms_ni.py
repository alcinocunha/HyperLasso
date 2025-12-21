import sys

if __name__ == "__main__":
    # check command line arguments
    if len(sys.argv) != 3:
        print("Usage: python cms_ni.py <reviewers> <articles>")
        sys.exit(1)

    R = int(sys.argv[1])  # number of reviewers
    A = int(sys.argv[2])  # number of articles

    def same_assigns(T,U):
        stmts = []
        for a in range(A):
            for r in range(R):
                stmts.append(f"assigns_{a}_{r}[{T}] = assigns_{a}_{r}[{U}]")
        return "(" + " & ".join(stmts) + ")"

    def aligned(r,T,U):
        stmts = []
        for a in range(A):
            stmts.append(f"(assigns_{a}_{r}[{T}] -> (decision_{a}[{T}] = 0 <-> decision_{a}[{U}] = 0) & " + " & ".join([f"(review_{a}_{r2}[{T}] = 0 <-> review_{a}_{r2}[{U}] = 0)" for r2 in range(R)]) + ")")
        return "G (" + " & ".join(stmts) + ")"

    def all_decided(T):
        stmts = []
        for a in range(A):
            stmts.append(f"decision_{a}[{T}] != 0")
        return "F (" + " & ".join(stmts) + ")"

    def same_reviews(r,T,U):
        stmts = []
        for a in range(A):
            stmts.append(f"(assigns_{a}_{r}[{T}] -> (" + " & ".join([f"review_{a}_{r2}[{T}] = review_{a}_{r2}[{U}]" for r2 in range(R)]) + "))")
        return "G (" + " & ".join(stmts) + ")"
    
    def same_decisions(r,T,U):
        stmts = []
        for a in range(A):
            stmts.append(f"(assigns_{a}_{r}[{T}] -> decision_{a}[{T}] = decision_{a}[{U}])")
        return "G (" + " & ".join(stmts) + ")"

    print("Forall A . Forall B .\n    (" + same_assigns("A","B") + " & " + aligned(0,"A","B") + " & " + all_decided("A") + " & " + all_decided("B") + " & " + same_reviews(0,"A","B") + ") -> " + same_decisions(0,"A","B"))