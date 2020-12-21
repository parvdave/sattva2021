import imp
import os
import sys
from sattva.wsgi import application

sys.path.insert(0, os.path.dirname(file))

#wsgi = imp.load_source('wsgi', 'passenger_wsgi.py')
#application = wsgi.application