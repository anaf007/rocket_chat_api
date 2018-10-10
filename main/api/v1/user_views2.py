from flask_restful import Resource
from main.extensions import api

class Hello(Resource):
    """创建用户."""
    def get(self):
        """返回数据.

        .. :quickref: Posts Collection; Get collection of posts.

        **示例请求**:

        .. sourcecode:: http

          GET /posts/ HTTP/1.1
          Host: example.com
          Accept: application/json

        **示例请求**:

        .. sourcecode:: http

          HTTP/1.1 200 OK
          Vary: Accept
          Content-Type: application/json

          [
            {
              "post_id": 12345,
              "author": "/author/123/",
              "tags": ["sphinx", "rst", "flask"],
              "title": "Documenting API in Sphinx with httpdomain",
              "body": "How to..."
            },
            {
              "post_id": 12346,
              "author": "/author/123/",
              "tags": ["python3", "typehints", "annotations"],
              "title": "To typehint or not to typehint that is the question",
              "body": "Static checking in python..."
            }
          ]

        :query sort: sorting order e.g. sort=author,-pub_date
        :query q: full text search query
        :resheader Content-Type: application/json
        :status 200: posts found
        :returns: :class:`myapp.objects.Post`
        """
        return {'hello': 'world'}



        
class CreateUser(Resource):
    """创建用户."""
    




from .version import dev_1
v1 = dev_1
# api.add_resource(Hello, f'/api_{v1}/user/hello') 
api.add_resource(Hello, f'/api_{v1}/user/create') 

