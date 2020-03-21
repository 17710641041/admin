#### 目录及文件说明

```
common：存放公共类和方法
conf: 存放配置文件
log：存放相关日志
static：存放静态文件，如样式（CSS）、脚本（js）、图片等
templates：公用模板目录，主要存放 HTML 文件
views：视图函数，业务逻辑代码目录
main.py：Tornado 主程序入口
models.py：数据库表结构定义
```

#### 项目依赖模块

```buildoutcfg
pip install mysqlclient-1.4.6-cp38-cp38-win_amd64.whl
https://pypi.org/project/mysqlclient/#files
pip install tornado
pip install mysql-connector-python
pip install sqlalchemy
```