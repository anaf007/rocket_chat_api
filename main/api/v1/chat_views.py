#coding=utf-8
from flask_restful import Resource
from main.extensions import api,rocket
from flask import request

from .version import dev_1
v1 = dev_1


class ChatDelete(Resource):
    """删除聊天信息

    https://rocket.chat/docs/developer-guides/rest-api/chat/delete/
    """
    def put(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/chat/chatdelete
              - 需要auth
              - PUT
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - ByehQjC44FwMeiLbX
              - 必须
              - 频道id
            * - msgId
              - 7aDSXtjMA3KPLxLjt
              - 必须
              - 需要删除消息的id
            * - asUser
              - 1
              - 默认0
              - 是否作为发送消息的用户删除消息。

        **请求示例**::

            data = {
                'roomId':'ByehQjC44FwMeiLbX',
                'msgId':'7aDSXtjMA3KPLxLjt',
                'asUser':1
    
            }
            r = put(url,data=data)

        **请求结果**:
         - success:boolean
         - id
         - ts

        """ 
        roomId = request.form['roomId']
        msgId = request.form['msgId']
        asUser = request.form['asUser']

        if asUser:
            asUser = True
        else:
            asUser = False 

        try:
            r = rocket.chat_delete(room_id=roomId,msg_id=msgId,asUser=asUser)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'删除失败。'},401

        return {
            'ts':r.json()['ts'],
            'id':r.json()['_id'],
            'success':True
        }


class GetMessage(Resource):
    """获取聊天信息
    
    https://rocket.chat/docs/developer-guides/rest-api/chat/getmessage/
    """
    def get(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/chat/getMessage
              - 需要auth
              - GET
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - msgId
              - 7aDSXtjMA3KPLxLjt
              - 必须
              - 要获取消息的id

        **请求示例**::

            r = get(url,data={'msgId':'7aDSXtjMA3KPLxLjt'})

        **请求结果**:
         - success:boolean
         - message:json

        """ 
        msgId = request.form['msgId']
        
        try:
            r = rocket.channels_files(msg_id=msgId)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'获取失败。'},401

        return {
            'message':r.json()['message'],
            'success':True
        }  


