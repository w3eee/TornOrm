# coding: utf8
""" 单元测试
"""
# coding: utf8
# before run this test you must create database first
# run: create database test default character set utf8  # in mysql-client

import unittest

from tornorm import Base, get_connection, set_

conn = get_connection(host='localhost', database='test', user='root', password='toor',
                      pre_exe=('set names utf8mb4', ))


class TestOrm(Base):

    _table_name = 'test_orm'
    _rows = [
        'id', 'name', 'content', 'type'
    ]
    _per_page = 10
    _db_conn = conn


class OrmTest(unittest.TestCase):

    def setUp(self):
        # 建立数据库表
        self.conn = conn
        self.conn.execute("DROP TABLE IF EXISTS `test_orm`; CREATE TABLE `test_orm` (`id` int NOT NULL AUTO_INCREMENT,"
                          "name varchar(128),content varchar(64),`type` tinyint(2) DEFAULT 1,"
                          "PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;")

    def test_new(self):
        t = TestOrm.new(name='test1', content='test', type=1)
        o = self.conn.get('select * from test_orm where name="test1"')
        self.assertTrue(t)
        self.assertEqual(t.id, o.id)

    def test_get(self):
        self._init_data()
        t = TestOrm.get(name='test0')
        self.assertTrue(t)
        self.assertEqual(t.type, 0)

    def test_exists(self):
        self._init_data()
        e = TestOrm.exists(name='test0')
        self.assertEqual(e, True)

    def test_find(self):
        # 插入三条数据
        for i in range(3):
            self._init_data()
        rs = TestOrm.find(name='test0')
        self.assertTrue(rs)
        self.assertEqual(len(rs), 3)

    def test_new_mul(self):
        data = [dict(name='test%s' % i, content='test%s' % i) for i in range(5)]
        rs = TestOrm.new_mul(*data)
        self.assertTrue(rs)
        # 此时数据库有五条数据
        rs = self.conn.query('select * from test_orm')
        self.assertEqual(len(rs), 5)

    def test_page(self):
        # 插入十条数据
        for i in range(10):
            self._init_data()
        rs1 = TestOrm.page(page=1, per_page=6)
        self.assertEqual(len(rs1), 6)
        rs2 = TestOrm.page(page=2, per_page=6)
        self.assertEqual(len(rs2), 4)

    def test_delete(self):
        self._init_data()
        d = TestOrm.delete(name='test0')
        self.assertTrue(d)
        # 此时 表是空的
        c = self.conn.query('select * from test_orm')
        self.assertFalse(c)

    def test_cls_update(self):
        self._init_data()
        cu = TestOrm.cls_update(set_(name='test1'), name='test0')
        self.assertTrue(cu)
        r1 = self.conn.query('select * from test_orm where name="test0"')
        self.assertFalse(r1)
        r2 = self.conn.query('select * from test_orm where name="test1"')
        self.assertTrue(r2)

    def test_update(self):
        self._init_data()
        o = TestOrm.get(name='test0')
        self.assertTrue(o)
        o = o.update(name='test1')
        self.assertEqual(o.name, 'test1')
        r2 = self.conn.query('select * from test_orm where name="test1"')
        self.assertTrue(r2)
        o.name = 'test2'
        o = o.save()
        self.assertEqual(o.name, 'test2')
        r2 = self.conn.query('select * from test_orm where name="test2"')
        self.assertTrue(r2)

    def _empty_table(self):
        self.conn.execute("delete from test_orm")

    def _init_data(self, name='test0', content='test', _type=0):
        self.conn.execute("insert into test_orm (name, content, type)values (%s, %s, %s)", name, content, _type)

    def tearDown(self):
        self._empty_table()
        # self.conn.execute("DROP TABEL test_orm")


if __name__ == '__main__':
    unittest.main()


