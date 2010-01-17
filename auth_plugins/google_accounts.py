#!/usr/bin/env python
from user import Auth, User
import logging

class Google(Auth):
    """The built-in Google Accounts API authentication method."""
    from google.appengine.api import users

    def __init__(self, config):
        self.config = config
        allow = self.config.get('allowed_users', [])
        self.allowed_users = allow if type(allow) == list else [allow]

    def user(self):
        user = self.users.get_current_user()
        if user is None: return None
        if not user.email() in self.allowed_users:
            logging.error('Blocked disallowed user')
            return None
        return GoogleUser(user, self.users.is_current_user_admin())

    def create_login_url(self, back_url):
        return self.users.create_login_url(back_url)

    def create_logout_url(self, back_url):
        return self.users.create_logout_url(back_url)

class GoogleUser(User):
    """A wrapper around a Google Accounts API user."""
    def __init__(self, google_user, is_admin):
        self.user = google_user
        self.is_admin = is_admin

    def nickname(self):
        if self.user is None:
            return None
        return self.user.nickname()

    def email(self):
        if self.user is None:
            return None
        return self.user.nickname()

    def is_admin(self):
        return self.is_admin

    def user_id(self):
        return self.email()

friendly_name = 'Google Accounts'
auth_class = Google
user_class = GoogleUser
