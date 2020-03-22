from __future__ import unicode_literals
from .goods_category import (addGoodsCategory, queryGoodsCategory, delGoodsCategory)

urls = [
    (r'addGoodsCategory', addGoodsCategory),
    (r'queryGoodsCategory', queryGoodsCategory),
    (r'delGoodsCategory', delGoodsCategory)
]
