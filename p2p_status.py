import common.test as t

def Executor(t):
    return t.ExecuteCommand("p2p status")


def ResultHandler(t, result):
    if result[0] == 0:
        t.MarkAsSucceed()
    else:
        t.MarkAsFailed()


def Test():
    test = t.Test(0, "p2p status")
    test.SetExecutor(Executor)
    test.SetHandler(ResultHandler)

    return test