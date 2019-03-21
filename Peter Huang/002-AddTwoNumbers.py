calss ListNode:
	def __init__(self, x):
		self.var = x
		self.next = None

def add_two_numbers(linked_list_01,linked_list_02):
	res = []
	if linked_list_01.var + linked_list_02.var >= 10:
		linked_list_01.next.var += 1
		res.append(linked_list_01.var + linked_list_02.var - 10)
	else:
		res.var = linked_list_01.var + linked_list_02.var
	while linked_list_01.next != None:
		if linked_list_01.next.var + linked_list_02.next.var >= 10:
			linked_list_01.next.next.var +=1
			linked_list_01.next = linked_list_01.next.next
			linked_list_02.next = linked_list_02.next.next
			res.append(linked_list_01.var + linked_list_02.var - 10)
		else:
			res.append(linked_list_01.var + linked_list_02.var)
			linked_list_01 = linked_list_01.next
			linked_list_02 = linked_list_02.next
	return res

def change_list_into_linkedlist(list):
	linked_list = ListNode()
	

def mian(list_01,list_02):
	linked_list_01 = ListNode()
	add_two_numbers()