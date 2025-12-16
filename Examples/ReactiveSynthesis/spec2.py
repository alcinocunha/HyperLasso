import sys

if __name__ == "__main__":
    # check command line arguments
    if len(sys.argv) != 3:
        print("Usage: python spec.py <states> <transitions>")
        sys.exit(1)

    S = int(sys.argv[1])  # number of states
    T = int(sys.argv[2])  # number of transitions
    
    def transition(C,W,M,t):
        stmts = []
        stmts.append(f"state[{M}] = from_{t}[{C}] & X (state[{M}] = to_{t}[{C}])")
        stmts.append(f"waiting_{t}_left[{C}] = waiting_left[{W}] & waiting_{t}_right[{C}] = waiting_right[{W}]")
        stmts.append(f"green_left[{M}] = green_{t}_left[{C}] & green_right[{M}] = green_{t}_right[{C}]")
        return " & ".join(stmts)

    def no_transition(C,W,M):
        stmts = []
        for t in range(T):
            stmts.append(f"!(from_{t}[{C}] = state[{M}] & waiting_{t}_left[{C}] = waiting_left[{W}] & waiting_{t}_right[{C}] = waiting_right[{W}])")
        stmts.append(f"!green_left[{M}] & !green_right[{M}]")
        for s in range(S):
            stmts.append(f"(state[{M}] = {s} -> X (state[{M}] = {s}))")
        return " & ".join(stmts)
    
    def behavior(C,W,M):
        return "G (" + " | ".join([f"(" + transition(C,W,M,t) + ")" for t in range(T)] + [f"(" + no_transition(C,W,M) + ")"]) + ")"
    
    def guarantee(A):
        return f"G (!green_left[{A}] | !green_right[{A}]) & G (F green_left[{A}]) & G (F green_right[{A}])"

    print("Forall C . Exists W . Forall M . !(" + behavior("C","W","M") + " & " + guarantee("M") + ")")
