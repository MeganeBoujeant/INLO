#!/usr/bin/env python
# -*- coding: utf-8 -*-

from node import Node


if __name__ == "__main__":
	n1 = Node(1)
	n2 = Node(5)
	n1.link  = n2
	print(n1)