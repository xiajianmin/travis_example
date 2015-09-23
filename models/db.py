# original construction for db
db = DAL('sqlite://testing.sqlite')

#DAL.define_table
import datetime
import time
import os

if os.getenv('WEB2PY_USE_DB_TESTING'):
	print "\n\n USING TEST DATABASE \n\n"
	db = DAL('mysql://root:@127.0.0.1/testdb', lazy_tables=False, migrate=False)

from gluon.custom_import import track_changes
track_changes(True)

from gluon.tools import *
auth = Auth(db)
# from custom_validators import PASSWORD
# from helper import check_password_expires, delete_extra_user_sessions
# from user_helper import get_user_fullname
# from collections import OrderedDict

## if user's timezone is set, alter request.now to be the user's local time
is_timezone_unknown = (session.user_timezone is None)
user_timezone = session.user_timezone or 'UTC'
if not is_timezone_unknown:
  from pytz import utc, timezone
  request.now = utc.localize(request.utcnow, is_dst=None).astimezone(timezone(session.user_timezone)).replace(tzinfo=None)

## configure email
from gluon.tools import Mail
mail = Mail()
# mail = auth.settings.mailer
mail.settings.server = 'smtp.gmail.com:587'
auth.settings.mailer = mail

db.define_table('person',
	Field('first_name'),
	Field('middle_initial'),
	Field('last_name'),
	Field('dob', 'date'),
	Field('sex'),
	Field('race'),
	Field('height'),
	Field('weight'),
	Field('address'),
	Field('city'),
	Field('state'),
	Field('zip')
	)