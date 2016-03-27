print "Hello Python"

class TestCase:
	def __init__(self, name):
		self.name = name
	def setUp(self) :
		pass
	def run(self):
		self.setUp()
		method = getattr(self, self.name)
		method()


class WasRun(TestCase):
	def testMethod(self):
		self.WasRun =  1
	def setUp(self) :
		self.WasRun = None
		self.wasSetUp = 1
	

class TestCaseTest(TestCase) :
	def setUp(self) :
		self.test = WasRun("testMethod")
	def testRunning(self) :
		self.test.run()
	      	assert(self.test.WasRun)
	def testSetUp(self) :
		self.test.run()
		assert(self.test.wasSetUp)
	
TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()

print "is There? test"
