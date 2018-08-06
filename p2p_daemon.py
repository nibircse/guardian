# Example test that checks p2p daemon status

import common.test as t
import common.result as r

# Executor is the main entry point for a test
# This function 
def Executor(t):
    return t.ExecuteCommand("systemctl status subutai-p2p.service")


# ResultHandler will handle result returned by executor
# In case of p2p daemon we expect it to have 'active' word in 
# systemctl status command output
def ResultHandler(t, result):
    status = -1
    if 'running' in result[1]:
        t.MarkAsSucceed()
        status = 0
    else:
        t.MarkAsFailed()
        status = 1
    
    result = r.Result(t.GetComponent(), t.GetName(), status)
    # If you have additional data for results, you can use r.append(key, value) method
    # All extra fields will be added to payload field of resulting YAML
    return result

# Test creates an instance of `Test` class, sets callbacks and returns it
# for later registration
def Test():
    test = t.Test(0, "p2p", "daemon")
    test.SetExecutor(Executor)
    test.SetHandler(ResultHandler)

    return test