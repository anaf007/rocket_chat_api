#coding=utf-8
from flask_restful import Resource
from main.extensions import api,rocket
from flask import request

from .version import dev_1
v1 = dev_1



class GroupsArchive(Resource):
    """保存该聊天群组
    
    https://rocket.chat/docs/developer-guides/rest-api/groups/archive/
    """
    def get(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/groups/groupArchive
              - 需要auth
              - GET
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - HyehQjC44FwMeiLbX
              - 必须
              - 要保存的频道id

        **请求示例**::

            r = get(url,data={'roomId':'7aDSXtjMA3KPLxLjt'})

        **请求结果**:
         - success:boolean

        """ 
        roomId = request.form['roomId']
        
        try:
            r = rocket.groups_archive(room_id=roomId)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'操作失败。'},401

        return {
            'success':True
        },200


class GroupsClose(Resource):
    """关闭群组

    https://rocket.chat/docs/developer-guides/rest-api/groups/close/
    """
    def get(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/groups/close
              - 需要auth
              - GET
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - HyehQjC44FwMeiLbX
              - 必须
              - 要关闭的群组id

        **请求示例**::

            r = get(url,data={'roomId':'7aDSXtjMA3KPLxLjt'})

        **请求结果**:
         - success:boolean

        """ 
        roomId = request.form['roomId']
        
        try:
            r = rocket.groups_close(room_id=roomId)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'关闭失败。'},401

        return {
            'success':True
        },200


class Counters(Resource):
    """获取群组计数。 插件无该接口
    https://rocket.chat/docs/developer-guides/rest-api/groups/counters/
    
    """


class GroupsCreate(Resource):
    """创建群组
    https://rocket.chat/docs/developer-guides/rest-api/groups/create/

    """

    def put(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/channels/create
              - 需要auth
              - PUT
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - name
              - testing
              - 必须
              - 群组名称
            * - members
              - "rocket.cat,admin"
              - 默认为''
              - 创建时要添加的用户列表用,号隔开
            * - readOnly
              - 1
              - 默认0
              - 设置频道是否只读

        **请求示例**::

            r = put(url,data={'name':'testing','members':"rocket.cat,admin",readOnly:1})

        **请求结果**:
         - success:boolean
         - channel:json

        ::

            {
              "group": {
                "_id": "NtR6RQ7NvzA9ejecX",
                "name": "testing",
                "t": "p",
                "usernames": [
                  "tester"
                ],
                "msgs": 0,
                "u": {
                  "_id": "aobEdbYhXfu5hkeqG",
                  "username": "tester"
                },
                "ts": "2016-12-09T16:53:06.761Z",
                "ro": false,
                "sysMes": true,
                "_updatedAt": "2016-12-09T16:53:06.761Z"
              },
              "success": true
            }
        """ 
        name = request.form['name']
        members = request.form['members']
        readOnly = request.form['readOnly']

        members = members.split(',')
        if readOnly:
            readOnly = True
        else:
            readOnly = False 

        try:
            r = rocket.groups_create(name=name,members=members,readOnly=readOnly)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'创建失败。'},401

        return {
            'group':r.json()['group'],
            'success':True
        }


class GroupsDelete(Resource):
    """ 删除群组
    https://rocket.chat/docs/developer-guides/rest-api/groups/delete/
    """
    def get(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/groups/delete
              - 需要auth
              - GET
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - HyehQjC44FwMeiLbX
              - 必须
              - 要删除的群组id

        **请求示例**::

            r = get(url,data={'roomId':'7aDSXtjMA3KPLxLjt'})

        **请求结果**:
         - success:boolean
         - group:json

        ::

            {
               "group": {
                  "_id": "ByehQjC44FwMeiLbX",
                  "name": "groupname",
                  "t": "c",
                  "usernames": [
                     "example"
                  ],
                  "msgs": 0,
                  "u": {
                     "_id": "aobEdbYhXfu5hkeqG",
                     "username": "example"
                  },
                  "ts": "2016-05-30T13:42:25.304Z"
               },
               "success": true
            }

        """ 
        roomId = request.form['roomId']
        
        try:
            r = rocket.groups_delete(room_id=roomId)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'关闭失败。'},401

        return {
            'success':True,
            'group':r.json()['group'],
        },200

    
