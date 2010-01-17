#!/usr/bin/env python
"""The base User class and example plugin file."""
import hashlib

class Auth():
    def is_logged_in(self):
        user = self.user
        return user is None

    def user(self):
        return User()

    def create_login_url(self, back_url):
        return 'http://www.example.com/login?redirect_to=%s' % back_url

    def create_logout_url(self, back_url):
        return 'http://www.example.com/logout?redirect_to=%s' % back_url

class User():
    def nickname(self):
        return None

    def email(self):
        return None

    def is_admin(self):
        return None

    def user_id(self):
        return None

    def hash_id(self):
        return hashlib.sha1(self.user_id()).hexdigest()

friendly_name = 'User Authentication Plugin'
auth_class = Auth
user_class = User
