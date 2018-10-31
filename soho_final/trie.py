class Node:

  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next_node(self):
    return self.next_node


class Trie:

  def __init__(self, Node):
    self.Node = Node

  def get_head_node(self):
    return self.head_node



