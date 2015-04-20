# TornOrm
A simple orm base on Torndb

Simple Demo:

        from tornorm import Base, get_connection, set_
        
        conn = get_connection(host='localhost', database='test', user='root', password='toor', maxcached=100,
                              pre_exe=('set names utf8mb4', ))
        
        
        class TestOrm(Base):
        
            _table_name = 'test_orm'
            _rows = [
                'id', 'name', 'content', 'type'
            ]
            _per_page = 10
            _db_conn = conn

        # new
        tm = TestModel.new(name='hello', content='this is content')
        # get
        test_mode = TestModel.get(id=23)
        test_mode.dictify(fields=['name'], properties=['status_label'])
        test_mode.name = 'new name'
        test_mode.save()
        # explore the code to find more
