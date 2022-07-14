import random

class ListNode:
    def __init__(self, data=None):
        self._data = data
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
        p = self._head
        for i in range(self._level_count - 1, -1, -1):
            while p._forwards[i] and p._forwards[i]._data < value:
                p = p._forwards[i]
        return p._forwards[0] if p._forwards[0] and p._forwards[0]._data == value else None

    def find_range(self, begin_value, end_value):
        '''
        查找一组元素, 返回一组ListNode对象
        '''
        p = self._head
        begin = None
        for i in range(self._level_count - 1, -1, -1):   # Move down a level
            while p._forwards[i] and p._forwards[i]._data < begin_value:
                p = p._forwards[i]   # Move along level
            if p._forwards[i] and p._forwards[i]._data >= begin_value:
                begin = p._forwards[i]

        if begin is None:
            return None #没有找到
        else:
            result = []
            while begin and begin._data <= end_value :
                result.append(begin)
                begin = begin._forwards[0] 
            return result

    def insert(self, value):
        '''
        插入一个元素, 返回True or False
        '''
        level = self._random_level()
        if self._level_count < level: self._level_count = level
        new_node = ListNode(value)
        new_node._forwards = [None] * level
        update = [self._head] * level
        p = self._head
        for i in range(level - 1 , -1, -1):
            while p._forwards[i] and p._forwards[i]._data < value:
                p = p._forwards[i]
            update[i] = p
        for i in range(level):
            new_node._forwards[i] = update[i]._forwards[i]
            update[i]._forwards[i] = new_node
        return True

    def delete(self, value):
        '''
        删除一个元素, 返回True or Flase
        '''
        update = [None] * self._level_count
        p = self._head
        for i in range(self._level_count - 1, -1, -1):
            while p._forwards[i] and p._forwards[i]._data < value:
                p = p._forwards[i]
            update[i] = p

        if p._forwards[0] and p._forwards[0]._data == value:
            for i in range(self._level_count - 1, -1, -1):
                if update[i]._forwards[i] and update[i]._forwards[i]._data == value:
                    update[i]._forwards[i] = update[i]._forwards[i]._forwards[i]     # Similar to prev.next = prev.next.next
            return True
        else:
            return False

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
        skiplist_str = ''
        i = self._level_count -1 
        while i >= 0:
            p = self._head
            skiplist_str = f'head {i}: '
            while p:
                if p._data:
                    skiplist_str += '->' + str(p._data)
                p = p._forwards[i]
            print(skiplist_str)
            i -= 1

if __name__ == "__main__":
    l = SkipList()
    l.pprint()
    for i in range(0, 40, 3):
        l.insert(i)
    l.pprint() 
    if l.delete(15):
        print("delete 15 success.")
    l.pprint() 
    if not l.delete(16):
        print("delete 16 fail.")
    l.pprint() 
    print("find 9 : ", l.find(9)._data)
    print("find data between 4 and 10:")
    for d in l.find_range(4, 10):
        print(d._data,end ='->')
