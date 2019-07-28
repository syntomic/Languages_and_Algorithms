## 代码风格：Pythonic
- 链式比较：`1 < a < 7`
- 交换变量：`x, y = y, x`
- 三目运算符：`c = a if a > b else b`
- 字符
- 拼接字符：`" ".join([a, b])`
- 格式化：`{}.format(name)`
- 生成式：`{user['name']: user['email'] for user in user_list if 'email' in user}`
- 条件判断：`if l:  # l.__len__() == 0` `if something is None # None 是单例对象`
- enumerate：`for index, element in enumerate(my_container)`
- 避免可变类型作为默认初始值
- 一切皆对象
- 防御式编程EAFP vs LBYL
    
    ```python
    # LBYL
    def getPersonInfo(person):
        if person is None:
            print('person must be not null!')
        print person.info

    # EAFP
    def getPersonInfo(person):
        try:
            print(person.info)
        except NameError:
            print('person must be not null!')
    ```
    
- 用`dict`对象完成`switch...case...`的功能
- 访问`tuple`的数据项时，可以用`namedtuple`代替index的方式访问
- 用`isinstance`来判断对象的类型：`isinstance(some_object, (int, float))`
- 用with管理操作资源的上下文环境
    ```python
    class Connection(object):
        def execute(self, sql):
            raise Exception('ohoh, exception!')

        def close(self):
            print 'closed the Connection'

        def __enter__(self):
            return self

        def __exit__(self, errorType, errorValue, error):
            self.close()

    with Connection() as conn:
        conn.execute('select * from t_users')
    ```

- 使用`generator`返回耗费内存的对象：`yeild item`
- docstring: 使用sphinx自动生成API文档
    - Google style
        ```python
        """
        This is a groups style docs.

        Parameters:
            param1 - this is the first param
            param2 - this is a second param

        Returns:
            This is a description of what is returned

        Raises:
            KeyError - raises an exception
        """
        ```
