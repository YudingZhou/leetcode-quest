# from typing import TypeVar, Generic
#
# T = TypeVar('T')
#
#
# class IList(Generic[T]):
#
#     def get(idx: int) -> T:
#         pass
#
#     def add(item: T):
#         pass
#
#     def addAt(idx: int, item: T):
#         pass
#
#     def deleteAt(idx: int):
#         pass
#
#     def size() -> int:
#         pass
#
#
# class LinkedList(IList):
#     class Node(Generic[T]):
#         def __init__(self, val: T):
#             self.next = None
#             self.val = val
#
#     def __init__(self):
#         self.size = 0
#         self.tail = None
#
#     def get(idx: int) -> T:  # O(n)
#         if idx >= size():
#             raise Error("out of boundary")
#         else:
#             Node
#             previous = tail
#             while idx - - != 0:
#                 previous = previous.next
#
#         return previous.next
#
#     def add(item: T):  # O(1)
#         if size() == 0:
#             self.tail = Node(item)
#             self.tail.next = self.tail
#         else:
#             Node
#             newNode = Node(item)
#             newNode.next = self.tail.next
#             self.tail.next = newNode
#
#     def addAt(idx: int, item: T):  # O(n)
#         if idx > size():
#             raise Error("out of boundary")
#         else:
#             Node
#             previous = tail
#             while idx - - != 0:
#                 previous = previous.next
#
#             Node
#             newNode = Node(item)
#             newNode.next = previous.next
#             previous.next = newNode
#
#     def deleteAt(idx: int):  # O(n)
#         if idx >= size() | | size() == 0:
#             raise Error("out of boundary")
#         if size() == 1:
#             tail = None
#         else:
#             Node
#             previous = tail
#
#             while idx - - != 0:
#                 previous = previous.next
#
#             previous.next = previous.next.next
#
#     def size() -> int:
#         return self.size
