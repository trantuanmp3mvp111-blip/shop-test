import os
from python_aternos import Client

u = os.getenv('ATERNOS_USER')
p = os.getenv('ATERNOS_PASS')

at = Client()
at.login(u, p)
srv = at.account.servers[0]
srv.start()
print('Started')
