from flask_restful import Resource
from main.extensions import api,rocket
from flask import request



class CreateUser(Resource):
    """创建新用户。"""
    def post(self):
        """https://rocket.chat/docs/developer-guides/rest-api/users/create/

        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/user/create
              - 需要auth
              - POST

        .. list-table:: 请求参数
            :header-rows: 1

            * - 名称
              - 示例
              - 必须
            * - email
              - rocket@rocket.com
              - 是
            * - name
              - rocket
              - 是
            * - password
              - rocket@_com
              - 是
            * - username
              - rocket
              - 是
            * - active
              - boolean
              - 默认true
            * - roles
              - ['bot']
              - 默认['user']
            * - joinDefaultChannels
              - false
              - 默认true
            * - requirePasswordChange
              - true
              - 默认false
            * - sendWelcomeEmail
              - true
              - false
            * - verified
              - true
              - false
            * - customFields
              - { twitter: '@example' }
              - 默认undefined

        **示例请求**::

            from requests import put
            data={
                'email': 'rocket@rocket.com',
                'name':'rocket',
                'password':'rocket',
                'username':'rocket',
            }
            result = put(url,data=data)

        请求结果：
         - user:json
         - success:boolean

        ::

            {
               "user": {
                  "_id": "BsNr28znDkG8aeo7W",
                  "createdAt": "2018-10-12T03:53:51.337Z",
                  "services": {
                     "password": {
                        "bcrypt": "$2a$10$5I5nUzqNEs8jKhi7BFS55uFYRf5TE4ErSUH8HymMNAbpMAvsOcl2C"
                     }
                  },
                  "username": "uniqueusername",
                  "emails": [
                     {
                        "address": "email@user.tld",
                        "verified": false
                     }
                  ],
                  "type": "user",
                  "status": "offline",
                  "active": true,
                  "roles": [
                     "user"
                  ],
                  "_updatedAt": "2018-10-12T03:53:51.402Z",
                  "name": "name",
                  "customFields": {
                     "twitter": "@userstwitter"
                  }
               },
               "success": true
            }

        """

        email = request.form['email']
        name = request.form['name']
        password = request.form['password']
        username = request.form['username']
        active = request.form['active']
        roles = request.form['roles']
        joinDefaultChannels = request.form['joinDefaultChannels']
        requirePasswordChange = request.form['requirePasswordChange']
        sendWelcomeEmail = request.form['sendWelcomeEmail']
        verified = request.form['verified']
        customFields = request.form['customFields']

        try:
            r = rocket.users_create(
                email=email,
                name=name,
                password=password,
                username=username,
                active=active,
                roles=roles,
                joinDefaultChannels=joinDefaultChannels,
                requirePasswordChange=requirePasswordChange,
                sendWelcomeEmail=sendWelcomeEmail,
                verified=verified,
                customFields=customFields,
            ).json()
        except Exception as e:
            return {'user':[],'success':false,'message':'创建用户失败，请确认必填项已填写。'}

        return {
            'user': r['users'],
            'success':r['success']
        },200          


class CreateToken(Resource):
    """创建用户身份验证令牌。"""

    def get(self):
        """https://rocket.chat/docs/developer-guides/rest-api/users/createtoken/

        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/user/create_token
              - 需要auth
              - GET

        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 是否必须
              - 描述
            * - username 
              - BsNr28znDkG8aeo7W
              - 必须
              - 输入用户名或者用户ID

        **请求示例**::

            r = rocket.users_create_token(username)
        
        请求结果：
         - userId
         - authToken
         - success

        ::

            {
                "userId": "ZxCPRud4N76RMRLJW",
                "authToken": "H9MvZ_D6obeg13Gj0ANuecBI3pKWTPcTlx4voqV2zt-",
                "success": true
            }
        """
        username = request.args.get('username')
        try:
            r = rocket.users_create_token(username=username)
        except Exception as e:
            r = None
        
        if not r:
            return {'success':False,'message':'查询失败，没有查询到对应的信息。'},401
        
        r = r.json()
        return {
            'userId': r['data']['userId'],
            'authToken': r['data']['authToken'],
            'success':True
        },200  

class Delete(Resource):
    """删除现有用户。"""
    def get(self):
        """https://rocket.chat/docs/developer-guides/rest-api/users/delete/

        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/user/delete
              - 需要auth
              - GET

        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 是否必须
              - 描述
            * - user_id
              - BsNr28znDkG8aeo7W
              - 必须
              - 输入用户ID

        **请求示例**::

            result = get(url,{'user_id':'BsNr28znDkG8aeo7W'})

        请求结果：
         - success
        """

        userid = request.args.get('user_id')
        try:
            r = rocket.users_delete(userid)
        except Exception as e:
            r = None

        if not r:  
            return {'success':False,'message':'删除失败，请输入正确的user_id.'},401

        return {'success':True}
                  

class DeleteOwnAccount(Resource):
    """用户删除自己的帐户。该插件无接口"""
    pass

class ForgotPassword(Resource):
    """重置密码。"""
    def get(self):
        """https://rocket.chat/docs/developer-guides/rest-api/users/forgotpassword/
        
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/user/forgotPassword
              - 不需要
              - GET

        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 是否必须
              - 描述
            * - email
              - rocket@rocket.com
              - 必须
              - 发送密码重置链接到该电子邮件

        **请求示例**::

            result = get(url,{'email':'rocket@rocket.com'})

        请求结果：
         - success
        """
        email = request.args.get('email')
        try:
            r = rocket.users_forgot_password(email)
        except Exception as e:
            r = None

        if not r:  
            return {'success':False,'message':'发送重置密码邮件失败！'},401

        return {'success':True}



