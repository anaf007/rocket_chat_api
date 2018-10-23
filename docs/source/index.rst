.. rocket_chat_api documentation master file, created by
   sphinx-quickstart on Tue Oct  9 14:55:27 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


项目rocket_chat_api的api文档
===========================================

https://github.com/jadolg/rocketchat_API

该项目依赖rocket_chat，必须先运行。

插件rocketchat_API

以下是rocket_chat接口信息



基本信息
====================================================================

.. list-table:: 基本信息功能列表，共计8个
   :header-rows: 1

   * - URL
     - 描述
     - 进度
   * - /api/v1/bases/info
     - Rocket.Chat服务信息
     - 已完成
   * - /api/v1/bases/directory
     - 在服务器上搜索所有用户或频道
     - 已完成
   * - /api/v1/bases/shield_svg
     - 获取网站或者添加svg
     - 插件无该接口
   * - /api/v1/bases/spotlight
     - 搜索可用的房间或者用户
     - 已完成
   * - /api/v1/bases/statistics
     - 有关Rocket.Chat服务器的统计信息
     - 已完成
   * - /api/v1/bases/statistics_list
     - 服务器统计信息列表。
     - 已完成
   * - /api/v1/bases/assets_setAsset
     - 按名称设置资产图像
     - 插件无该接口
   * - /api/v1/bases/assets_unsetAsset
     - 按名称取消资产设置
     - 插件无该接口

.. automodule:: main.api.v1.base_views
   :members:


身份验证
====================================================================

.. list-table:: 身份验证列表，共计2个
   :header-rows: 1

   * - URL
     - 描述
     - 进度
   * - /api/v1/auth/login
     - 使用REST API进行身份验证。
     - 完成
   * - /api/v1/auth/me
     - 显示有关已验证用户的信息。
     - 完成

.. automodule:: main.api.v1.authentication_views
   :members:


用户模块
====================================================================

.. list-table:: 用户模块列表，共计21个
   :header-rows: 1

   * - URL
     - 描述
     - 进度
   * - /api/v1/user/create
     - 创建一个新用户。
     - 已完成
   * - /api/v1/user/createToken
     - 创建用户身份验证令牌。
     - 已完成
   * - /api/v1/user/delete
     - 删除现有用户。
     - 已完成
   * - /api/v1/user/deleteOwnAccount
     - 用户删除自己的帐户。
     - 插件无该接口
   * - /api/v1/user/forgotPassword
     - 重置密码。
     - 已完成
   * - /api/v1/user/generatePersonalAccessToken
     - 生成个人访问令牌。
     - 插件无该接口
   * - /api/v1/user/getAvatar
     - 获取用户头像的URL。
     - 已完成
   * - /api/v1/user/getPersonalAccessTokens
     - 获取用户的个人访问令牌。
     - 插件无该接口
   * - /api/v1/user/getPreferences
     - 获取用户的所有首选项。
     - 已完成
   * - /api/v1/user/getPresence
     - 获取用户的在线状态。
     - 已完成
   * - /api/v1/user/getUsernameSuggestion
     - 获取用户的建议
     - 插件无该接口
   * - /api/v1/user/info
     - 获取用户的信息，仅限于调用者的权限。
     - 已完成
   * - /api/v1/user/list
     - 所有用户及其信息，仅限于权限。
     - 已完成
   * - /api/v1/user/regeneratePersonalAccessToken
     - 重新生成用户个人访问令牌。
     - 插件无该接口
   * - /api/v1/user/register
     - 注册新用户。
     - 已完成
   * - /api/v1/user/removePersonalAccessToken
     - 删除个人访问令牌。
     - 插件无该接口
   * - /api/v1/user/resetAvatar
     - 重置用户的头像
     - 已完成
   * - /api/v1/user/setAvatar
     - 设置用户的头像
     - 已完成
   * - /api/v1/user/setPreferences
     - 设置用户的首选项
     - 已完成
   * - /api/v1/user/update
     - 更新现有用户。
     - 已完成
   * - /api/v1/user/updateOwnBasicInfo
     - 更新自己用户的基本信息。
     - 插件无该接口

.. automodule:: main.api.v1.user_views
   :members:


频道
====================================================================

