"""
    商品分类
"""
import tornado.web
import logging
from tornado.escape import json_decode
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

from conf.toJSon import (AlchemyEncoder)

# 从commons中导入http_response方法
from common.commons import (http_response )

# 从配置文件中导入错误码
from conf.base import (ERROR_CODE)

from module.admin.goods.goods_category import (goodsCategory)

class addGoodsCategory(tornado.web.RequestHandler):

    def post(self):
        try:
            # 获取入参
            args = json_decode(self.request.body)
            phone = args['phone']
        except:
            # 获取入参失败时，抛出错误码及错误信息
            http_response(self, ERROR_CODE['40001'], 40001)
            return
        http_response(self, ERROR_CODE['40000'], 40000)