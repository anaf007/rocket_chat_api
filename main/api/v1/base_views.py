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
        
        .. list-table:: 请求信息
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
            None

        """
        try:
            r = rocket.directory('').json()
        except Exception as e:
            
            r = None


        if not r:
            return {'state':'false'},404

        return {'version':r['info']['version'],'state':r['success']},200           


class ShieldSvg(Resource):
    """返回svg"""

    def get(self):
        """https://rocket.chat/docs/developer-guides/rest-api/miscellaneous/shield-svg/

        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/shield.svg
              - 不需要
              - GET

        .. list-table:: 查询参数
            :header-rows: 1

            * - 名称
              - 例子
              - 必要
              - 描述
            * - type
              - online
              - 可选
              - 可以是一个online，user，channel
            * - icon
              - false
              - 可选
              - 
            * - channel
              - general
              - 可选
              - 频道名称
            * - name
              - Rocket.Chat 
              - 可选
              - 要显示的名称

        **示例请求**::

            curl http://localhost:5000/api/v1/bases/shield_svg

        **请求结果**:   
        
            header::

                Content-Type:image/svg+xml;charset=utf-8 

            body::

                None

        """

        return {'state':'false'},404



class Spotlight(Resource):
    """搜索用户可见的用户或房间。"""

    def get(self):
        """https://rocket.chat/docs/developer-guides/rest-api/miscellaneous/spotlight/

        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/shield.svg
              - 需要
              - GET

        .. list-table:: 查询参数
            :header-rows: 1

            * - 名称
              - 例子
              - 必要
              - 描述
            * - query
              - john
              - 需要
              - 要搜索的术语。支持频道'＃'和用户'@'

        **示例请求**::

            curl http://localhost:5000/api/v1/bases/spotlight

        **请求结果**::

            {
                "message": "You must be logged in to do this.",
                "status": "error"
            }  
        """

        try:
            r = rocket.spotlight().json()
        except Exception as e:
            r = None

        pprint(r)
        if not r:
            return {'state':'false'},404

        return {'message':r['message'],'status':r['status']},404



api.add_resource(Info, f'/api/{v1}/bases/info')         
api.add_resource(Directory, f'/api/{v1}/bases/directory')         
api.add_resource(ShieldSvg, f'/api/{v1}/bases/shield_svg')         
api.add_resource(Spotlight, f'/api/{v1}/bases/spotlight')         







