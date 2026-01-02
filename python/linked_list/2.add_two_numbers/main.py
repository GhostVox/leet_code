from typing import Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers_unified(l1, l2):
    dummy = ListNode()
    curr = dummy
    carry = 0

    # Run as long as there is ANY data left to process
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # New sum logic
        total = val1 + val2 + carry
        carry = total // 10
        curr.next = ListNode(total % 10)

        # Advance pointers safely
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


def add_two_numbersv(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    carry = 0
    dummy_node: ListNode = ListNode()
    tail_node = dummy_node
    while (
        l1 is not None and l2 is not None
    ):  # Handles case where both list contain nodes
        new_node, carry = add_nodes(
            l1, l2, carry
        )  # we add the nodes together get the next node
        dummy_node.next = new_node
        dummy_node = new_node
        l1 = l1.next  # shift down line
        l2 = l2.next  # shift down line
    if l1 is None and l2 is not None:
        dummy_node, carry = finish_linking(dummy_node, l2, carry)

    if l2 is None and l1 is not None:
        dummy_node, carry = finish_linking(dummy_node, l1, carry)

    if carry > 0:
        dummy_node.next = ListNode(carry)
        dummy_node = dummy_node.next
    # Trunacate the first node in the list so we start with the first node given from add.
    return tail_node.next


def finish_linking(answer_head: ListNode, cp_head: ListNode, carry: int):
    while cp_head.next is not None:
        new_node, carry = add_nodes(cp_head, ListNode(0), carry)
        answer_head.next = new_node
        answer_head = new_node
        cp_head = cp_head.next
    new_node, carry = add_nodes(cp_head, ListNode(0), carry)
    answer_head.next = new_node
    answer_head = new_node

    return answer_head, carry


def add_nodes(n1: ListNode, n2: ListNode, carry: int) -> Tuple[ListNode, int]:
    sum = n1.val + n2.val + carry
    carry = sum // 10
    value = sum % 10
    return (ListNode(value), carry)
