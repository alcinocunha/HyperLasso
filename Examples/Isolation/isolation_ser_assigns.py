import sys
import itertools

if __name__ == "__main__":
    # check command line arguments
    if len(sys.argv) != 4:
        print("Usage: python isolation_ser_assigns.py <transactions> <keys> <values>")
        sys.exit(1)

    T = int(sys.argv[1])  # number of transactions
    K = int(sys.argv[2])  # number of keys
    V = int(sys.argv[3])  # number of values

    print("MODULE main")
    print("FROZENVAR")

    for t in range(T):
        for k in range(K):
            print(f"    reads_{t}_{k} : 0..{V};")
            print(f"    writes_{t}_{k} : 0..{V};")

    print("VAR")

    print(f"    t : 0..{T};")

    for t in range(T):
        print(f"    installed_{t} : boolean;")
    
    for k in range(K):
        print(f"    value_{k} : 0..{V};")

    print("ASSIGN")

    def can_install(t):
        stmts = [f"t = {t}", f"!installed_{t}"]
        for k in range(K):
            stmts.append(f"(reads_{t}_{k} = 0 | reads_{t}_{k} = value_{k})")
        return "(" + " & ".join(stmts) + ")"

    for t in range(T):
        print(f"    init(installed_{t}) := FALSE;")
        print(f"    next(installed_{t}) := case (" + can_install(t) + f"): TRUE; TRUE: installed_{t}; esac;")
    for k in range(K):
        print(f"    init(value_{k}) := 0;")
        cases = []
        for t in range(T):
            cases.append(f"(" + can_install(t) + f" & writes_{t}_{k} > 0): writes_{t}_{k};")
        cases.append(f"TRUE: value_{k};")
        print(f"    next(value_{k}) := case " + " ".join(cases) + " esac;")


