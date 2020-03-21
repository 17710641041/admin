from conf.base import BaseDB, engine
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)


class Users(BaseDB):
    """table for users"""
    __tablename__ = "users"
    # 定义表结构，包括id，phone，password，createTime
    id = Column(Integer, primary_key=True)
    phone = Column(Integer, nullable=False)
    password = Column(String(32), nullable=False)
    nickName = Column(String(25), nullable=True)
    headImgurl = Column(String(200), nullable=True)
    sex = Column(Integer, nullable=True)
    parentCode = Column(String(20), nullable=True)
    weixinOpenid = Column(String(32), nullable=True)
    alipayOpenid = Column(String(32), nullable=True)
    baiduOpenid = Column(String(32), nullable=True)
    status = Column(Integer, nullable=True)
    createTime = Column(DateTime, nullable=True)

    def __init__(
            self,
            phone,
            password,
            createTime,
            nickName = '',
            headImgurl='',
            sex=1,
            parentCode='',
            weixinOpenid = '',
            alipayOpenid = '',
            baiduOpenid = '',
            status = 1
    ):
        self.phone = phone
        self.password = password
        self.createTime = createTime
        self.nickName = nickName
        self.headImgurl = headImgurl
        self.sex = sex
        self.parentCode = parentCode
        self.weixinOpenid = weixinOpenid
        self.alipayOpenid = alipayOpenid
        self.baiduOpenid = baiduOpenid
        self.status = status


def initdb():
    BaseDB.metadata.create_all(engine)


if __name__ == '__main__':
    print("Initialize database")
    initdb()