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
    isEnable = Column(Integer, nullable=True)
    addTime = Column(DateTime, nullable=True)

    def __init__(
            self,
            name,
            addTime,
            isEnable = 1,
            icon = '',
            pid = 0
    ):
        self.name = name
        self.addTime = addTime
        self.isEnable = isEnable
        self.addTime = addTime
        self.icon = icon
        self.pid = pid

def initdb():
    BaseDB.metadata.create_all(engine)


if __name__ == '__main__':
    print("Initialize database")
    initdb()