class GroupsFiles(Resource):
    """获取私有组中的文件列表。
    https://rocket.chat/docs/developer-guides/rest-api/groups/files/

    """
    def get(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/groups/groupFile
              - 需要auth
              - GET
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - HyehQjC44FwMeiLbX
              - 必须
              - 要获取的群组id

        **请求示例**::

            r = get(url,data={'roomId':'7aDSXtjMA3KPLxLjt'})

        **请求结果**:
         - success:boolean
         - files:json
         - count:int
         - offset:int
         - total:int

        ::

            {
                "files": [
                    {
                        "_id": "S78TNnvaWGwdYRaCD",
                        "name": "images.jpeg",
                        "size": 9778,
                        "type": "image/jpeg",
                        "rid": "GENERAL",
                        "description": "",
                        "store": "GridFS:Uploads",
                        "complete": true,
                        "uploading": false,
                        "extension": "jpeg",
                        "progress": 1,
                        "user": {
                            "_id": "ksKsKmrjvxzkzxkww",
                            "username": "rocket.cat",
                            "name": "Rocket Cat"
                        },
                        "_updatedAt": "2018-03-08T14:47:37.003Z",
                        "instanceId": "uZG54xuoKauKHykbQ",
                        "etag": "jPaviS9qG22xC5sDC",
                        "path": "/ufs/GridFS:Uploads/S78TNnvaWGwdYRaCD/images.jpeg",
                        "token": "28cAb868d9",
                        "uploadedAt": "2018-03-08T14:47:37.295Z",
                        "url": "/ufs/GridFS:Uploads/S78TNnvaWGwdYRaCD/images.jpeg"
                    }
                ],
                "count": 1,
                "offset": 0,
                "total": 1,
                "success": true
            }

        """ 
        roomId = request.form['roomId']
        
        try:
            r = rocket.groups_files(room_id=roomId)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'获取失败。'},401

        return {
            'success':True,
            'group':r.json()['group'],
        },200

    
class GroupsHistory(Resource):
    """ 检索历史消息
    https://rocket.chat/docs/developer-guides/rest-api/groups/history/

    """
    def put(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/groups/history
              - 需要auth
              - PUT
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - HyehQjC44FwMeiLbX
              - 必须
              - 要获取的群组id
            * - latest
              - 2018-10-19T14:42:25.304Z
              - 默认为现在
              - 获取的时间范围
            * - oldest
              - 2018-10-19T14:42:25.304Z
              - 默认空
              - 
            * - inclusive
              - 1
              - 0
              - 是否包含最新/旧信息
            * - count
              - 100
              - 默认20
              - 消息数量
            * - unreads
              - 0
              - 默认0 
              - 是否包含未读数量

        **请求示例**::

            data = {
                'roomId':'7aDSXtjMA3KPLxLjt',
                'latest':'',
                'oldest':'',
                'inclusive':1,
                'count':'',
                'unreads':0,
            }

            r = get(url,data=data)

        **请求结果**::
        
            {
                  "messages": [
                    {
                      "_id": "AkzpHAvZpdnuchw2a",
                      "rid": "ByehQjC44FwMeiLbX",
                      "msg": "hi",
                      "ts": "2016-12-09T12:50:51.555Z",
                      "u": {
                        "_id": "y65tAmHs93aDChMWu",
                        "username": "testing"
                      },
                      "_updatedAt": "2016-12-09T12:50:51.562Z"
                    },
                    {
                      "_id": "vkLMxcctR4MuTxreF",
                      "t": "uj",
                      "rid": "ByehQjC44FwMeiLbX",
                      "ts": "2016-12-08T15:41:37.730Z",
                      "msg": "testing2",
                      "u": {
                        "_id": "bRtgdhzM6PD9F8pSx",
                        "username": "testing2"
                      },
                      "groupable": false,
                      "_updatedAt": "2016-12-08T16:03:25.235Z"
                    },
                    {
                      "_id": "bfRW658nEyEBg75rc",
                      "t": "uj",
                      "rid": "ByehQjC44FwMeiLbX",
                      "ts": "2016-12-07T15:47:49.099Z",
                      "msg": "testing",
                      "u": {
                        "_id": "nSYqWzZ4GsKTX4dyK",
                        "username": "testing1"
                      },
                      "groupable": false,
                      "_updatedAt": "2016-12-07T15:47:49.099Z"
                    },
                    {
                      "_id": "pbuFiGadhRZTKouhB",
                      "t": "uj",
                      "rid": "ByehQjC44FwMeiLbX",
                      "ts": "2016-12-06T17:57:38.635Z",
                      "msg": "testing",
                      "u": {
                        "_id": "y65tAmHs93aDChMWu",
                        "username": "testing"
                      },
                      "groupable": false,
                      "_updatedAt": "2016-12-06T17:57:38.635Z"
                    }
                  ],
                  "success": true
            }

        """ 
        roomId = request.form['roomId']
        latest = request.form['latest']
        oldest = request.form['oldest']
        inclusive = request.form['inclusive']
        count = request.form['count']
        unreads = request.form['unreads']

        if inclusive:
            inclusive = True
        else:
            inclusive = False
        if count:
            count = int(count)
        else:
            count = 20
        if unreads:
            unreads = True
        else:
            unreads = False

        try:
            r = rocket.groups_history(
                room_id=roomId,
                latest=latest,
                oldest=oldest,
                inclusive=inclusive,
                count=count,
                unreads=unreads,
            )
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'查询失败。'},401

        return {
            'success':True,
            'messages':r.json()['messages'],
        },200


