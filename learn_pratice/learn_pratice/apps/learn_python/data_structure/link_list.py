

'''
一、链表简介
链表是一种在存储单元上非连续、非顺序的存储结构。数据元素的逻辑顺序是通过链表中的指针链接次序实现。
链表是由一系列的结点组成，结点可以在运行时动态生成。每个结点包含两部分：数据域与指针域。数据域存储数据元素，指针域存储下一结点的指针。

二、单向链表
单向链表也叫单链表，是链表中最简单的形式，它的每个节点包含两个域，一个信息域（元素域）和一个链接域。
这个链接指向链表中的下一个节点，而最后一个节点的链接域则指向一个空值
/imgs/link_list.jpg

head 保存首地址，item 存储数据，next 指向下一结点地址。

链表失去了序列的随机读取优点，同时链表增加了指针域，空间开销也较大，但它对存储空间的使用要相对灵活。

列如：有一堆数据[1,2,3,5,6,7]，要在3和5之间插入4,
如果用数组，需要将5之后的数据都往后退一位，然后再插入4，这样非常麻烦，但是如果用链表，我就直接在3和5之间插入4就行
'''


class Node(object):

    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(object):

    def __init__(self):
        self._head = None

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, node):
        self._head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        # 初始指针指向head
        cur = self._head
        count = 0
        # 指针指向None 表示到达尾部
        while cur is not None:
            count += 1
            # 指针下移
            cur = cur.next
        return count

    def items(self):
        """遍历链表"""
        # 获取head指针
        cur = self._head
        # 循环遍历
        while cur is not None:
            # 返回生成器
            yield cur.item
            # 指针下移
            cur = cur.next

    def add(self, item):
        """向链表头部添加元素"""
        node = Node(item)
        # 新结点指针指向原头部结点
        node.next = self._head
        # 头部结点指针修改为新结点
        self._head = node

    def append(self, item):
        """尾部添加元素"""
        node = Node(item)
        # 先判断是否为空链表
        if self.is_empty():
            # 空链表，_head 指向新结点
            self._head = node
        else:
            # 不是空链表，则找到尾部，将尾部next结点指向新结点
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, index, item):
        """指定位置插入元素"""
        # 指定位置在第一个元素之前，在头部插入
        if index <= 0:
            self.add(item)
        # 指定位置超过尾部，在尾部插入
        elif index > (self.length() - 1):
            self.append(item)
        else:
            # 创建元素结点
            node = Node(item)
            cur = self._head
            # 循环到需要插入的位置
            for i in range(index - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除节点"""
        cur = self._head
        pre = None
        while cur is not None:
            # 找到指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self._head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                return True
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next

    def find(self, item):
        """查找元素是否存在"""
        return item in self.items()

    # def is_empty(self):
    #     return self._head is None
    #
    # def length(self):
    #     cur = self._head
    #     count = 0
    #     while cur is not None:
    #         count += 1
    #         cur = cur.next
    #     return count
    #
    # def items(self):
    #     cur = self._head
    #     while cur is not None:
    #         yield cur.item
    #         cur = cur.next
    #
    # def add(self, item):
    #     node = Node(item)
    #     node.next = self._head
    #     self._head = node
    #
    # def append(self, item):
    #     node = Node(item)
    #     if self.is_empty():
    #         self._head = node
    #     else:
    #         cur = self._head
    #         while cur.next is not None:
    #             cur = cur.next
    #         cur.next = node
    #
    # def insert(self, index, item):
    #     if index <= 0:
    #         self.add(item)
    #     elif index > (self.length() - 1):
    #         self.append(item)
    #     else:
    #         node = Node(item)
    #         cur = self._head
    #         for _ in range(index - 1):
    #             cur = cur.next
    #         node.next = cur.next
    #         cur.next = node
    #
    # def remove(self, item):
    #     cur = self._head
    #     pre = None
    #     while cur is not None:
    #         if cur.item == item:
    #             if not pre:
    #                 self._head = cur.next
    #             else:
    #                 pre.next = cur.next
    #         else:
    #             pre = cur
    #             cur = cur.next



if __name__ == '__main__':
    link_list = SingleLinkList()
    node1 = Node(1)
    node2 = Node(2)
    link_list.head = node1
    node1.next = node2

    print(link_list.head.item)
    print(link_list.head.next.item)


'''
是不是感觉很麻烦，所以我们要在链表中增加操作方法。

is_empty() 链表是否为空
length() 链表长度
items() 获取链表数据迭代器
add(item) 链表头部添加元素
append(item) 链表尾部添加元素
insert(pos, item) 指定位置添加元素
remove(item) 删除节点
find(item) 查找节点是否存在
'''