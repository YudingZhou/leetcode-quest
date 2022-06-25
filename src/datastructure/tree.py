
from typing import TypeVar, Generic

T = TypeVar("T")


class N(Generic[T]):
	def __init__(self, val: T):
		self.left = None
		self.right = None
		self.val = val
 