# Example test that checks p2p daemon status

import common.test as t

# Executor is the main entry point for a test
def Executor(t):
    return t.ExecuteCommand("systemctl status sshd.service")


# ResultHandler will handle result returned by executor
# In case of p2p daemon we expect it to have 'active' word in 
# systemctl status command output
def ResultHandler(t, result):
    if 'running' in result[1]:
        t.MarkAsSucceed()
    else:
        t.MarkAsFailed()


def Test():
    test = t.Test(0, "p2p daemon")
    test.SetExecutor(Executor)
    test.SetHandler(ResultHandler)

    return test