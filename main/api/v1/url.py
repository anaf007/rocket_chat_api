from main.extensions import api

from .views import *

from .version import dev_1

v1 = dev_1

api.add_resource(HelloWorld, f'/api_{v1}/hello')
