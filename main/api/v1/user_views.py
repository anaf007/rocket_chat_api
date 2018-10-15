from flask_restful import Resource
from main.extensions import api,rocket
from flask import request
from pprint import pprint


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

            r = get(url,{'username':username})
        
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

        return {'success':True},200
                  

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

        return {'success':True},200


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
        },200


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
        },200


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
        },200
        

class GetUsernameSuggestion(Resource):
    """获取用户的建议.插件无该接口"""
    pass

class UserInfo(Resource):
    """获取用户的信息，仅限于调用者的权限。"""
    def get(self):
        """https://rocket.chat/docs/developer-guides/rest-api/users/info/
        
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/user/info
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
         - id
         - type
         - status
         - active
         - name
         - username
         - success

        ::

            {
                "success": true,
                "id": "uEi6WLYAP5aeiFWKu",
                "type": "user",
                "status": "offline",
                "active": true,
                "name": "rocket",
                "username": "rocket"
            }
        
        """
        username = request.args.get('username')
        try:
            r = rocket.users_info(username=username)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'查询用户信息失败。'},401
        
        r = r.json()
        return {
            'success':True,
            'id':r['user']['_id'],
            'type':r['user']['type'],
            'status':r['user']['status'],
            'active':r['user']['active'],
            'name':r['user']['name'],
            'username':r['user']['username']
        },200



class UserList(Resource):
    """所有用户及其信息，仅限于权限。此处管理员和普通用户登录返回的user结果有差别"""
    def get(self):
        """https://rocket.chat/docs/developer-guides/rest-api/users/list/
        
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/user/list
              - 需要
              - GET

        **请求示例**::

            result = get(url)

        请求结果：
         - success
         - count
         - offset
         - total
         - users:json
         - username

        ::

            {
                "success": true,
                "count": 5,
                "offset": 0,
                "total": 5,
                "users": [{...},{...}...]
            }
        
        """
        try:
            r = rocket.users_list()
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'查询用户信息失败。'},401
        
        r = r.json()
        return {
            'success':True,
            'count':r['count'],
            'offset':r['offset'],
            'total':r['total'],
            'users':r['users']
        },200


class RegeneratePersonalAccessToken(Resource):
    """重新生成用户个人访问令牌。插件无该接口"""
    pass

class Register(Resource):
    """注册新用户。"""
    def put(self):
        """https://rocket.chat/docs/developer-guides/rest-api/users/register/

        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/user/register
              - 需要
              - PUT

        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 是否必须
              - 描述
            * - username
              - rogersmith
              - 必须且唯一
              - 输入要注册的用户名
            * - email
              - roger@example.com
              - 必须且唯一
              - 输入要注册的邮箱
            * - pwd
              - passw0rd
              - 必须
              - 输入注册用户密码
            * - name
              - Roger Smith
              - 必须
              - 输入要注册的姓名

        **请求示例**::

            result = put(url,data={'username': username,'email':email,'pwd':pwd,'name':name})

        请求结果：
         - success:boolean
         - user:json

        ::

            {
                "success": true,
                "users": {...}
            }

        """ 
        username = request.form['username']
        email = request.form['email']
        name = request.form['username']
        pwd = request.form['pwd']

        try:
            r = rocket.users_register(
                    email=email,
                    username=username,
                    name=name,
                    password=pwd,
                )
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'注册用户失败。'},401
        
        r = r.json()
        return {
            'success':True,
            'user':r['user']
        },200


class RemovePersonalAccessToken(Resource):
    """删除个人访问令牌。插件无该接口"""
    pass

class ResetAvatar(Resource):
    """重置用户的头像."""
    def get(self):
        """https://rocket.chat/docs/developer-guides/rest-api/users/resetavatar/
        
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/user/resetAvatar
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
              - 输入要重置头像的用户名

        **请求示例**::

            result = get(url,{'username':'rocket'})

        请求结果：
         - success:boolean
        """

        username =request.args.get('username')
        try:
            r = rocket.users_reset_avatar(username=username)
        except Exception as e:
            r = None

        if not r:  
            return {'success':False,'message':'重置头像失败。'},401

        return {
            'success':True,
        },200


