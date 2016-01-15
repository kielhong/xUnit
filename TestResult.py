class TestResult:
    def __init__(self):
        self.count = 0
        self.failCount = 0

    def testStarted(self):
        self.count = self.count + 1

    def testFailed(self):
        self.failCount = self.failCount + 1

    def summary(self):
        return "%d run, %d fail" % (self.count, self.failCount)