class GroupsInfo(Resource):
    """获取群组信息
    https://rocket.chat/docs/developer-guides/rest-api/groups/info/
    """
    def get(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/groups/info
              - 需要auth
              - GET
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - HyehQjC44FwMeiLbX
              - 必须
              - 要关闭的群组id

        **请求示例**::

            r = get(url,data={'roomId':'7aDSXtjMA3KPLxLjt'})

        **请求结果**::

            {
                  "group": {
                    "_id": "ByehQjC44FwMeiLbX",
                    "ts": "2016-11-30T21:23:04.737Z",
                    "t": "p",
                    "name": "testing",
                    "usernames": [
                      "testing",
                      "testing1"
                    ],
                    "u": {
                        "_id": "aobEdbYhXfu5hkeqG",
                        "username": "testing1"
                    },
                    "msgs": 1,
                    "default": true,
                    "_updatedAt": "2016-12-09T12:50:51.575Z",
                    "lm": "2016-12-09T12:50:51.555Z"
                  },
                  "success": true
                }

        """ 
        roomId = request.form['roomId']
        
        try:
            r = rocket.groups_info(room_id=roomId)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'获取失败。'},401

        return {
            'success':True,
            'group':r.json()['group'],
        },200


class GroupsInvite(Resource):
    """将用户添加到私有组
    https://rocket.chat/docs/developer-guides/rest-api/groups/invite/

    """
    def put(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/groups/invite
              - 需要auth
              - PUT
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - HyehQjC44FwMeiLbX
              - 必须
              - 要关闭的群组id
            * - userId
              - nSYqWzZ4GsKTX4dyK
              - 必须
              - 用户id

        **请求示例**::

            data = {
                'roomId':'7aDSXtjMA3KPLxLjt',
                'userId':'nSYqWzZ4GsKTX4dyK',
            }

            r = get(url,data=data)

        **请求结果**::

            {
                  "group": {
                    "_id": "ByehQjC44FwMeiLbX",
                    "ts": "2018-19-19T21:15:04.737Z",
                    "t": "p",
                    "name": "testing",
                    "usernames": [
                      "testing",
                      "testing1"
                    ],
                    "u": {
                        "_id": "aobEdbYhXfu5hkeqG",
                        "username": "testing1"
                    },
                    "msgs": 1,
                    "_updatedAt": "2018-10-19T12:50:51.575Z",
                    "lm": "2018-10-19T12:50:51.555Z"
                  },
                  "success": true
                }

        """ 
        roomId = request.form['roomId']
        userId = request.form['userId']
        
        try:
            r = rocket.groups_invite(room_id=roomId,user_id=userId)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'添加失败。'},401

        return {
            'success':True,
            'group':r.json()['group'],
        },200