class PinMessage(Resource):
    """pin聊天信息到频道
    
    https://rocket.chat/docs/developer-guides/rest-api/chat/pinmessage/
    """
    def get(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/chat/pinMessage
              - 需要auth
              - GET
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - msgId
              - 7aDSXtjMA3KPLxLjt
              - 必须
              - 需要pin消息的id

        **请求示例**::

            r = get(url,data={'msgId':'7aDSXtjMA3KPLxLjt'})

        **请求结果**:
         - success:boolean
         - message:json

        """ 
        msgId = request.form['msgId']
        
        try:
            r = rocket.chat_pin_message(msg_id=msgId)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'pin失败。'},401

        return {
            'message':r.json()['message'],
            'success':True
        }  


class PostMessage(Resource):
    """发布聊天信息
    
    https://rocket.chat/docs/developer-guides/rest-api/chat/postmessage/
    """
    def put(self):
        """
        .. list-table:: 请求信息
            :header-rows: 1

            * - URL
              - Auth
              - HTTP方法
            * - /api/v1/chat/postMessage
              - 需要auth
              - PUT
        
        .. list-table:: 请求参数
            :header-rows: 1

            * - 参数名称
              - 示例
              - 必须
              - 描述
            * - roomId
              - ByehQjC44FwMeiLbX
              - 必须
              - 消息发送位置的频道ID。
            * - channel
              - #general
              - 必须
              - 消息发送位置的频道名称，注意前面带有#前缀
            * - text
              - Sample message
              - 可选
              - 要发送的文本消息
            * - alias
              - Some Name
              - 可选
              - 别名，但是还是会显示用户名
            * - emoji
              - :smirk:
              - 可选
              - 设置消息头像为表情符号
            * - avatar
              - http://site.com/logo.png
              - 可选
              - 设置头像为图像url
            * - attachments
              - [{}]
              - 可选
              - 可选的附加值，有关详细，看下面的介绍


        可选细节：一般为对象数组，可以有许多部分，包括：
         - 作者信息
         - 标题信息
         - 图片
         - 音频
         - 视频
         - 表/字段

        .. list-table:: 附加细节
            :header-rows: 1

            * - 属性
              - 示例
              - 选择
              - 描述
            * - color
              - #ff0000
              - 一般
              - 可选的css背景值
            * - text
              - Sample attachment text
              - 一般
              - 附件要显示的文本，与邮件的文本不同
            * - ts
              - 2018-10-16T16:53:06.761Z
              - 一般
              - 显示在text旁边的时间值
            * - thumb_url
              - https://site.com/img.png
              - 在附加文本前显示头像
              - 可选的css背景值
            * - message_link
              - https://rocket.chat
              - 一般
              - 在提供ts是有效的一个消息连接
            * - collapsed
              - false
              - 一般
              - 视频或者图像是否折叠
            * - author_name
              - anaf 
              - 作者
              - 作者姓名
            * - author_link
              - https://rocket.chat/
              - 作者
              - 作者主页连接
            * - author_icon
              - https://site.com/img.png
              - 作者
              - 作者姓名左侧小图标
            * - title
              - Attachment Title
              - 作者
              - 作者下方标题
            * - title_link
              - https://rocket.chat/
              - 标题
              - 标题连接
            * - title_link_download
              - true
              - 标题
              - 标题下载按钮地址
            * - image_url
              - https://site.com/img.png
              - 图片
              - 要显示的图像地址
            * - audio_url
              - https://site.com/aud.mp3
              - 音频
              - 要播放的音频文件，只支持html音频的功能。
            * - video_url
              - https://site.com/vid.mp4
              - 视频
              - 要播放的视频文件，只支持html视频的功能。
            * - fields
              - [{}]
              - 字段
              - 再附加对象的数组对象

        **附件字段对象：** 附件的字段属性允许在消息上显示“表”或“列”。

        .. list-table:: 附件字段对象
            :header-rows: 1

            * - 属性
              - 示例
              - 必要
              - 描述
            * - short
              - true
              - 默认false
              - 该字段是否应该是短字段。
            * - title
              - Status
              - 必须
              - 字段标题
            * - value
              - online
              - 必须
              - 字段的值，显示在标题之下

        **官方请求示例**::

            {
                "alias": "Gruggy",
                "avatar": "http://res.guggy.com/logo_128.png",
                "channel": "#general",
                "emoji": ":smirk:",
                "roomId": "Xnb2kLD2Pnhdwe3RH",
                "text": "Sample message",
                "attachments": [
                    {
                        "audio_url": "http://www.w3schools.com/tags/horse.mp3",
                        "author_icon": "https://avatars.githubusercontent.com/u/850391?v=3",
                        "author_link": "https://rocket.chat/",
                        "author_name": "Bradley Hilton",
                        "collapsed": false,
                        "color": "#ff0000",
                        "fields": [
                            {
                                "short": true,
                                "title": "Test",
                                "value": "Testing out something or other"
                            },
                            {
                                "short": true,
                                "title": "Another Test",
                                "value": "[Link](https://google.com/) something and this and that."
                            }
                        ],
                        "image_url": "http://res.guggy.com/logo_128.png",
                        "message_link": "https://google.com",
                        "text": "Yay for gruggy!",
                        "thumb_url": "http://res.guggy.com/logo_128.png",
                        "title": "Attachment Example",
                        "title_link": "https://youtube.com",
                        "title_link_download": true,
                        "ts": "2016-12-09T16:53:06.761Z",
                        "video_url": "http://www.w3schools.com/tags/movie.mp4"
                    }
                ]
            }

        **请求结果**::
        
            {
              "ts": 1481748965123,
              "channel": "general",
              "message": {
                "alias": "",
                "msg": "This is a test!",
                "parseUrls": true,
                "groupable": false,
                "ts": "2016-12-14T20:56:05.117Z",
                "u": {
                  "_id": "y65tAmHs93aDChMWu",
                  "username": "graywolf336"
                },
                "rid": "GENERAL",
                "_updatedAt": "2016-12-14T20:56:05.119Z",
                "_id": "jC9chsFddTvsbFQG7"
              },
              "success": true
            }

        **由于参数太多，暂时按照最少的是只需要3个参数，频道id、名称、和内容，其他省略：**

        """ 
        roomId = request.form['roomId']
        channel = request.form['channel']
        text = request.form['text']

        if channel:
            channel = "#"+channel
        else:
            channel = False 

        try:
            r = rocket.chat_delete(room_id=roomId,msg_id=msgId,asUser=asUser)
        except Exception as e:
            r = None

        if not r:
            return {'success':False,'message':'删除失败。'},401

        return {
            'ts':r.json()['ts'],
            'id':r.json()['_id'],
            'success':True
        }


class React(Resource):
    """设置/取消现有聊天
    
    https://rocket.chat/docs/developer-guides/rest-api/chat/delete/
    """
    pass


class ReportMessage(Resource):
    """汇报聊天信息
    
    https://rocket.chat/docs/developer-guides/rest-api/chat/delete/
    """
    pass


class ChatSearch(Resource):
    """搜索聊天信息
    
    https://rocket.chat/docs/developer-guides/rest-api/chat/delete/
    """
    pass


class StarMessage(Resource):
    """开始聊天
    
    https://rocket.chat/docs/developer-guides/rest-api/chat/delete/
    """
    pass


class SendMessage(Resource):
    """发送聊天信息
    
    https://rocket.chat/docs/developer-guides/rest-api/chat/delete/
    """
    pass


class UnPinMessage(Resource):
    """删除聊天窗口
    
    https://rocket.chat/docs/developer-guides/rest-api/chat/delete/
    """
    pass


class UnStarMessage(Resource):
    """删除开始聊天状态
    
    https://rocket.chat/docs/developer-guides/rest-api/chat/delete/
    """
    pass


class ChatUpdate(Resource):
    """更新信息
    
    https://rocket.chat/docs/developer-guides/rest-api/chat/delete/
    """
    pass


class GetMessageReadReceipts(Resource):
    """检索聊天信息回复
    
    https://rocket.chat/docs/developer-guides/rest-api/chat/delete/
    """
    pass



api.add_resource(ChatDelete, f'/api/{v1}/chat/chatdelete')  
api.add_resource(GetMessage, f'/api/{v1}/chat/getMessage')  
api.add_resource(PinMessage, f'/api/{v1}/chat/pinMessage')  
api.add_resource(PostMessage, f'/api/{v1}/chat/postMessage')  
api.add_resource(React, f'/api/{v1}/chat/react')  
api.add_resource(ReportMessage, f'/api/{v1}/chat/report_message')  
api.add_resource(ChatSearch, f'/api/{v1}/chat/chat_search')  
api.add_resource(StarMessage, f'/api/{v1}/chat/star_message')  
api.add_resource(SendMessage, f'/api/{v1}/chat/send_message')  
api.add_resource(UnPinMessage, f'/api/{v1}/chat/un_pin_message')  
api.add_resource(UnStarMessage, f'/api/{v1}/chat/un_star_message')  
api.add_resource(ChatUpdate, f'/api/{v1}/chat/chat_update')  
api.add_resource(GetMessageReadReceipts, f'/api/{v1}/chat/get_message_read_receipts')  




