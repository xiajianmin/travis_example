import json

def show():
	person_id = request.args[0]

	person = db(db.person.id == person_id).select()
	return locals()

def add_person():
	r = request.vars

	new_person = json.loads(r.new_person)

	res = db.person.insert(**new_person)
	return res;

def edit_person():
	r = request.vars

	edited_person_data = json.loads(r.edited_data)
	res = db(db.person.id == r.person_id).update(**edited_person_data)

	return res;

def delete_person():
	r = request.vars

	res = db(db.person.id == r.person_id).delete()
	return res;

def get_person_count():

	res = db(db.person.id > 0).select(db.person.id)

	return len(res)