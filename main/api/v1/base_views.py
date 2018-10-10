from flask_restful import Resource
from main.extensions import api,rocket

from pprint import pprint


from .version import dev_1
v1 = dev_1


class Info(Resource):
    """返回有关服务器的信息，包括版本信息."""
    def get(self):
        """https://rocket.chat/docs/developer-guides/rest-api/miscellaneous/info/
        
        **示例请求**::

            curl http://localhost:5000/api/v1/bases/info

        返回:
         - version:版本号
         - state:状态 success false 

        ::

            {
                "version": "0.71.0-develop",
                "state": true
            }

        """

        try:
            r = rocket.info().json()
        except Exception as e:
            r = None

        if not r:
            return {'state':'false'},404

        return {'version':r['info']['version'],'state':r['success']},200           



class Directory(Resource):
    """用于在服务器上可用的所有用户和频道上按用户或频道进行搜索。"""

    def get(self):
        """ https://rocket.chat/docs/developer-guides/rest-api/miscellaneous/directory/
        
        .. list-table:: 基本请求
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/directory
              - 需要
              - GET

        **示例请求**::

            curl http://localhost:5000/api/v1/bases/directory

        返回:
         - version:版本号
         - state:状态 success false 

        ::

            {
                "version": "0.71.0-develop",
                "state": true
            }
        """
        try:
            r = rocket.directory('').json()
        except Exception as e:
            print(str(e))
            r = None

        pprint(r)

        if not r:
            return {'state':'false'},404

        return {'version':r['info']['version'],'state':r['success']},200           




api.add_resource(Info, f'/api/{v1}/bases/info')         
api.add_resource(Directory, f'/api/{v1}/bases/directory')         







