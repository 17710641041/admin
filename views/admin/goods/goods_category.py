"""
    商品分类
"""
import json

import tornado.web
from tornado.escape import json_decode
from datetime import datetime

from conf.toJSon import (AlchemyEncoder)

# 从commons中导入http_response方法
from common.commons import (http_response )

# 从配置文件中导入错误码
from conf.base import (ERROR_CODE)

from module.admin.goods.goods_category import (goodsCategory)

class addGoodsCategory(tornado.web.RequestHandler):

    @property
    def db(self):
        return self.application.db

    def post(self):
        try:
            # 获取入参
            args = json_decode(self.request.body)
            name = args['name']
            pid = args['pid']
            sort = args['sort']
        except:
            # 获取入参失败时，抛出错误码及错误信息
            http_response(self, ERROR_CODE['40001'], 40001)
            return
        ex_user = self.db.query(goodsCategory).filter_by(name=name).first()
        if ex_user:
            http_response(self, ERROR_CODE['40005'], 40005)
        else:
            create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            add_goods_category = goodsCategory(name, create_time, pid, sort)
            self.db.add(add_goods_category)
            self.db.commit()
            self.db.close()
            # 处理成功后，返回成功码“0”及成功信息“ok”
            http_response(self, ERROR_CODE['40000'], 40000)


class queryGoodsCategory(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def get(self):
        ex_user = self.db.query(goodsCategory).all()
        if ex_user:
            data = json.dumps(ex_user, cls=AlchemyEncoder)
            obj = json.loads(data)
            self.db.commit()
            self.db.close()
            http_response(self, obj, 40000)
        else:
            http_response(self, ERROR_CODE['40006'], 40006)


class delGoodsCategory(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def post(self):
        try:
            # 获取入参
            args = json_decode(self.request.body)
            id = args['id']
        except:
            # 获取入参失败时，抛出错误码及错误信息
            http_response(self, ERROR_CODE['40001'], 40001)
            return
        ex_user = self.db.query(goodsCategory).filter_by(id=id).first()
        if ex_user:
            self.db.delete(ex_user)
            self.db.commit()
            self.db.close()
            http_response(self, ERROR_CODE['40000'], 40000)
        else:
            http_response(self, ERROR_CODE['40007'], 40007)