.. list-table:: 频道列表，共计33个
   :header-rows: 1

   * - URL
     - 描述
     - 进度
   * - /api/v1/channels/addAll
     - 将服务器上的所有用户添加到通道。
     - 已完成
   * - /api/v1/channels/archive
     - 存档一个频道。
     - 已完成
   * - /api/v1/channels/cleanHistory
     - 清理频道的历史记录，需要特殊许可。
     - 插件无该接口
   * - /api/v1/channels/close
     - 从用户的频道列表中删除频道。
     - 已完成
   * - /api/v1/channels/counters
     - 获取通道计数器。
     - 插件无该接口
   * - /api/v1/channels/create
     - 创建一个新频道。
     - 已完成
   * - /api/v1/channels/delete
     - 删除频道。
     - 已完成
   * - /api/v1/channels/files
     - 获取通道中的文件列表。
     - 已完成
   * - /api/v1/channels/getAllUserMentionsByChannel
     - 获取频道的所有提及。
     - 已完成
   * - /api/v1/channels/getIntegrations
     - 获取通道的集成。
     - 已完成
   * - /api/v1/channels/history
     - 从通道中检索消息。
     - 已完成
   * - /api/v1/channels/info
     - 获取频道的信息。
     - 已完成
   * - /api/v1/channels/invite
     - 将用户添加到频道。
     - 已完成
   * - /api/v1/channels/kick
     - 从频道中删除用户。
     - 已完成
   * - /api/v1/channels/leave
     - 从通道中删除主用户。
     - 已完成
   * - /api/v1/channels/list
     - 从服务器检索所有通道。
     - 已完成
   * - /api/v1/channels/list_joined
     - 仅获取调用用户已加入的通道。
     - 已完成
   * - /api/v1/channels/members
     - 频道用户列表。
     - 已完成
   * - /api/v1/channels/messages
     - 获取频道所有消息。
     - 插件无该接口
   * - /api/v1/channels/moderators
     - 列出频道的所有版主。
     - 插件无该接口
   * - /api/v1/channels/open
     - 将频道添加回用户的频道列表。
     - 已完成
   * - /api/v1/channels/rename
     - 更改频道的名称。
     - 已完成
   * - /api/v1/channels/roles
     - 列出频道中所有用户的角色。
     - 已完成
   * - /api/v1/channels/setCustomFields
     - 设置频道的自定义字段。
     - 已完成
   * - /api/v1/channels/setAnnouncement
     - 设置频道公告。
     - 已完成
   * - /api/v1/channels/setDefault
     - 设置通道是否为默认通道。
     - 插件无该接口
   * - /api/v1/channels/setDescription
     - 设置频道的描述。
     - 已完成
   * - /api/v1/channels/setJoinCode
     - 设置加入频道所需的代码。
     - 已完成
   * - /api/v1/channels/setPurpose
     - 设置频道的说明。
     - 插件无该接口
   * - /api/v1/channels/setReadOnly
     - 设置通道是否为只读。
     - 已完成
   * - /api/v1/channels/setTopic
     - 设置频道的主题。
     - 已完成
   * - /api/v1/channels/setType
     - 设置频道应该是的房间类型。
     - 已完成
   * - /api/v1/channels/unarchive
     - 取消归档频道。
     - 已完成

.. automodule:: main.api.v1.channels_views
   :members:


群组
====================================================================

.. list-table:: 群组列表，共计27个
   :header-rows: 1

   * - URL
     - 描述
     - 进度
   * - /api/v1/groups/groupArchive
     - 保存该聊天群组。
     - 已完成
   * - /api/v1/groups/close   
     - 从组列表中删除私有群组。
     - 已完成
   * - /api/v1/groups/counters
     - 获取群组计数。
     - 插件无该接口
   * - /api/v1/groups/create
     - 创建群组。
     - 已完成
   * - /api/v1/groups/delete
     - 删除私人组。
     - 已完成
   * - /api/v1/groups/files
     - 获取私有组中的文件列表。
     - 已完成
   * - /api/v1/groups/history
     - 从私有组中检索历史消息。
     - 已完成
   * - /api/v1/groups/info
     - 获取有关专用组的信息。
     - 已完成
   * - /api/v1/groups/invite
     - 将用户添加到私有组。
     - 已完成
   * - /api/v1/groups/kick
     - 从私有组中删除用户。
     - 已完成
   * - /api/v1/groups/leave
     - 从私有组中删除主用户。
     - 已完成
   * - /api/v1/groups/list
     - 列出调用者所属的私有组。
     - 已完成
   * - /api/v1/groups/listAll
     - 列出所有群组包含私人组。
     - 已完成
   * - /api/v1/groups/members
     - 获取群组内的用户
     - 已完成
   * - /api/v1/groups/messages
     - 检索所有组消息。
     - 插件无该接口
   * - /api/v1/groups/moderators
     - 列出组的所有主持人。
     - 插件无该接口
   * - /api/v1/groups/open
     - 将专用组添加回组列表。  
     - 已完成
   * - /api/v1/groups/rename
     - 更改群组名称。
     - 已完成
   * - /api/v1/groups/roles
     - 获取用户在私有组中的角色。
     - 已完成
   * - /api/v1/groups/setAnnouncement
     - 设置组的公告。
     - 插件无该接口
   * - /api/v1/groups/setCustomFields
     - 设置专用组的自定义字段。
     - 插件无该接口
   * - /api/v1/groups/setDescription
     - 设置私人组的描述。
     - 已完成
   * - /api/v1/groups/setPurpose
     - 设置私人组的宗旨。
     - 插件无该接口
   * - /api/v1/groups/setReadOnly
     - 设置房间是否为只读。
     - 已完成
   * - /api/v1/groups/setTopic
     - 设置私有组话题。
     - 已完成
   * - /api/v1/groups/setType
     - 设置此组的房间类型。
     - 已完成
   * - /api/v1/groups/unarchive
     - 取消归档私人组。
     - 已完成