class GroupsKick(Resource):
    """从组中删除用户
    https://rocket.chat/docs/developer-guides/rest-api/groups/kick/
    """
    def put(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/groups/kick
              - 需要auth
              - PUT
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - HyehQjC44FwMeiLbX
              - 必须
              - 群组id
            * - userId
              - nSYqWzZ4GsKTX4dyK
              - 必须
              - 用户id

        **请求示例**::

            data = {
                'roomId':'7aDSXtjMA3KPLxLjt',
                'userId':'nSYqWzZ4GsKTX4dyK',
            }

            r = get(url,data=data)

        **请求结果**::

            {
                  "group": {
                    "_id": "ByehQjC44FwMeiLbX",
                    "ts": "2018-19-19T21:15:04.737Z",
                    "t": "p",
                    "name": "testing",
                    "usernames": [
                      "testing",
                      "testing1"
                    ],
                    "u": {
                        "_id": "aobEdbYhXfu5hkeqG",
                        "username": "testing1"
                    },
                    "msgs": 1,
                    "_updatedAt": "2018-10-19T12:50:51.575Z",
                    "lm": "2018-10-19T12:50:51.555Z"
                  },
                  "success": true
                }

        """ 
        roomId = request.form['roomId']
        userId = request.form['userId']
        
        try:
            r = rocket.groups_kick(room_id=roomId,user_id=userId)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'删除失败。'},401

        return {
            'success':True,
            'group':r.json()['group'],
        },200


class GroupsLeave(Resource):
    """删除主用户
    https://rocket.chat/docs/developer-guides/rest-api/groups/leave/
    """
    def get(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/groups/leave
              - 需要auth
              - GET
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - HyehQjC44FwMeiLbX
              - 必须
              - 群组id
            

        **请求示例**::

            r = get(url,roomId=roomId)

        **请求结果**::

            {
                  "group": {
                    "_id": "ByehQjC44FwMeiLbX",
                    "name": "invite-me",
                    "t": "p",
                    "usernames": [
                      "testing2"
                    ],
                    "msgs": 0,
                    "u": {
                      "_id": "aobEdbYhXfu5hkeqG",
                      "username": "testing1"
                    },
                    "ts": "2018-10-19T15:08:58.042Z",
                    "ro": false,
                    "sysMes": true,
                    "_updatedAt": "2018-10-19T15:22:40.656Z"
                  },
                  "success": true
                }
        """ 
        roomId = request.form['roomId']
        
        try:
            r = rocket.groups_leave(room_id=roomId)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'删除失败。'},401

        return {
            'success':True,
            'group':r.json()['group'],
        },200


class List(Resource):
    """获取群组列表
    https://rocket.chat/docs/developer-guides/rest-api/groups/list/
    """
    def get(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/groups/list
              - 需要auth
              - GET

        **请求示例**::

            r = get(url)

        **请求结果**::

            {
                "groups": [
                    {
                        "_id": "ByehQjC44FwMeiLbX",
                        "name": "test-test",
                        "t": "p",
                        "msgs": 0,
                        "u": {
                            "_id": "aobEdbYhXfu5hkeqG",
                            "username": "testing1"
                        },
                        "ts": "201-10-19T15:08:58.042Z",
                        "ro": false,
                        "sysMes": true,
                        "_updatedAt": "201-10-19T15:22:40.656Z"
                    },
                    {
                        "_id": "t7qapfhZjANMRAi5w",
                        "name": "testing",
                        "t": "p",
                        "msgs": 0,
                        "u": {
                            "_id": "y65tAmHs93aDChMWu",
                            "username": "testing2"
                        },
                        "ts": "201-10-11T15:08:58.042Z",
                        "ro": false,
                        "sysMes": true,
                        "_updatedAt": "201-10-19T15:22:40.656Z"
                    }
                ],
                "offset": 0,
                "count": 1,
                "total": 1,
                "success": true
            }

        """ 
        try:
            r = rocket.groups_list()
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'获取失败。'},401

        return {
            'success':True,
            'group':r.json()['group'],
            'offset':r.json()['offset'],
            'count':r.json()['count'],
            'total':r.json()['total'],
        },200


class ListAll(Resource):
    """获取所有群组以及私人的群组，需要view-room-administration权限
    https://rocket.chat/docs/developer-guides/rest-api/groups/listall/
    """
    def get(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/groups/list
              - 需要auth
              - GET

        **请求示例**::

            r = get(url)

        **请求结果**::

            {
                "groups": [
                    {
                        "_id": "xA52DRDM7dqx2PfTp",
                        "name": "private1",
                        "fname": "private1",
                        "t": "p",
                        "msgs": 0,
                        "u": {
                            "_id": "3WpJQkDHhrWPBvXuW",
                            "username": "admin"
                        },
                        "customFields": {
                            "companyId": "org1"
                        },
                        "ts": "2018-10-21T21:05:06.729Z",
                        "ro": false,
                        "sysMes": true,
                        "_updatedAt": "2018-10-21T21:05:06.729Z"
                    }
                ],
                "offset": 0,
                "count": 1,
                "total": 1,
                "success": true
            }

        """ 
        try:
            r = rocket.groups_list_all()
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'获取失败。'},401

        return {
            'success':True,
            'groups':r.json()['groups'],
            'offset':r.json()['offset'],
            'count':r.json()['count'],
            'total':r.json()['total'],
        },200


