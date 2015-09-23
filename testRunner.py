"""
Runs all tests that exist in the tests directories.

The class should have a name based on the file's path, like this:
FilenameDirectory -> DefaultTasksModel

for example:
applications/app/tests/controllers/default.py
is
class DefaultController(unittest.TestCase)

BEWARE that the name is NOT in plural (controllers->Controller)

Execute with:
>   python web2py.py -S appname -M -R testRunner.py


02/03/2009
Jon Vlachoyiannis
jon@emotionull.com

REF: http://www.web2pyslices.com/slice/show/1392/unit-testing
"""

import unittest
import glob
import sys
import os
import doctest

suite = unittest.TestSuite()
from copy import copy

test_files = glob.glob('applications/travis_example/tests/*.py')
doc_test_files = glob.glob('applications/travis_example/controllers/*.py')

if not test_files and not doc_test_files:
    raise Exception("No files found for app: travis_example")

# setup web2py environment as true
os.environ["WEB2PY_USE_DB_TESTING"] = "1"

# re-exec db.py to use test database
db_file = 'applications/travis_example/models/db.py'
execfile(db_file, globals())

# Bring all unit tests in and their controllers/models/whatever
for test_file in test_files:
	g = copy(globals())
	execfile(test_file, g)

	# take filename only
	filename = test_file.split('applications/travis_example/tests/')[1]
	# take out extension
	ext = filename[-3:]
	filename = filename[:-3]
	# split filename to be capitalize
	filename_list = filename.split('_')

	to_be_tested_file = ('').join(str.capitalize(x) for x in filename_list) + 'Test'
	controller_file = 'applications/travis_example/controllers/'+filename+ext

	execfile(controller_file, g)

	suite.addTest(unittest.makeSuite(g[to_be_tested_file]))

# db = test_db # Use the test database for all tests

unittest.TextTestRunner(verbosity=2).run(suite)