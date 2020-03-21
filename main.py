"""
# -*- coding:utf-8 -*-
# Author: 宋国君
# Email: 673903363.com
# Version: 商城项目入口文件
"""

import platform
import tornado.ioloop
import tornado.web
import os
from tornado.options import define, options
from common.url_router import include, url_wrapper
from sqlalchemy.orm import scoped_session, sessionmaker
from conf.base import BaseDB, engine

# windows 系统下 tornado 使用 使用 SelectorEventLoop
if platform.system() == "Windows":
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class Application(tornado.web.Application):
    def __init__(self):
        handlers = url_wrapper([
            (r"/users/", include('views.users.users_urls'))
        ])
        # 定义 Tornado 服务器的配置项，如 static/templates 目录位置、debug 级别等
        settings = dict(
            debug=True,
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            template_path=os.path.join(os.path.dirname(__file__), "templates")
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=True, expire_on_commit=False))

if __name__ == '__main__':
    print("Tornado server is ready for service\r")
    tornado.options.parse_command_line()
    Application().listen(8000, xheaders=True)
    tornado.ioloop.IOLoop.instance().start()
