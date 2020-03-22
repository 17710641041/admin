from __future__ import unicode_literals
from .goods_category import (addGoodsCategory,queryGoodsCategory)

urls = [
    (r'addGoodsCategory', addGoodsCategory),
    (r'queryGoodsCategory', queryGoodsCategory)
]