class GeneratePersonalAccessToken(Resource):
    """生成个人访问令牌。插件无该接口"""
    pass

class GetAvatar(Resource):
    """获取用户头像的URL。"""
    def get(self):
        """https://rocket.chat/docs/developer-guides/rest-api/users/getavatar/
        
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/user/getAvatar
              - 不需要
              - GET

        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 是否必须
              - 描述
            * - username
              - rocket
              - 必须
              - 输入要显示头像的用户名

        **请求示例**::

            result = get(url,{'username':'rocket'})

        请求结果：
         - result:string url
         - success:boolean

        """

        username = request.args.get('username')
        try:
            r = rocket.users_get_avatar(username=username)
        except Exception as e:
            r = None

        if not r:  
            return {'success':False,'message':'获取头像失败。'},401

        return {
            'success':True,
            'result':r.url,
        }




class GetPersonalAccessTokens(Resource):
    """获取用户的个人访问令牌。插件无该接口"""
    pass

class GetPreferences(Resource):
    """获取用户的所有首选项。

    2018-10-12接口已完成，可能是本机问题环境问题，提示错误，无法取得结果
    
    mac提示：{'success': False, 'error': "Cannot set property 'language' of undefined"}

    """
    def get(self):
        """https://rocket.chat/docs/developer-guides/rest-api/users/get-preferences/
        
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/user/getPreferences
              - 需要auth
              - GET

        
        **请求示例**::

            result = get(url)

        请求结果：
         - preferences:json
         - success:boolean

        ::

            {
                "preferences": {
                    "newRoomNotification": "door",
                    "newMessageNotification": "chime",
                    "muteFocusedConversations": true,
                    "useEmojis": true,
                    "convertAsciiEmoji": true,
                    "saveMobileBandwidth": true,
                    "collapseMediaByDefault": false,
                    "autoImageLoad": true,
                    "emailNotificationMode": "all",
                    "roomsListExhibitionMode": "category",
                    "unreadAlert": true,
                    "notificationsSoundVolume": 100,
                    "desktopNotifications": "default",
                    "mobileNotifications": "default",
                    "enableAutoAway": true,
                    "highlights": [],
                    "desktopNotificationDuration": 0,
                    "viewMode": 0,
                    "hideUsernames": false,
                    "hideRoles": false,
                    "hideAvatars": false,
                    "hideFlexTab": false,
                    "sendOnEnter": "normal",
                    "roomCounterSidebar": false
                },
                "success": true
            }

        """

        try:
            r = rocket.users_get_preferences()
        except Exception as e:
            r = None

        if not r:  
            return {'success':False,'message':'获取失败。'},401

        return {
            'success':True,
            'result':r.json()['preferences'],
        }


class GetPresence(Resource):
    """获取用户的在线状态。"""
    def get(self):
        """https://rocket.chat/docs/developer-guides/rest-api/users/getpresence/
        
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/user/getPresence
              - 需要
              - GET

        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 是否必须
              - 描述
            * - username
              - rocket
              - 必须
              - 输入查询在线的用户的用户名

        **请求示例**::

            result = get(url,{'username':'rocket'})

        请求结果：
         - success:boolean
         - lastLogin
         - presence

        ::

            {
                "success": true,
                "presence": "offline",
                "lastLogin": "2018-10-12T08:37:28.101Z"
            }
        """
        username = request.args.get('username')
        try:
            r = rocket.users_get_presence(username=username)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'查询失败。'},401
        
        r = r.json()
        return {
            'success':True,
            'presence':r['presence'],
            'lastLogin':r['lastLogin'],
        }
        

class GetUsernameSuggestion(Resource):
    """获取用户的建议"""
    pass

class UserInfo(Resource):
    """获取用户的信息，仅限于调用者的权限。"""
    pass

class UserList(Resource):
    """所有用户及其信息，仅限于权限。"""
    pass

class RegeneratePersonalAccessToken(Resource):
    """重新生成用户个人访问令牌。"""
    pass

class Register(Resource):
    """注册新用户。"""
    pass 

class RemovePersonalAccessToken(Resource):
    """删除个人访问令牌。"""
    pass

class ResetAvatar(Resource):
    """重置用户的头像"""
    pass

class SetAvatar(Resource):
    """设置用户的头像"""
    pass

class SetPreferences(Resource):
    """设置用户的首选项"""
    pass

class Update(Resource):
    """更新现有用户。"""
    pass

class UpdateOwnBasicInfo(Resource):
    """更新自己用户的基本信息。"""
    pass




from .version import dev_1
v1 = dev_1
api.add_resource(CreateUser, f'/api/{v1}/user/create')         
api.add_resource(CreateToken, f'/api/{v1}/user/create_token')         
api.add_resource(Delete, f'/api/{v1}/user/delete')         
api.add_resource(DeleteOwnAccount, f'/api/{v1}/user/deleteOwnAccount')         
api.add_resource(ForgotPassword, f'/api/{v1}/user/forgotPassword')         
api.add_resource(GetAvatar, f'/api/{v1}/user/getAvatar')         
api.add_resource(GetPreferences, f'/api/{v1}/user/getPreferences')         
api.add_resource(GetPresence, f'/api/{v1}/user/getPresence')         







