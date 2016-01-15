from WasRun import WasRun
from TestCase import TestCase
from TestResult import TestResult

class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 fail" == result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert("1 run, 1 fail" == result.summary())

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testTemplateMethod"))
        suite.add(WasRun("testFailedResult"))
        suite.add(WasRun("testResult"))
        result = suite.run()
        assert("3 run, 1 failed" == result.summary())

# Monday 13:30 - 14:00
#print TestCaseTest("testTemplateMethod").run().summary()
#print TestCaseTest("testFailedResult").run().summary()
print TestCaseTest("testResult").run().summary()
print TestCaseTest("testSuite").run().summary()


# DONE : call tearDown
# TODO : count test, count fail
# TODO : even if test fails, run tearDown
# TODO : run multi testCase
# TODO : report test results