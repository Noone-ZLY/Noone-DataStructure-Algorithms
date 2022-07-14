from hashlib import new
from sympy import N


class ListNode:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next
    

class LinkList:
    def __init__(self) -> None:
        new_Node = ListNode()
        self.head = new_Node
    
    def init_by_array(self, nums):
        '''
        用数组初始化链表
        '''
        for num in nums[::-1]:
            new_node = ListNode(val=num)
            new_node.next = self.head.next
            self.head.next = new_node
        return True
    
    def insert(self, val):
        '''
        尾部插入元素, 返回True or Flase
        '''
        cur = self.head
        while cur.next:
            cur = cur.next
        new_node = ListNode(val)
        new_node.next = cur.next
        cur.next = new_node
        return True

    def delete(self, val):
        '''
        删除元素, 返回True or False
        '''
        cur = self.head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                return True
            cur = cur.next
        print("删除失败, 该元素不存在")
        return False

    def find(self, val):
        '''
        查找元素, 返回True, 若未找到返回False
        '''
        cur = self.head.next
        while cur:
            if cur.val == val:
                return True
            cur = cur.next
        print("查找失败, 该元素不存在")
        return False
        
    def pprint(self):
        '''
        打印链表
        '''
        cur = self.head.next
        print_str = 'print:'
        while cur:
            print_str += '->' + str(cur.val)
            cur = cur.next
        print(print_str)

# 测试
if __name__ == '__main__':
    root = LinkList()
    root.init_by_array([1, 2, 3])
    root.pprint()
    root.insert(4)
    root.pprint()
    root.find(4)
    root.delete(4)
    root.pprint()

