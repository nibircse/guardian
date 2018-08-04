# Main class for tests
# Each performing test must create an instance of Test class
# Test class provides several methods that can perform activities on user machine:
# ExecuteCommand - executes a CLI command, gathers exit code, stdout and stderr
#
# Result of each executor will be handled by Result() method which will run user defined
# callback to provide output of expected format


import time
import subprocess
from enum import Enum

def undefinedCallback(result):
    print("Undefined callback")

TestStatus = Enum('TestStatus', 'succeed failed pending running')

TestList = {}

class Test:
    name = "Unnamed"
    createDate = 0
    startDate = 0
    endDate = 0
    executorCallback = undefinedCallback
    handlerCallback = undefinedCallback
    status = TestStatus.pending


    def __init__(self, config, name):
        self.name = name
        self.createDate = time.time()
        self.config = config
        self.status = TestStatus.pending
    

    def SetExecutor(self, cb):
        self.executorCallback = cb


    def SetHandler(self, cb):
        self.handlerCallback = cb


    def Start(self):
        self.startDate = time.time()
        self.status = TestStatus.running
        return self.executorCallback(self)


    def Stop(self):
        self.endDate = time.time()
        return 0

    
    def ExecuteCommand(self, command):
        p = subprocess.Popen(command.split(' '), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        return [p.returncode, out.decode('utf-8'), err.decode('utf-8')]


    def Result(self, result):
        return self.handlerCallback(self, result)


    def MarkAsSucceed(self):
        self.status = TestStatus.succeed


    def MarkAsFailed(self):
        self.status = TestStatus.failed

    
    def GetStatus(self):
        return self.status


# RegisterTest will add test described as `name` to the queue
# executor is a main test entry point
# resultHandler will parse result of executor
def RegisterTest(newTest, name):
    print("Registering test " + name)
    TestList[name] = newTest()