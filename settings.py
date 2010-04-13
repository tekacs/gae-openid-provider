#!/usr/bin/env python
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import users as users_module
import provider

class Configuration(db.Expando):
    user_id = db.StringProperty()

class Home(provider.Handler):
    def get(self):
        self.Render('settings')

class SettingsStorage(provider.Handler):
    pass

class SettingsHandler(provider.Handler):
    pass

url_patterns = [
         ('/settings', Home),
         ('/settings/save/(.*)', SettingsStorage),
         ('/settings/module/(.*)', SettingsHandler),
        ]

def main():
    global users
    application = webapp.WSGIApplication(url_patterns, debug=True)
    users = users_module.UsersAPI()
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
