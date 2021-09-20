from typing import List


def twoSum1(nums: List[int], target: int) -> List[int]:
    ret = []
    for loc1, num1 in enumerate(nums):
        for loc2, num2 in enumerate(nums[1:]):
            if num1 + num2 == target:
                ret.append([num1, num2])
    print(ret)


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers2(l1: ListNode, l2: ListNode) -> ListNode:
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    num1 = 0
    num2 = 0
    i = 0
    while l1 is not None:
        num1 = num1 + l1.val * (10 ** i)
        l1 = l1.next
        i = i + 1

    i = 0
    while l2 is not None:
        num2 = num2 + l2.val * (10 ** i)
        l2 = l2.next
        i = i + 1
    print(num1)
    print(num2)
    num = num1 + num2

    i = 1
    first = ListNode(num % 10)
    num = int(num / 10)
    tmp = first
    while num > 0:
        mod = num % 10
        tmp.next = ListNode(mod)
        tmp = tmp.next
        num = int(num / 10)
    print(first)


def lengthOfLongestSubstring3(s: str) -> int:
    max_length = 0
    word = None
    for i, from_word in enumerate(s):
        for j, to_word in enumerate(s[i + 1:]):
            if to_word in s[i:j + i + 1]:
                if len(s[i:j + i + 1]) > max_length:
                    word = s[i:j + i + 1]
                    max_length = len(word)
                break
    print(word)


def longestPalindrome4(s: str) -> int:
    max_length = 0
    word = None
    for i, from_word in enumerate(s):
        for j, to_word in enumerate(s[i + 1:]):
            if to_word == s[i]:
                if len(s[i:j + i + 1]) > max_length:
                    word = s[i:j + i + 1]
                    max_length = len(word)
                break
    print(word)


def convert6(s: str, numRows: int) -> str:
    str = "LEETCODEISHIRING"
    ret = int[numRows]

    col = []
    for i in range(numRows):
        col.append()


def intToRoman(num: int) -> str:
    pass


def ff():
    src = [1, 1, 2, 3, 4, 5, 1]
    length = len(src)
    trgt = [1 for i in range(length - 2)]
    left = [1 for i in range(length - 2)]
    right = [1 for i in range(length - 2)]
    for i, cur in enumerate(src):
        if i == 0 or i == length - 1 - 1:
            continue
        if i == length - 1 - 1:
            break
        if i == 1:
            left[i - 1] = src[i - 1]
            continue
        if i == length - 1 - 1 - 1:
            right[i + 1] = src[i + 1]
            continue

        left[i - 1] = left[i - 2] * src[i - 1]
        right[i + 1] = right[i + 2] * src[i + 1]

    print(left)
    print(right)
