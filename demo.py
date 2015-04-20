# coding: utf8
# 测试之前先建立数据库test, 数据表question, 字段定义如下

import time

from tornorm import Base, get_connection


conn = get_connection(host='localhost', database='test', user='root', password='toor', maxcached=100,
                      pre_exe=('set names utf8mb4', ))


class Question(Base):

    _db_conn = conn

    _table_name = 'question'
    _rows = [
        'id', 'title', 'content', 'type', 'ins_time', 'status', 'user_id', 'image',
        'last_answer_time', 'last_answer_id', 'max_answer_like', 'answer_count', 'fix_time'
    ]
    # _db_config = {'host': 'localhost', 'database': 'familyparty', 'user': 'root', 'pre_exe': ('set names utf8mb4', )}
    _per_page = 10

    type_v = 2  # 加v用户的问题
    type_editor = 0  # 编辑编辑的问题
    type_user = 1  # 普通用户的问题

    # 状态
    status_del = 0
    status_normal = 1  # 用户的问题标志位
    status_hot = 2  # 热门问题 : 问题最大回答赞数量达到20
    status_home = 3  # 首页问题: 1. 小编的问题, 2. 小编回答的问题, 3. 问题回答最大赞达到50

    @classmethod
    def new(cls, **params):
        """ 新建问题
        """
        params['ins_time'] = int(time.time())
        return super(Question, cls).new(**params)

    @classmethod
    def get(cls, fields=None, **kwargs):
        """ 取得一个问题
        """
        return super(Question, cls).get(fields=fields, **kwargs)


# ---------------- 定义测试函数 ---------------------

def new():
    return Question.new(
        title=u'问题标题',
        content=u'问题内容',
        type=Question.type_v,
        status=1,
        user_id='hello'
    )


def get(id):
    return Question.get(id=id)


def find():
    return Question.find(status=1, user_id='hello')


if __name__ == '__main__':
    q = new()
    print 'new: ', q.dictify()
    q = get(id=q.id)
    print 'get: ', q.dictify()
    r = find()
    print 'find: ', len(r)