class GroupsMembers(Resource):
    """ 获取群组内的用户
    https://rocket.chat/docs/developer-guides/rest-api/groups/members/
    """
    def get(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/groups/members
              - 需要auth
              - GET
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - HyehQjC44FwMeiLbX
              - 必须
              - 群组id

        **请求示例**::

            r = get(url,data={'roomId':'7aDSXtjMA3KPLxLjt'})

        **请求结果**::

            {
                "members": [
                    {
                        "_id": "Q4GkX6RMepGDdQ7YJ",
                        "status": "online",
                        "name": "Marcos Defendi",
                        "utcOffset": -3,
                        "username": "marcos.defendi"
                    },
                    {
                        "_id": "rocket.cat",
                        "name": "Rocket.Cat",
                        "username": "rocket.cat",
                        "status": "online",
                        "utcOffset": 0
                    }
                ],
                "count": 2,
                "offset": 0,
                "total": 2,
                "success": true
            }

        """ 
        roomId = request.form['roomId']
        
        try:
            r = rocket.groups_members(room_id=roomId)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'获取失败。'},401

        return {
            'success':True,
            'members':r.json()['members'],
            'count':r.json()['count'],
            'offset':r.json()['offset'],
            'total':r.json()['total'],
        },200


class Messages(Resource):
    """检索所有组消息。 插件无该接口
    https://rocket.chat/docs/developer-guides/rest-api/groups/messages/
    """
    pass
    

class Moderators(Resource):
    """
    插件无该接口
    """
    pass


class GroupsOpen(Resource):
    """将私有组添加回用户的私有组列表。?Adds the private group back to the user’s list of private groups.
    https://rocket.chat/docs/developer-guides/rest-api/groups/open/
    """
    def get(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/groups/open
              - 需要auth
              - GET
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - HyehQjC44FwMeiLbX
              - 必须
              - 群组id

        **请求示例**::

            r = get(url,data={'roomId':'7aDSXtjMA3KPLxLjt'})

        **请求结果**::

            {
                "success": true
            }

        """ 
        roomId = request.form['roomId']
        
        try:
            r = rocket.groups_open(room_id=roomId)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'操作失败。'},401

        return {
            'success':True,
        },200


class GroupsRename(Resource):
    """更改群组名称。
    https://rocket.chat/docs/developer-guides/rest-api/groups/rename/
    """
    def put(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/groups/rename
              - 需要auth
              - PUT
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - HyehQjC44FwMeiLbX
              - 必须
              - 群组id
            * - name
              - new-name
              - 必须
              - 更改的名称

        **请求示例**::

            data = {
                'roomId':'7aDSXtjMA3KPLxLjt',
                'name':'new name',
            }

            r = put(url,data=data)

        **请求结果**::

            {
                  "group": {
                    "_id": "ByehQjC44FwMeiLbX",
                    "name": "new-name",
                    "t": "p",
                    "usernames": [
                      "testing1"
                    ],
                    "msgs": 4,
                    "u": {
                      "_id": "aobEdbYhXfu5hkeqG",
                      "username": "testing1"
                    },
                    "ts": "2018-10-19T15:08:58.042Z",
                    "ro": false,
                    "sysMes": true,
                    "_updatedAt": "2018-10-19T15:57:44.686Z"
                  },
                  "success": true
            }

        """ 
        roomId = request.form['roomId']
        name = request.form['name']
        
        try:
            r = rocket.groups_rename(room_id=roomId,name=name)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'操作失败。'},401

        return {
            'success':True,
            'group':r.json()['group'],
        },200


class Role(Resource):
    """获取群组中的角色
    https://rocket.chat/docs/developer-guides/rest-api/groups/roles/
    """
    def get(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/groups/roles
              - 需要auth
              - GET
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - HyehQjC44FwMeiLbX
              - 必须
              - 群组id

        **请求示例**::

            r = get(url,data={'roomId':'7aDSXtjMA3KPLxLjt'})

        **请求结果**::

            {
                "roles": [
                    {
                        "rid": "BaE62jfDLXK3Xo6BA",
                        "u": {
                           "_id": "BkNkw3iKgNyhMbPyW",
                           "username": "ronnie.dio",
                           "name": "Ronnie James Dio"
                        },
                        "roles": [
                           "moderator"
                        ],
                        "_id": "ehPuGyZBedznJsQHp"
                    }
                ],
                "success": true
            }

        """ 
        roomId = request.form['roomId']
        
        try:
            r = rocket.groups_roles(room_id=roomId)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'获取失败。'},401

        return {
            'success':True,
            'roles':r.json()['roles'],
        },200


