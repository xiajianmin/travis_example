import unittest
import json
from gluon.globals import Request, Session, Storage, Response

import cPickle as pickle

class PersonTest(unittest.TestCase):
	def __init__(self, p):
		print ("\n === INIT TEST ===\n")
		global auth, session, request
		unittest.TestCase.__init__(self, p)

		os.environ["WEB2PY_USE_DB_TESTING"]= "1"

		self.session = pickle.dumps(session)
		request.application = 'travis_example'
		request.controller = "person"
		self.request = request

		print ("\n === INIT TEST END ===\n")

	def setUp(self):
		print ("\n === SETUP TEST ===\n")
		global response, session, request, auth
		session = pickle.loads(self.session)
		request = self.request

		auth = Auth(globals(), db)
		auth.define_tables()

		print ("\n === SETUP TEST END ===\n")

	def testShowPerson(self):
		print ("\n === START TEST SHOW PERSON ===\n")

		request.args = [1]

		request.function = 'show'
		resp = show()

		print resp

		print ("\n === END TEST SHOW PERSON ===\n")

	def testAddPerson(self):
		print ("\n === START TEST ADD PERSON ===\n")

		request.function = 'get_person_count'
		resp = get_person_count()

		print ('count: ' + str(resp))

		new_person = {'first_name': 'JANE',
		'last_name': 'DOE',
		'dob': '1980-05-12'
		}

		request.vars.new_person = json.dumps(new_person)

		request.function = 'add_person'
		resp = add_person()

		print resp # should be 2

		request.function = 'get_person_count'
		resp = get_person_count()

		print ('count: ' + str(resp))

		print ("\n === END TEST ADD PERSON ===\n")

	def testEditPerson(self):
		print ("\n === START TEST EDIT PERSON ===\n")

		# request.function = 'edit_person'
		# resp = edit_person()

		print ("\n === END TEST EDIT PERSON ===\n")

	def testDeletePerson(self):
		print ("\n === START TEST DELETE PERSON ===\n")

		request.vars.person_id = 2

		request.function = 'delete_person'
		resp = delete_person()

		print resp

		request.function = 'get_person_count'
		resp = get_person_count()

		print ('count: ' + str(resp))

		print ("\n === END TEST DELETE PERSON ===\n")