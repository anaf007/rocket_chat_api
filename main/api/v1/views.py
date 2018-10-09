from flask_restful import Resource

class HelloWorld(Resource):
    """Posts collection."""
    def get(self):
        """返回数据.

        .. :quickref: Posts Collection; Get collection of posts.

        **Example request**:

        .. sourcecode:: http

          GET /posts/ HTTP/1.1
          Host: example.com
          Accept: application/json

        **Example response**:

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