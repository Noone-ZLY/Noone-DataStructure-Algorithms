import random

class ListNode:
    def __init__(self, key=None, value=None):
        self._key = key
        self._value = value
        self._forwards = []


class SkipList:
    _MAX_LEVEL = 4
    def __init__(self):
        self._level_count = 1
        self._head = ListNode()
        self._head._forwards = [None] * self._MAX_LEVEL

    def find(self, value):
        '''
        查找一个元素, 返回一个ListNode对象
        '''
        pass

    def find_range(self, begin_value, end_value):
        '''
        查找一组元素, 返回一组ListNode对象
        '''
        pass

    def insert(self, value):
        '''
        插入一个元素, 返回True or False
        '''
        pass

    def delete(self, value):
        '''
        删除一个元素, 返回True or Flase
        '''
        pass

    def _random_level(self, p=0.5):
        '''
        返回随机层数
        '''
        level = 1
        while random.random() < p and level < self._MAX_LEVEL:
            level += 1
        return level

    def pprint(self):
        '''
        打印链表
        '''
        pass

