from flask_restful import Resource
from main.extensions import api,rocket

from flask import request

from .version import dev_1
v1 = dev_1


class Login(Resource):
    """用户登录."""
    def put(self):
        """https://rocket.chat/docs/developer-guides/rest-api/authentication/login/
        
        请求参数:
         - username
         - pwd

        **请求示例**::

            curl http://localhost:5000/api/v1/users/login -d "username=myusername&password=mypassword"
            #or
            from requests import put, get
            result = put(url, data={'username': username,'pwd':pwd})
            print(result.json())

        请求结果：
         - status：success
         - authToken
         - userId

        ::

            {'status': 'success', 'userId': '9wC7Q5QTaetLnQJi6', 'authToken': '-z3B5PP-GFus03GitDjm3YgzauaWhT_irIvi44DUsMc'}

        """
        username = request.form['username']
        pwd = request.form['pwd']

        try:
            r = rocket.login(username,pwd)
        except Exception as e:
            r = None

        if not r:
            return {'state':'false'},401

        r = r.json()   
        state = r['status']  
        userId = r['data']['userId']    
        authToken = r['data']['authToken']    

        return {'status':state,'userId':userId,'authToken':authToken},200           
    

class Me(Resource):
    """返回用户信息"""
    def get(self):
        """https://rocket.chat/docs/developer-guides/rest-api/authentication/me/
        
        需登录

        **请求示例**::

            curl -H "X-Auth-Token: 9HqLlyZOugoStsXCUfD_0YdwnNnunAJF8V47U3QHXSq" -H "X-User-Id: aobEdbYhXfu5hkeqG" http://localhost:5000/api/v1/users/me
            #or
            from requests import put, get
            result = get(url)
            print(result.json())

        请求结果：
         - user_id
         - name
         - emails
         - status
         - statusConnection
         - username
         - active
         - roles
         - success

        """
        try:
            r = rocket.me()
        except Exception as e:
            print(str(e))
            r = None

          

        if not r:
            return {'success':'false','message':'获取个人信息失败，请重新登录。'},401
        
        r = (r.json())          
        return {
            'user_id' : r['_id'],
            'name' : r['name'],
            'emails' : r['emails'],
            'status' : r['status'],
            'statusConnection' : r['statusConnection'],
            'username' : r['username'],
            'active' : r['active'],
            'roles' : r['roles'],
            'success' : r['success']
        },200


        


        

api.add_resource(Login, f'/api/{v1}/users/login')   
api.add_resource(Me, f'/api/{v1}/users/me')   








