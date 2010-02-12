import unittest, doctest

modules = 'objects server'.split()
docmodules = []

def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    for n in modules:
        ftw = __import__('faketwitter.tests.%s' % (n))
        module = getattr(ftw.tests, n)
        tests = loader.loadTestsFromModule(module)
        suite.addTests(tests)

    for dm in docmodules:
        suite.addTest(doctest.DocTestSuite(dm))

    return suite

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())

