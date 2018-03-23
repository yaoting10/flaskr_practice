#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from sqlalchemy import create_engine, MetaData

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.contrib.cache import RedisCache


engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/test', convert_unicode=True)
metadata = MetaData(bind=engine)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
cache = RedisCache(host="t.dev.mattbaby.com", port=6379, password="hmp_uat")


def init_db():
    # 在这里导入所有的可能与定义模型有关的模块，这样他们才会合适地
    # 在 metadata 中注册。否则，您将不得不在第一次执行 init_db() 时
    # 先导入他们。
    import com.orm.models
    Base.metadata.create_all(bind=engine)