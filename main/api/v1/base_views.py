from flask_restful import Resource
from main.extensions import api,rocket
from flask import request

from pprint import pprint

from .version import dev_1
v1 = dev_1


class Info(Resource):
    """返回有关服务器的信息，包括版本信息."""
    def get(self):
        """https://rocket.chat/docs/developer-guides/rest-api/miscellaneous/info/
        
        **示例请求**::

            from requests import get
            result = get(url)

        请求结果:
         - version:版本号
         - state:状态 

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
            return {'state':'false'},401

        return {
          'version':r['info']['version'],
          'state':r['success']
        },200           


class Directory(Resource):
    """查询频道或者用户信息"""

    def get(self):
        """ https://rocket.chat/docs/developer-guides/rest-api/miscellaneous/directory/
        
        需登录
        
        **请求参数**：
         - type:0:channels,1:users
         - text:字符串，需要查询的用户或房间名称

        **示例请求**::

            curl -G -H "X-Auth-Token: ijFlJ1yfidXhwEYY284Anoq_iEsOeMMVCupzNhX22tB" 
              -H "X-User-Id: hw5DThnhQmxDWnavu" 
              -H "Content-type: application/json" 
              http://localhost:5000/api/v1/bases/directory 
              --data-urlencode 'query={"text": "rocket", "type": "users"}'
            #or
            from requests import get
            result = get(url,{"text":'rocket', "type": 1})
        
        请求结果:
         - count
         - offset
         - result
         - success
         - total

        """

        search_type = request.args.get('type',0)
        earch_text = request.args.get('text')

        # if search_type != 'channels' :
        #     return {'state':'false','message':'查询类型有误，请输入正确的查询类型。'},401
        # if search_type != 'users':
        #     return {'state':'false','message':'查询类型有误，请输入正确的查询类型。'},401
        
        if search_type:
            search_type = 'channels'
        else:
            search_type = 'users'

        try:
            r = rocket.directory({"text":earch_text, "type": search_type}).json()
        except Exception as e:
            r = None

        if not r:
            return {'state':'false','message':'查询失败，没有查询到对应的信息。'},401
        
        # if (r['status']=='error'):
        #     return {'state':'false','message':'需要登录'},401
        
        try:
            return {
                'count':r['count'],
                'offset':r['offset'],
                'result':r['result'],
                'success':r['success'],
                'total':r['total'],
            },200
        except Exception as e:
            return {'state':False,'message':'请先登录。'}


        # return {
        #     'count':r['count'],
        #     'offset':r['offset'],
        #     'result':r['result'],
        #     'success':r['success'],
        #     'total':r['total'],
        # },200
        

class ShieldSvg(Resource):
    """返回svg,该插件没有对应的api。"""

    def get(self):
        """https://rocket.chat/docs/developer-guides/rest-api/miscellaneous/shield-svg/

        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/bases/shield_svg
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

        return {'state':False,'message':'端口暂未开放'},401


class Spotlight(Resource):
    """搜索用户可见的用户或房间。"""

    def get(self):
        """https://rocket.chat/docs/developer-guides/rest-api/miscellaneous/spotlight/

        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/bases/spotlight
              - 需要
              - GET

        .. list-table:: 查询参数
            :header-rows: 1

            * - 名称
              - 例子
              - 必要
              - 描述
            * - 类型
              - 0
              - [0,1]
              - 0选项为房间，1为用户
            * - 名称
              - rocket
              - 必填项
              - 

        **示例请求**::

            result = get(url,{'type':1,'text':'users'})

        **请求结果**::

            {
                "users": json,
                "rooms": json,
                "success":string
            }  

        ::

            {
                "users": [
                {
                  "_id": "rocket.cat",
                  "name": "Rocket.Cat",
                  "username": "rocket.cat",
                  "status": "online"
                }
              ],
              "rooms": [],
              "success": true
            }

        """

        search_type = request.args.get('type',0)
        earch_text = request.args.get('text')

        if search_type:
            earch_text = '@'+earch_text
        else:
            earch_text = '#'+earch_text

        try:
            r = rocket.spotlight(earch_text).json()
        except Exception as e:
            r = None

        if not r:
            return {'state':'false','message':'查询失败，没有查询到对应的信息。'},401

        return {
            'users':r['users'],
            'success':r['success'],
            'rooms':r['rooms']
        },200


class Statistics(Resource):
    """统计服务器信息"""
    def get(self):
        """https://rocket.chat/docs/developer-guides/rest-api/miscellaneous/statistics/
        
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/bases/statistics
              - 需要
              - GET

        **示例请求**::

            result = get(url)

        **请求结果**::

            {
                "statistics": json,
                "success":boolean
            } 

        """

        try:
            r = rocket.statistics().json()
        except Exception as e:
            r = None

        if r['success']:
            return {
                'statistics':r['statistics'],
                'success':r['success']
            },200
        else:
            return {
                'success':r['success'],
                'error':r['error'],
                'errorType':r['errorType'],
            },401


class StatisticsList(Resource):
    """服务器统计信息列表。 """

    def get(self):
        """https://rocket.chat/docs/developer-guides/rest-api/miscellaneous/statistics-list/
        
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/bases/statistics_list
              - 需要
              - GET

        .. list-table:: 请求参数
            :header-rows: 1

            * - 名称
              - 例子
              - 必要
              - 描述
            * - query
              - {"_id":"v3D4mvobwfznKozH8"}
              - 需要
              - 需要查询的内容
            * - offset
              - 0
              - 可选
              - 
            * - count
              - 1
              - 可选
              - 
            * - fields
              - {"os":0,"migration":0,"deploy":0,"process":0}
              - 可选
              - 
            * - sort
              - {"_id":1}
              - 可选
              - 

        **示例请求**::

            result = get(url)

        请求结果：
         - statistics：json
         - success:boolean

        """

        try:
            r = rocket.statistics_list().json()
        except Exception as e:
            r = None

        try:
            if r['status'] =='error':
                return {'state':'false','message':'查询失败，请登录。'},401
        except Exception as e:
          pass

        if not r:
            return {'state':'false','message':'查询失败，没有查询到对应的信息。'},401

        return {
            'statistics':r['statistics'],
            'success':r['success']
        },200



api.add_resource(Info, f'/api/{v1}/bases/info')         
api.add_resource(Directory, f'/api/{v1}/bases/directory')         
api.add_resource(ShieldSvg, f'/api/{v1}/bases/shield_svg')         
api.add_resource(Spotlight, f'/api/{v1}/bases/spotlight')         
api.add_resource(Statistics, f'/api/{v1}/bases/statistics')         
api.add_resource(StatisticsList, f'/api/{v1}/bases/statistics_list')         