class SetAvatar(Resource):
    """设置用户的头像。"""
    def put(self):
        """https://rocket.chat/docs/developer-guides/rest-api/users/setavatar/
        
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/user/setAvatar
              - 需要
              - PUT

        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 是否必须
            * - avatarUrl
              - http://domain.tld/to/my/own/avatar.jpg
              - 必须,一个图像地址，并非文件

        **请求示例**::

            result = get(url,{'username':'rocket','avatarUrl':avatarUrl})

        请求结果：
         - success:boolean

        """
        url = request.form['avatarUrl']

        try:
            r = rocket.users_set_avatar(url)
        except Exception as e:
            r = None

        if not r:
            return {'state':'false','message':'设置头像失败。'},401

        return {
            'success':True,
        },200


class SetPreferences(Resource):
    """设置用户的首选项."""
    def put(self):
        """https://rocket.chat/docs/developer-guides/rest-api/users/set-preferences/
        
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/user/set_preferences
              - 需要
              - PUT

        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 是否必须
              - 描述
            * - userId
              - BsNr28znDkG8aeo7W
              - 必须
              - 用户的id
            * - newRoomNotification
              - test
              - 必须
              - 新房间的通知
            * - newMessageNotification
              - test
              - 必须
              - 新消息的通知
            * - useEmojis
              - true
              - 必须
              - 是否可用Emojis表情
            * - convertAsciiEmoji
              - true
              - 必须
              - 转换为ASCII码emoji表情
            * - saveMobileBandwidth
              - true
              - 必须
              - 保存为手机的速度
            * - collapseMediaByDefault
              - true
              - 必须
              - 收起媒体文件
            * - autoImageLoad
              - true
              - 必须
              - 图像自动加载
            * - emailNotificationMode
              - test
              - 必须
              - 邮件通知模式
            * - roomsListExhibitionMode
              - test
              - 必须
              - 房间列表展示模式
            * - unreadAlert
              - true
              - 必须
              - 未读信息的提示
            * - notificationsSoundVolume
              - 100
              - 必须
              - 消息通知的音量
            * - desktopNotifications
              - test
              - 必须
              - 桌面通知
            * - mobileNotifications
              - test
              - 必须
              - 手机通知
            * - enableAutoAway
              - true
              - 必须
              - 用启用自动离线功能
            * - highlights
              - []
              - 必须
              - 
            * - desktopNotificationDuration
              - 100
              - 必须
              - 桌面通知持续时间
            * - viewMode
              - 0
              - 必须
              - 显示模式
            * - hideUsernames
              - false
              - 必须
              - 是否隐藏用户名
            * - hideRoles
              - false
              - 必须
              - 是否隐藏用户角色
            * - hideAvatars
              - false
              - 必须
              - 是否隐藏用户头像
            * - sendOnEnter
              - test
              - 必须
              - 设置回车发送信息
            * - roomCounterSidebar
              - true
              - 必须
              - 显示房间侧边计数器
            * - language
              - pt-BR
              - 必须
              - 语言
            * - sidebarShowFavorites
              - true
              - 可选
              - 显示侧边收藏夹
            * - sidebarShowUnread
              - true
              - 可选
              - 显示侧边未读信息
            * - sidebarSortby
              - test
              - 可选
              - 显示排序
            * - sidebarViewMode
              - test
              - 可选
              - 显示查看模式
            * - sidebarHideAvatar
              - true
              - 可选
              - 侧边栏隐藏头像
            * - groupByType
              - true
              - 可选
              - 按类型分组
            * - muteFocusedConversations
              - true
              - 可选
              - 用户的id

        **请求示例**::

            result = get(url,{'user_id':'BsNr28znDkG8aeo7W',data={...}})

        请求结果：
         - success:boolean
         - preferences:json

        """
        userId = request.form['userId']
        setData = {
            'newRoomNotification':request.form['newRoomNotification'],
            'newMessageNotification':request.form['newMessageNotification'],
            'useEmojis':request.form['useEmojis'],
            'convertAsciiEmoji':request.form['convertAsciiEmoji'],
            'saveMobileBandwidth':request.form['saveMobileBandwidth'],
            'collapseMediaByDefault':request.form['collapseMediaByDefault'],
            'autoImageLoad':request.form['autoImageLoad'],
            'emailNotificationMode':request.form['emailNotificationMode'],
            'roomsListExhibitionMode':request.form['roomsListExhibitionMode'],
            'unreadAlert':request.form['unreadAlert'],
            'notificationsSoundVolume':request.form['notificationsSoundVolume'],
            'mobileNotifications':request.form['mobileNotifications'],
            'enableAutoAway':request.form['enableAutoAway'],
            'highlights':request.form['highlights'],
            'desktopNotificationDuration':request.form['desktopNotificationDuration'],
            'viewMode':request.form['viewMode'],
            'hideUsernames':request.form['hideUsernames'],
            'hideRoles':request.form['hideRoles'],
            'hideAvatars':request.form['hideAvatars'],
            'sendOnEnter':request.form['sendOnEnter'],
            'roomCounterSidebar':request.form['roomCounterSidebar'],
            'language':request.form['language'],
            'sidebarShowFavorites':request.form['sidebarShowFavorites'],
            'sidebarShowUnread':request.form['sidebarShowUnread'],
            'sidebarSortby':request.form['sidebarSortby'],
            'sidebarViewMode':request.form['sidebarViewMode'],
            'sidebarHideAvatar':request.form['sidebarHideAvatar'],
            'groupByType':request.form['groupByType'],
            'muteFocusedConversations':request.form['muteFocusedConversations'],
        }
        try:
            r = rocket.users_set_preferences(user_id=userId,data=setData)
        except Exception as e:
            r = None

        if not r:
            return {'state':'false','message':'设置用户首选项失败，请检查输入的参数。'},401

        return {
            'success':True,
            'preferences':r.json()['preferences']
        },200



