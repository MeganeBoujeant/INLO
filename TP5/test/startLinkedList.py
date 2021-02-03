
# coding: utf-8
from linkedList import LinkedList
from linkedList import Node

if __name__ == "__main__":
    llist = LinkedList(["a", "b", "c", "d", "e"])
    llist.add_last(Node("g"))
    llist.add_first(Node("z"))
    llist.add_before("z", Node("y"))
    llist.add_before("y", Node("x"))
    llist.add_before("g", Node("f"))
    llist.add_after("g", Node("h"))
    #llist.add_before("q", Node("r"))
    #llist.remove_node("q")
    llist.remove_node("a")
    print(llist)
    llist.remove_node("x")
    print(llist)