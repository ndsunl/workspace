from pymongo import MongoClient


class DataBaseManager(object):
    def __init__(self):
        """
        你需要在这里初始化MongoDB的连接，连上本地MongoDB，库名为chapter_4，集合名为people_info
        """
        client = MongoClient()
        database = client.chapter_4
        self.handler = database.people_info


    def query_info(self):
        """
        你需要在这里实现这个方法,
        查询集合people_info并返回所有"deleted"字段为0的数据。
        注意返回的信息需要去掉_id
        """
        info_list = list(self.handler.find({"deleted": 0}, {'_id': 0}))

        return info_list


    def _query_last_id(self):
        """
        你需要实现这个方法，查询当前已有数据里面最新的id是多少
        返回一个数字，如果集合里面至少有一条数据，那么就返回最新数据的id，
        如果集合里面没有数据，那么就返回0
        提示：id不重复，每次加1

        :return: 最新ID
        """
        last_id = self.handler.find({}, {'_id':0, 'id':1}).sort('id', -1).limit(1)

        return last_id[0]['id'] if last_id else 0

    def add_info(self, para_dict):
        """
        你需要实现这个方法，添加人员信息。
        你可以假设para_dict已经是格式化好的数据了，
        你直接把它插入MongoDB即可，不需要做有效性判断。

        在实现这个方法时，你需要首先查询MongoDB，获取已有数据里面最新的ID是多少，
        这个新增的人员的ID需要在已有的ID基础上加1.


        :param para_dict: 格式为{'name': 'xxx', 'age': 12, 'birthday': '2000-01-01', 'origin_home': 'xxx', 'current_home': 'yyy', 'deleted': 0}
        :return: True或者False
        """
        current_id = 1
        current_id += self._query_last_id()
        para_dict.update(id = current_id)
        self.handler.insert_one(para_dict)

        last_id = self._query_last_id()

        return True if last_id == current_id else False
        

    def update_info(self, people_id, para_dict):
        """
        你需要实现这个方法。这个方法用来更新人员信息。
        更新信息是根据people_id来查找的，因此people_id是必需的。

        :param people_id: 人员id，数字
        :param para_dict: 格式为{'name': 'xxx', 'age': 12, 'birthday': '2000-01-01', 'origin_home': 'xxx', 'current_home': 'yyy'}
        :return: True或者False
        """
        try:
            self.handler.update_one({'id': people_id}, {'$set': para_dict})
        except Exception as e:
            print(f'修改数据失败，信息如下: {e}')
            return False

        return True


    def del_info(self, people_id):
        """
        你需要实现这个方法。请注意，此处需要使用"假删除"，
        把删除操作写为更新"deleted"字段的值为1
        :param people_id: 人员id
        :return: True或者False
        """
        try:
            self.handler.update_one({'id': people_id}, {'$set': {'deleted': 1}})
        except Exception as e:
            print(f'删除数据失败，信息如下: {e}')
            return False
            
        return True


if __name__ == '__main__':
    database_manager = DataBaseManager()
