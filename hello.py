print "Hello Python"

class TestCase:
	def __init__(self, name):
		self.name = name
	def run(self):
		method = getattr(self, self.name)
		method()

class WasRun(TestCase):
	def __init__(self, name):
		self.WasRun = None
		TestCase.__init__(self, name)
	def testMethod(self):
		self.WasRun =  1
	def run(self):
		method = getattr(self, self.name)
		method()

class TestCaseTest(TestCase) :
	def testRunning(self) :
	      test = WasRun("testMethod")
	      assert(not test.WasRun)
	      test.run()
	      assert(test.WasRun)
TestCaseTest("testRunning").run()

print "is There?"
