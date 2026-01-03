import pytest
from main import ListNode, add_two_numbers, add_nodes, finish_linking


def create_linked_list(values):
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    """Helper function to convert a linked list to a Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


class TestAddTwoNumbers:
    def test_example_1(self):
        # Input: l1 = [2,4,3], l2 = [5,6,4]
        # Output: [7,0,8]
        # Explanation: 342 + 465 = 807
        l1 = create_linked_list([2, 4, 3])
        l2 = create_linked_list([5, 6, 4])
        result = add_two_numbers(l1, l2)
        assert linked_list_to_list(result) == [7, 0, 8]

    def test_example_2(self):
        # Input: l1 = [0], l2 = [0]
        # Output: [0]
        l1 = create_linked_list([0])
        l2 = create_linked_list([0])
        result = add_two_numbers(l1, l2)
        assert linked_list_to_list(result) == [0]

    def test_different_lengths_l1_longer(self):
        # Input: l1 = [9,9,9,9], l2 = [9,9]
        # Output: [8,9,0,0,1]
        # Explanation: 9999 + 99 = 10098
        l1 = create_linked_list([9, 9, 9, 9])
        l2 = create_linked_list([9, 9])
        result = add_two_numbers(l1, l2)
        assert linked_list_to_list(result) == [8, 9, 0, 0, 1]

    def test_different_lengths_l2_longer(self):
        # Input: l1 = [1], l2 = [9,9,9]
        # Output: [0,0,0,1]
        # Explanation: 1 + 999 = 1000
        l1 = create_linked_list([1])
        l2 = create_linked_list([9, 9, 9])
        result = add_two_numbers(l1, l2)
        assert linked_list_to_list(result) == [0, 0, 0, 1]

    def test_single_digit_with_carry(self):
        l1 = create_linked_list([5])
        l2 = create_linked_list([5])
        result = add_two_numbers(l1, l2)
        assert linked_list_to_list(result) == [0, 1]
