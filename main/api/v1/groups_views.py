#coding=utf-8
from flask_restful import Resource
from main.extensions import api,rocket
from flask import request

from .version import dev_1
v1 = dev_1



class Archive(Resource):
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
            * - /api/v1/groups/archive
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
            r = rocket.groups_archive(msg_id=roomId)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'操作失败。'},401

        return {
            'success':True
        },200


class GroupsClose(Resource):
    """

    """
    def get(self):
        """"""
        pass

    def put(self):
        """"""
        pass


class Counters(Resource):
    """

    """
    def get(self):
        """"""
        pass

    def put(self):
        """"""
        pass


class GroupsCreate(Resource):
    """

    """
    def get(self):
        """"""
        pass

    def put(self):
        """"""
        pass

class GroupsDelete(Resource):
    """

    """
    def get(self):
        """"""
        pass

    def put(self):
        """"""
        pass

class Files(Resource):
    """

    """
    def get(self):
        """"""
        pass

    def put(self):
        """"""
        pass

class History(Resource):
    """

    """
    def get(self):
        """"""
        pass

    def put(self):
        """"""
        pass

class Info(Resource):
    """

    """
    def get(self):
        """"""
        pass

    def put(self):
        """"""
        pass

class Invite(Resource):
    """

    """
    def get(self):
        """"""
        pass

    def put(self):
        """"""
        pass

class Kick(Resource):
    """

    """
    def get(self):
        """"""
        pass

    def put(self):
        """"""
        pass

class Leave(Resource):
    """

    """
    def get(self):
        """"""
        pass

    def put(self):
        """"""
        pass

class List(Resource):
    """

    """
    def get(self):
        """"""
        pass

    def put(self):
        """"""
        pass

class ListAll(Resource):
    """

    """
    def get(self):
        """"""
        pass

    def put(self):
        """"""
        pass

class Members(Resource):
    """

    """
    def get(self):
        """"""
        pass

    def put(self):
        """"""
        pass

class Messages(Resource):
    """

    """
    def get(self):
        """"""
        pass

    def put(self):
        """"""
        pass

class Moderators(Resource):
    """

    """
    def get(self):
        """"""
        pass

    def put(self):
        """"""
        pass

class Open(Resource):
    """

    """
    def get(self):
        """"""
        pass

    def put(self):
        """"""
        pass

class Rename(Resource):
    """

    """
    def get(self):
        """"""
        pass

    def put(self):
        """"""
        pass

class Roles(Resource):
    """

    """
    def get(self):
        """"""
        pass

    def put(self):
        """"""
        pass

class SetAnnouncement(Resource):
    """

    """
    def get(self):
        """"""
        pass

    def put(self):
        """"""
        pass

class SetCustomFields(Resource):
    """

    """
    def get(self):
        """"""
        pass

    def put(self):
        """"""
        pass

class SetDescription(Resource):
    """

    """
    def get(self):
        """"""
        pass

    def put(self):
        """"""
        pass

class SetPurpose(Resource):
    """

    """
    def get(self):
        """"""
        pass

    def put(self):
        """"""
        pass

class SetReadOnly(Resource):
    """

    """
    def get(self):
        """"""
        pass

    def put(self):
        """"""
        pass

class SetTopic(Resource):
    """

    """
    def get(self):
        """"""
        pass

    def put(self):
        """"""
        pass

class SetType(Resource):
    """

    """
    def get(self):
        """"""
        pass

    def put(self):
        """"""
        pass

class Unarchive(Resource):
    """

    """
    def get(self):
        """"""
        pass

    def put(self):
        """"""
        pass




api.add_resource(Archive, f'/api/{v1}/groups/archive') 

