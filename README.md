# Subutai Guardian
Protects and alerts peer and resource host owners. Just ideas at this point
to fix a lot of our headaches.

# Using Subutai Guardian

To get help about this tool you can simply run `python3 main.py` with no arguments provided.

Arguments:

* `list` - list all test components. Test component is a group of tests related to specific component, e.g. p2p, peeros etc.
* `list componentName` - list all registered tests inside a component
* `run` - run all registered tests
* `run componentName` - run all tests inside specified component
* `run componentName.testName` - run specific test

# Writing tests

If you want to extend this tool with additional tests you need to perform the following steps:

1. Create a separate file for your tests. It's better to use the form of componentName_testName.py
1.a. If your component is completely new you need to create a new file named componentName.py and add it to import list in main.py (see p2p.py for example)
2. In your test file define the following functions:
* `Executor(t)` - main entry point for your test. This function accepts Test class object as an argument
* `ResultHandler(t, result)` - function that will handle results provided by Executor(). In this function you need to define a logic, that will decide
    whether your test was failed or not. Inside this method you need to call `t.MarkAsSucceed()` if test succeed or `t.MarkAsFailed()` otherwise. 
    `ResultHandler` must return an instance of `Result` class.
* `Test()` function must create an instance of `Test` class, providing component name, test name and setting `Executor` and `ResultHandler` callbacks
3. Final step is to open your componentName.py file and add a call of `t.RegisterTest` function with callback to `Test()` function that you defined in a 
previous step

You can use files `p2p.py` and `p2p_daemon.py` as an example.

### Handling test results

To understand the idea behind `ResultHandler()` function we can look at `p2p status` test. This test will execute `p2p status` command and pass result to this handler function. Result is a tuple of 3 elements: exit code, stdout, stderr. In this particular case we want to know whether p2p have broken connections or not. So, inside
a `ResultHandler()` function we're taking `stdout` of `p2p status` and see if it contains 'DISCONNECTED' or 'WAITING_CONNECTION' keywords. If we have such keywords we
consider test as failed and execute `t.MarkAsFailed()`. Then we create an instance of `Result` class and return it. 

# Output

Subutai Guardian generated YAML file (TBD) for each test in the following format:
```
    component: componentName
    name: testName
    timestamp: 1533554195
    status: 0
    peer: <peer_id>
    payload:
        extraField1: value1
        extraField2: value2
```

# List of tests and components

## p2p
* `daemon` (p2p_daemon.py) - check status of p2p daemon
* `status` (p2p_status.py) - executes `p2p status` command