class Update(Resource):
    """更新现有用户."""
    def put(self):
        """https://rocket.chat/docs/developer-guides/rest-api/users/update/

        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/user/update
              - 需要
              - PUT

        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 是否必须
              - 描述
            * - userId
              - BsNr28znDkG8aeo7W
              - 必须
              - 输入要更新的用户id
            * - email
              - example@example.com
              - 可选的
              - 用户的电子邮件地址
            * - name
              - Example User
              - 可选的
              - 用户的显示名称
            * - password
              - pass@w0rd
              - 可选的
              - 用户的密码
            * - username
              - example
              - 可选的
              - 用户的用户名
            * - active
              - false
              - 可选 默认值：true
              - 是否可登陆
            * - roles
              - ['bot']
              - 可选 默认值：['user']
              - 用户为其分配的角色。
            * - joinDefaultChannels
              - false
              - 可选 默认值：true
              - 用户是否应加入默认频道。
            * - requirePasswordChange
              - true
              - 可选 默认值：false
              - 是否要求用户在登录时更改密码
            * - sendWelcomeEmail
              - true
              - 可选 默认值：false
              - 用户应该收到欢迎电子邮件吗？
            * - verified
              - true
              - 可选 默认值：false
              - 是否应该验证用户的电子邮件地址？
            * - customFields
              - { twitter: '@example' }
              - 可选 默认值：undefined
              - 用户应在其帐户中拥有的任何自定义字段。

        **请求示例**::

            result = put(url,{'userId':'rocket',data={...}})

        请求结果：
         - success:boolean
         - user:json

        """
        userId = request.form['userId']
        updateData = {
            'email':request.form['email'],
            'name':request.form['name'],
            'password':request.form['password'],
            'username':request.form['username'],
            'active':request.form['active'],
            'roles':request.form['roles'],
            'joinDefaultChannels':request.form['joinDefaultChannels'],
            'requirePasswordChange':request.form['requirePasswordChange'],
            'sendWelcomeEmail':request.form['sendWelcomeEmail'],
            'verified':request.form['verified'],
            'customFields':request.form['customFields'],
        }

        try:
            r = rocket.users_update(user_id=userId,data=updateData)
        except Exception as e:
            r = None

        if not r:
            return {'state':'false','message':'更新用户信息失败，请检查输入的参数是否正确。'},401

        return {
            'success':True,
            'user':r.json()['user']
        },200


class UpdateOwnBasicInfo(Resource):
    """更新自己用户的基本信息。插件无该接口"""
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
api.add_resource(UserInfo, f'/api/{v1}/user/info')         
api.add_resource(UserList, f'/api/{v1}/user/list')         
api.add_resource(Register, f'/api/{v1}/user/register')         
api.add_resource(ResetAvatar, f'/api/{v1}/user/resetAvatar')         
api.add_resource(SetAvatar, f'/api/{v1}/user/setAvatar')         
api.add_resource(SetPreferences, f'/api/{v1}/user/set_preferences')         
api.add_resource(Update, f'/api/{v1}/user/update')         







