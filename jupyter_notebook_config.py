import os
from jupyter_server.auth import passwd

if not os.path.exists('notebooks'):
    os.makedirs('notebooks')

c.ServerApp.ip = '0.0.0.0'
c.ServerApp.allow_origin = '*'
c.ServerApp.open_browser = False
c.ServerApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors 'self' https://replit.com"
    }
}
c.ServerApp.root_dir = "notebooks"
hashed_password = os.environ.get('NOTEBOOK_PASSWORD_HASH')
if not hashed_password:
    hashed_password = passwd('replit')
c.PasswordIdentityProvider.hashed_password = hashed_password
