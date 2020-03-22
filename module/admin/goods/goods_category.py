"""
商品分类
"""
from conf.base import BaseDB, engine
from sqlalchemy import (Column, Integer, String, DateTime)


class goodsCategory(BaseDB):
    """table for users"""
    __tablename__ = "goods_category"
    # 定义表结构，包括id，phone，password，createTime
    id = Column(Integer, primary_key=True)
    pid = Column(Integer, nullable=False)
    icon = Column(String(255), nullable=False)
    name = Column(String(60), nullable=False)
    sort = Column(Integer, nullable=False)
    isEnable = Column(Integer, nullable=True)
    addTime = Column(DateTime, nullable=True)

    def __init__(
        self,
        name,
        addTime,
        pid = 0,
        sort= 99,
        isEnable = 1,
        icon = ''

    ):
        self.name = name
        self.addTime = addTime
        self.pid = pid
        self.sort = sort
        self.isEnable = isEnable
        self.icon = icon


def initdb():
    BaseDB.metadata.create_all(engine)


if __name__ == '__main__':
    print("Initialize database")
    initdb()