class SetAnnouncement(Resource):
    pass

class SetCustomFields(Resource):
    pass


class SetDescriptions(Resource):
    """设置群组描述
    https://rocket.chat/docs/developer-guides/rest-api/groups/setdescription/
    """
    def put(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/groups/setdescription
              - 需要auth
              - PUT
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - HyehQjC44FwMeiLbX
              - 必须
              - 群组id
            * - description
              - 这是群组描述
              - 必须
              - 群组描述

        **请求示例**::

            data = {
                'roomId':'7aDSXtjMA3KPLxLjt',
                'description':'new description',
            }

            r = put(url,data=data)

        **请求结果**::

            {
                  "description": 'new description',
                  "success": true
            }

        """ 
        roomId = request.form['roomId']
        description = request.form['description']
        
        try:
            r = rocket.groups_set_description(room_id=roomId,description=description)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'设置失败。'},401

        return {
            'success':True,
            'description':r.json()['description'],
        },200


class SetPurpose(Resource):
    """设置私人组的描述？与上面描述类似？插件无该接口
    https://rocket.chat/docs/developer-guides/rest-api/groups/setpurpose/
    """
    pass


class SetReadOnlyer(Resource):
    """设置是否只读
    https://rocket.chat/docs/developer-guides/rest-api/groups/setreadonly/

    """
    def get(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/groups/set_read_only
              - 需要auth
              - GET
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - HyehQjC44FwMeiLbX
              - 必须
              - 群组id
            * - readOnly
              - 1
              - 必须
              - 0  或 1 

        **请求示例**::

            r = get(url,data={'roomId':'7aDSXtjMA3KPLxLjt','readOnly':1})

        **请求结果**::

            {
                "group": {
                    "_id": "ByehQjC44FwMei5LbX",
                    "name": "testing-private",
                    "t": "p",
                    "msgs": 0,
                    "u": {
                        "_id": "aiPqNoGkjpNDiRx6d",
                        "username": "goose160"
                    },
                    "ts": "2018-10-18T18:02:50.754Z",
                    "ro": true,
                    "sysMes": true,
                    "_updatedAt": "2018-10-18T19:02:24.429Z",
                    "usernames": [
                        "goose160",
                        "graywolf336"
                    ],
                    "joinCodeRequired": true,
                    "muted": []
                },
                "success": true
            }

        """ 
        roomId = request.form['roomId']
        readOnly = request.form['readOnly']

        if readOnly:
            readOnly = True
        else:
            readOnly = False
        
        try:
            r = rocket.groups_set_read_only(room_id=roomId,read_only=readOnly)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'操作失败。'},401

        return {
            'success':True,
            'group':r.json()['group'],
        },200