.. automodule:: main.api.v1.groups_views
   :members:


聊天接口
====================================================================

.. list-table:: 聊天接口列表，共计13个
   :header-rows: 1

   * - URL
     - 描述
     - 进度
   * - /api/v1/chat/chat_delete
     - 删除现有聊天消息。
     - 已完成
   * - /api/v1/chat/getMessage
     - 获取聊天消息。    
     - 已完成
   * - /api/v1/chat/pinMessage
     - 将聊天消息固定到消息的频道。
     - 已完成
   * - /api/v1/chat/postMessage
     - 发布新的聊天消息。
     - 已完成
   * - /api/v1/chat/react
     - 设置/取消设置用户对现有聊天消息的反应。
     - 已完成
   * - /api/v1/chat/reportMessage
     - 报告消息。
     - 插件无该接口
   * - /api/v1/chat/search
     - 搜索频道中的消息。
     - 已完成
   * - /api/v1/chat/starMessage
     - 标记聊天消息。
     - 已完成
   * - /api/v1/chat/sendMessage
     - 发送新的聊天消息。
     - 暂定
   * - /api/v1/chat/unPinMessage
     - 删除提供的聊天消息的固定状态。
     - 已完成
   * - /api/v1/chat/unStarMessage
     - 删除标记信息。
     - 已完成
   * - /api/v1/chat/update
     - 更新聊天消息的文本。
     - 已完成
   * - /api/v1/chat/getMessageReadReceipts
     - 检索邮件已读回执。
     - 已完成

.. automodule:: main.api.v1.chat_views
   :members:

IM接口    
====================================================================

.. list-table:: IM接口 列表，共计12个
   :header-rows: 1

   * - URL
     - 描述
     - 进度
   * - /api/v1/im.close
     - 从直接消息列表中删除直接消息。
     -
   * - /api/v1/im.counters
     - 获取直接消息的计数器。
     -
   * - /api/v1/im.create
     - 与其他用户创建直接消息会话。
     -
   * - /api/v1/im.history
     - 从直接消息中检索消息。
     -
   * - /api/v1/im.files
     - 从直接消息中检索文件列表。
     -
   * - /api/v1/im.members
     - 检索直接消息的参与者的用户。
     -
   * - /api/v1/im.messages
     - 从特定直接消息中检索消息。
     -
   * - /api/v1/im.messages.others
     - 从服务器中的任何直接消息中检索消息。
     -
   * - /api/v1/im.list
     - 列出调用者所属的直接消息。
     -
   * - /api/v1/im.list.everyone
     - 列出服务器中呼叫者的所有直接消息。
     -
   * - /api/v1/im.open
     - 将直接消息添加回直接消息列表。
     -
   * - /api/v1/im.setTopic
     - 设置直接消息主题。
     -  

.. automodule:: main.api.v1.im_views
   :members:
   :undoc-members: 


集成接口
====================================================================


.. list-table:: 集成接口列表，共计4个
   :header-rows: 1

   * - URL
     - 描述
     - 进度
   * - /api/v1/integrations.create
     - 创建集成。
     -
   * - /api/v1/integrations.history
     - 列出指定集成的所有历史记录。
     -
   * - /api/v1/integrations.list
     - 列出所有集成。
     -
   * - /api/v1/integrations.remove
     - 删除集成。
     -         

.. automodule:: main.api.v1.integrations_views
   :members:
   :undoc-members: 


权限接口
====================================================================


.. list-table:: 权限接口列表，共计2个
   :header-rows: 1

   * - URL
     - 描述
     - 进度
   * - /api/v1/permissions.list
     - 列出服务器上的权限。
     -
   * - /api/v1/permissions.update
     - 编辑服务器上的权限。
     -

