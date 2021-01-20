#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node:

	def __init__(self, param_data):
		self.data = param_data
		self.link = None

	def __str__(self):
		node_list = []
		node = self
		while node.link != None:
			node_list.append(node.data)
			node = node.link
		node_list.append(node.data)
		return str(node_list)