class GroupsSetTopic(Resource):
    """设置私有组话题？
    https://rocket.chat/docs/developer-guides/rest-api/groups/settopic/
    """
    def put(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/groups/set_topic
              - 需要auth
              - PUT
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - HyehQjC44FwMeiLbX
              - 必须
              - 群组id
            * - topic
              - Discuss all of the testing.
              - 必须
              - 私有组的话题设置

        **请求示例**::

            data = {
                'roomId':'7aDSXtjMA3KPLxLjt',
                'topic':'Discuss all of the testing',
            }

            r = put(url,data=data)

        **请求结果**::

            {
              "topic": "Testing out everything.",
              "success": true
            }

        """ 
        roomId = request.form['roomId']
        topic = request.form['topic']
        
        try:
            r = rocket.groups_set_topic(room_id=roomId,topic=topic)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'设置失败。'},401

        return {
            'success':True,
            'topic':r.json()['topic'],
        },200


class GroupsSetType(Resource):
    """设置私有组的类型
    https://rocket.chat/docs/developer-guides/rest-api/groups/settype/
    """
    def put(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/groups/set_type
              - 需要auth
              - PUT
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - HyehQjC44FwMeiLbX
              - 必须
              - 群组id
            * - type
              - c
              - c or p
              - 设置群组的类型为c或者p

        **请求示例**::

            data = {
                'roomId':'7aDSXtjMA3KPLxLjt',
                'type':'c',
            }

            r = put(url,data=data)

        **请求结果**::

            {
                "group": {
                    "_id": "ByehQjC44FwMeiLbX",
                    "name": "testing0",
                    "t": "c",
                    "msgs": 0,
                    "u": {
                        "_id": "aiPqNoGkjpNDiRx6d",
                        "username": "goose160"
                    },
                    "ts": "2018-10-19T18:02:50.754Z",
                    "ro": false,
                    "sysMes": true,
                    "_updatedAt": "2018-10-19T19:02:24.429Z",
                    "usernames": [
                        "goose160",
                        "graywolf336"
                    ],
                    "joinCodeRequired": true,
                    "muted": []
                },
                "success": true
            }

        """ 
        roomId = request.form['roomId']
        a_type = request.form['type']
        
        try:
            r = rocket.groups_set_type(room_id=roomId,a_type=a_type)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'设置失败。'},401

        return {
            'success':True,
            'group':r.json()['group'],
        },200


class GroupsUnarchive(Resource):
    """
    https://rocket.chat/docs/developer-guides/rest-api/groups/unarchive/
    """
    def get(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/groups/un_archives
              - 需要auth
              - GET
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - HyehQjC44FwMeiLbX
              - 必须
              - 频道id

        **请求示例**::

            r = get(url,data={'roomId':'7aDSXtjMA3KPLxLjt'})

        **请求结果**:
         - success:boolean

        """ 
        roomId = request.form['roomId']
        
        try:
            r = rocket.groups_unarchive(room_id=roomId)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'操作失败。'},401

        return {
            'success':True
        },200






api.add_resource(GroupsArchive, f'/api/{v1}/groups/groupArchive') 
api.add_resource(GroupsClose, f'/api/{v1}/groups/close') 
api.add_resource(GroupsCreate, f'/api/{v1}/groups/create') 
api.add_resource(GroupsDelete, f'/api/{v1}/groups/delete') 
api.add_resource(GroupsFiles, f'/api/{v1}/groups/groupFile') 
api.add_resource(GroupsHistory, f'/api/{v1}/groups/history') 
api.add_resource(GroupsInfo, f'/api/{v1}/groups/info') 
api.add_resource(GroupsInvite, f'/api/{v1}/groups/invite') 
api.add_resource(GroupsKick, f'/api/{v1}/groups/kick') 
api.add_resource(GroupsLeave, f'/api/{v1}/groups/leave') 
api.add_resource(List, f'/api/{v1}/groups/list') 
api.add_resource(ListAll, f'/api/{v1}/groups/listAll') 
api.add_resource(GroupsMembers, f'/api/{v1}/groups/members') 
api.add_resource(GroupsOpen, f'/api/{v1}/groups/open') 
api.add_resource(GroupsRename, f'/api/{v1}/groups/rename') 
api.add_resource(Role, f'/api/{v1}/groups/roles') 
api.add_resource(SetDescriptions, f'/api/{v1}/groups/setdescription') 
api.add_resource(SetPurpose, f'/api/{v1}/groups/setpurposes') 
api.add_resource(SetReadOnlyer, f'/api/{v1}/groups/set_read_only') 
api.add_resource(GroupsSetTopic, f'/api/{v1}/groups/set_topic') 
api.add_resource(GroupsSetType, f'/api/{v1}/groups/set_type') 
api.add_resource(GroupsUnarchive, f'/api/{v1}/groups/un_archives') 


