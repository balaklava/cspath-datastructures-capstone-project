from hashmap import HashMap
from linkedlist import LinkedList
from linkedlist import Node

###########################################
# hashmap usage

hash_map = HashMap(15)
hash_map.assign(key="gabbro", value="igneous")
hash_map.assign(key="sandstone", value="sedimentary")
hash_map.assign(key="gneiss", value="metamorphic")

print(hash_map.retrieve("gabbro"))
print(hash_map.retrieve("sandstone"))
print(hash_map.retrieve("gneiss"))



############################################
# Node class usage

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

print(n1.get_value(), n1.get_next_node())
print(n2.get_value(), n2.get_next_node())
print(n3.get_value(), n3.get_next_node())
print()

n1.set_next_node(n2)
n2.set_next_node(n3)

print(n1.get_value(), n1.get_next_node())
print(n2.get_value(), n2.get_next_node())
print(n3.get_value(), n3.get_next_node())
print()

print(n1.get_value(), n1.get_next_node().get_value())
print(n2.get_value(), n2.get_next_node().get_value())
print(n3.get_value(), n3.get_next_node())



#############################################
# LinkedList usage

ll = LinkedList()
print()
print(ll)

ll.insert_beginning(5)
ll.insert_beginning(15)
ll.insert_beginning(25)

print(ll.get_head_node())
print(ll.get_head_node().get_value())
print()

print(ll.stringify_list())

head_node = ll.get_head_node()
print(head_node.get_value())
print(head_node.get_next_node().get_value())
print()

ll.remove_node(head_node.get_value())
print(ll.stringify_list())






