from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('mysql://root:@localhost:3306/admin?charset=utf8', encoding="utf8", echo=False)
BaseDB = declarative_base()

ERROR_CODE = {
    "40000": "成功",
    "40001": "入参非法",
    "40002": "手机号已存在",
    "40003": "用户不存在",
    "40004": "您输入的密码有误",
}