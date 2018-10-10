from flask_restful import Resource
from main.extensions import api

class CreateUser(Resource):
    """创建用户."""
    def get(self):
        """get请求.

        .. :quickref: Posts Collection; Get collection of posts.
        
        **示例请求**:

        .. sourcecode:: http

            GET /posts/ HTTP/1.1
            Host: example.com
            Accept: application/json

        """

        return {'user': 'create'}            



from .version import dev_1
v1 = dev_1
api.add_resource(CreateUser, f'/api_{v1}/user/create')         







