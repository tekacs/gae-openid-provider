This is a fully functioning OpenID provider, modified from the below, which was
itself modified from Google's own example OpenID provider application.

The modifications centre around extracting authentication out into 'plugins',
rather than remaining tied-into Google Accounts authentication as in the
original system. As such, authentication methods other than Google Accounts
can be used to verify the identity of OpenID users.

The default authentication method used in this provider is Google Accounts,
with an on-disk list of allowed users, restricting the use of the system to
those users permitted by administrators. This is to be expanded to an in-DB
list of allowed users, with an admin interface to add and remove users. The
current behaviour in the face of a disallowed user is to drop the user's
session, without displaying an error message. This is to be expanded to
provide a message to the user, denying access.

Source:

Based on http://openid-provider.appspot.com/ sources, ported to latest
python-openid library, version 2.1.1 (included).

An OpenID Provider app for Google App Engine. Allows Google users to log into
OpenID servers using their Google Account
(either regular Google Accounts or Google Apps Accounts, according to
appengine authentication settings)

For more about OpenID, see:
  http://openid.net/
  http://openid.net/about.bml
