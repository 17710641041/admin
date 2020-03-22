import json

import tornado.web
import logging
import hashlib
from tornado.escape import json_decode
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

from conf.toJSon import (
    AlchemyEncoder
)

# 从commons中导入http_response方法
from common.commons import (http_response )

# 从配置文件中导入错误码
from conf.base import (ERROR_CODE)

from module.user.user_module import (Users)

########## 登录日志 #############
logFilePath = "log/users/users.log"
logger = logging.getLogger("Users")
logger.setLevel(logging.DEBUG)
handler = TimedRotatingFileHandler(logFilePath, when="D", interval=1, backupCount=30)
formatter = logging.Formatter('%(asctime)s \
%(filename)s[line:%(lineno)d] %(levelname)s %(message)s', )
handler.suffix = "%Y%m%d"
handler.setFormatter(formatter)
logger.addHandler(handler)


#获取用户信息
class usersGet(tornado.web.RequestHandler):

    @property
    def db(self):
        return self.application.db

    def post(self):
        try:
            # 获取入参
            args = json_decode(self.request.body)
            phone = args['phone']
        except:
            # 获取入参失败时，抛出错误码及错误信息
            logger.info("usersGet: request argument incorrect")
            http_response(self, ERROR_CODE['40001'], 40001)
            return
        ex_user = self.db.query(Users).filter_by(phone=phone).first()
        if ex_user:
            #转json字符串
            userData = json.dumps(ex_user, cls=AlchemyEncoder)
            obj = json.loads(userData)
            del obj["password"]
            # 处理成功后，返回成功码“0”及成功信息“ok”
            logger.debug("loginHandle: regist successfully")
            http_response(self, obj, 40000)
        else:
            logger.debug("loginHandle: 用户信息不存在")
            http_response(self, ERROR_CODE['40003'], 40003)



#用户登录
class loginHandle(tornado.web.RequestHandler):

    """
    handle /user/login
    :param phone: 用户手机号
    :param password: 用户密码
    :param code: 验证码
    """

    @property
    def db(self):
        return self.application.db

    def post(self):
        try:
            # 获取入参
            args = json_decode(self.request.body)
            phone = args['phone']
            password = args['password']
            verify_code = args['code']
        except:
            # 获取入参失败时，抛出错误码及错误信息
            logger.info("loginHandle: request argument incorrect")
            http_response(self, ERROR_CODE['40001'], 40001)
            return
        ex_user = self.db.query(Users).filter_by(phone=phone).first()

        if ex_user:
            hash = hashlib.md5()
            hash.update(bytes(password, encoding='utf-8'))
            if(hash.hexdigest() != ex_user.password):
                http_response(self, ERROR_CODE['40004'], 40004)
            else:
                #转json字符串
                userData = json.dumps(ex_user, cls=AlchemyEncoder)
                obj = json.loads(userData)
                del obj["password"]
                # 处理成功后，返回成功码“0”及成功信息“ok”
                logger.debug("loginHandle: regist successfully")
                http_response(self, obj, 40000)
        else:
            logger.debug("loginHandle: 用户信息不存在")
            http_response(self, ERROR_CODE['40003'], 40003)


#用户注册
class RegistHandle(tornado.web.RequestHandler):

    """
    handle /user/regist request
    :param phone: 用户手机号
    :param password: 用户密码
    :param code: 验证码
    """

    @property
    def db(self):
        return self.application.db

    def post(self):
        try:
            # 获取入参
            args = json_decode(self.request.body)
            phone = args['phone']
            password = args['password']
            verify_code = args['code']
        except:
            # 获取入参失败时，抛出错误码及错误信息
            logger.info("RegistHandle: request argument incorrect")
            http_response(self, ERROR_CODE['40001'], 40001)
            return

        ex_user = self.db.query(Users).filter_by(phone=phone).first()
        if ex_user:
            # 如果手机号已存在，返回用户已注册信息
            http_response(self, ERROR_CODE['40002'], 40002)
            self.db.close()
            return
        else:
            # 用户不存在，数据库表中插入用户信息
            hash = hashlib.md5()
            hash.update(bytes(password, encoding='utf-8'))
            logger.debug("RegistHandle: insert db, user: %s" % phone)
            create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            add_user = Users(phone, hash.hexdigest(), create_time)
            self.db.add(add_user)
            # 处理成功后，返回成功码“0”及成功信息“ok”
            self.db.commit()
            self.db.close()
            logger.debug("RegistHandle: regist successfully")
            http_response(self, ERROR_CODE['40000'], 40000)
