import p2p
import common.test as t

for name, test in t.TestList.items():
    print("Running " + name)
    test.Result(test.Start())
    if test.GetStatus() == t.TestStatus.succeed:
        print("[OK]")
    elif test.GetStatus() == t.TestStatus.failed:
        print("[Failed]")
    else:
        print("[Error]")