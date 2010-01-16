#!/usr/bin/env python
"""
A simple users API, simply to abstract authentication from the
built-in API. This is to allow authentication methods other than
the Google Accounts system.
"""

import os.path
import yaml
import logging

def load_yaml(filename):
    try:
        contents = yaml.load(open(filename).read())
    except:
        contents = None
    if type(contents) == dict:
        return contents
    else:
        return {}

class UsersAPI():
    def __init__(self):
        self.config = load_yaml('auth.yaml')
        (self.plugin, self.plugin_config) = self.load_plugin()
        self.auth = self.load_auth()

    def load_plugin(self):
        plugin_name = self.config.get('auth_plugin', 'google')
        if type(plugin_name) != str:
            return (None, None)
        try:
            plugin = __import__('auth_plugins.' + plugin_name)
            plugin = getattr(plugin, plugin_name)
            logging.info('Loaded auth plugin successfully.')
        except ImportError:
            logging.info('Failed to load auth plugin!')
            return (None, None)
        plugin_config = self.config.get(plugin_name, {})
        if type(plugin_config) != dict:
            plugin_config = {} # Kill config if not a dict.
        return (plugin, plugin_config)

    def load_auth(self):
        if self.plugin is None:
            return None
        try:
            return self.plugin.auth_class(self.plugin_config)
        except AttributeError:
            return None

    def get_current_user(self):
        if self.auth is None: return None
        return self.auth.user()

    def create_login_url(self, back_url):
        if self.auth is None: return back_url
        return self.auth.create_login_url(back_url)

    def create_logout_url(self, back_url):
        if self.auth is None: return back_url
        return self.auth.create_logout_url(back_url)