.. automodule:: main.api.v1.permissions_views
   :members:
   :undoc-members: 


角色接口
====================================================================


.. list-table:: 角色接口列表，共计3个
   :header-rows: 1

   * - URL
     - 描述
     - 进度
   * - /api/v1/roles.create
     - 在系统中创建新角色。
     -
   * - /api/v1/roles.addUserToRole
     - 获取系统中的所有角色。
     -
   * - /api/v1/roles.list
     - 为用户分配角色。
     -

.. automodule:: main.api.v1.roles_views
   :members:
   :undoc-members: 


.. toctree::
   :maxdepth: 2
   :caption: Contents:


推送令牌
====================================================================


.. list-table:: 推送令牌列表，共计1个
   :header-rows: 1

   * - URL
     - 方法
     - 描述
     - 进度
   * - /api/v1/push.token 
     - POST
     - 保存推送令牌。
     -
   * - /api/v1/push.token 
     - DELETE
     - 删除推送令牌。
     -


.. automodule:: main.api.v1.push_token_views
   :members:
   :undoc-members: 


房间
====================================================================


.. list-table:: 房间接口列表，共计5个
   :header-rows: 1

   * - URL
     - 描述
     - 进度
   * - /api/v1/rooms.cleanHistory
     - 清理房间的历史，需要特殊许可。
     -
   * - /api/v1/rooms.favorite
     - 最喜欢/不喜欢的房间。
     -
   * - /api/v1/rooms.get
     - 获取房间。
     -
   * - /api/v1/rooms.saveNotification
     - 设置特定频道的通知设置。
     -
   * - /api/v1/rooms.upload/:rid
     - 上传带附件的邮件。
     -


.. automodule:: main.api.v1.rooms_views
   :members:
   :undoc-members: 


命令方法
====================================================================


.. list-table:: 命令方法列表，共计3个
   :header-rows: 1

   * - URL
     - 描述
     - 进度
   * - /api/v1/commands.get
     - 获取斜杠命令的规范。
     -
   * - /api/v1/commands.list
     - 列出所有可用的斜杠命令。
     -
   * - /api/v1/commands.run
     - 在指定的房间中执行斜杠命令。
     -

.. automodule:: main.api.v1.commands_views
   :members:
   :undoc-members:



Emoji定制
====================================================================


.. list-table:: Emoji定制列表，共计1个
   :header-rows: 1

   * - URL
     - 描述
     - 进度
   * - /api/v1/emoji-custom
     - 列出可用的自定义表情符号。
     -


.. automodule:: main.api.v1.emoji_views
   :members:
   :undoc-members:


消息接口
====================================================================


.. list-table:: 消息接口列表，共计1个
   :header-rows: 1

   * - URL
     - 描述
     - 进度
   * - /api/v1/messages/types
     - 列出所有可用的消息类型。
     -

.. automodule:: main.api.v1.messages_views
   :members:
   :undoc-members:


设置接口
====================================================================


.. list-table:: 设置接口列表，共计6个
   :header-rows: 1

   * - URL
     - 方法
     - 描述
     - 进度
   * - /api/v1/settings
     - GET
     - 列出所有私人设置。
     -
   * - /api/v1/settings.public
     - GET
     - 列出所有公共设置。
     -
   * - /api/v1/settings.oauth
     - GET
     - 返回所有可用oauth服务的列表。
     -
   * - /api/v1/service.configurations
     - GET
     - 列出所有服务配置。    
     -
   * - /api/v1/settings/:_id [GET]
     - GET
     - 获取一个设置。
     -
   * - /api/v1/settings/:_id [POST]
     - POST
     - 更新设置。
     -


.. automodule:: main.api.v1.settings_views
   :members:
   :undoc-members:


订阅接口
====================================================================

.. list-table:: 订阅接口列表，共计4个
   :header-rows: 1

   * - URL
     - 方法
     - 描述
     - 进度
   * - /api/v1/subscriptions.get
     - GET
     - 获取所有订阅。
     - 
   * - /api/v1/subscriptions.getOne
     - GET
     - 按房间ID获取订阅。
     -
   * - /api/v1/subscriptions.read  
     - POST
     - 将房间标记为已读。
     -
   * - /api/v1/subscriptions.unread
     - POST
     - 将邮件标记为未读。
     -

.. automodule:: main.api.v1.subscriptions_views
   :members:
   :undoc-members:


.. toctree::
   :maxdepth: 2
   :caption: Contents:




