from typing import List
import numpy as np

from common.struct.node.binary import TreeNode

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        ret = []
        for loc1, num1 in enumerate(nums):
            for loc2, num2 in enumerate(nums[1:]):
                if num1 + num2 == target:
                    ret.append([num1, num2])
        print(ret)

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
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

    def lengthOfLongestSubstring3(self, s: str) -> int:
        """
        给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

        输入: s = "abcabcbb"
        输出: 3
        解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
        """
        longest_word = ""
        for i, from_word in enumerate(s):
            for j, to_word in enumerate(s[i + 1:]):
                if to_word in s[i:j + i + 1]:
                    if len(s[i:j + i + 1]) > len(longest_word):
                        longest_word = s[i:j + i + 1]
                    break
        return len(longest_word)

    def lengthOfLongestSubstring3_(self, s: str) -> int:
        word = ''
        loc = 0
        for i, itm in enumerate(s):
            if itm not in s[loc:i]:
                if len(s[loc:i + 1]) >= len(word):
                    word = s[loc:i+1]
            else:
                loc = loc + word.index(itm)+1
        return len(word)

    def findMedianSortedArrays4(self, nums1: List[int], nums2: List[int]) -> float:
        """
        4. 寻找两个正序数组的中位数
        输入：nums1 = [1,2], nums2 = [3,4]
        输出：2.50000
        解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
        :param self:
        :param nums1:
        :param nums2:
        :return:
        """
        stack = []
        while len(nums1) > 0 or len(nums2) > 0:
            if len(nums1) == 0 and len(nums2) == 0:
                break
            elif len(nums1) == 0 and len(nums2) > 0:
                stack.append(nums2[0])
                nums2.pop(0)
            elif len(nums1) > 0 and len(nums2) == 0:
                stack.append(nums1[0])
                nums1.pop(0)
            elif nums1[0] < nums2[0] or len(nums2) == 0:
                stack.append(nums1[0])
                nums1.pop(0)
            else:
                stack.append(nums2[0])
                nums2.pop(0)

        print(stack)
        while len(stack) > 2:
            stack.pop()
            stack.pop(0)
        return stack[0] if len(stack) == 1 else (stack[0] + stack[1]) / 2

    # def longestPalindrome5(self, s: str) -> int:
    #     max_length = 0
    #     word = None
    #     for i, from_word in enumerate(s):
    #         for j, to_word in enumerate(s[i + 1:]):
    #             if to_word == s[i]:
    #                 if len(s[i:j + i + 1]) > max_length:
    #                     word = s[i:j + i + 1]
    #                     max_length = len(word)
    #                 break
    #     print(word)

    def longestPalindrome5(self, s: str) -> str:
        if len(s) < 2:
            return s
        longest_word = ''
        for i, from_word in enumerate(s):
            for j, to_word in enumerate(s[i:]):
                if self.isPalindrome(s[i:i + j + 1]) and len(s[i:i + j + 1]) > len(longest_word):
                    print(longest_word)
                    longest_word = s[i:j + i + 1]
        return longest_word

    def isPalindrome(self, s: str) -> bool:
        stack = list(s)
        while stack:
            if len(stack) < 2:
                break
            if len(stack) > 1:
                left = stack.pop(0)
                right = stack.pop()
                if left != right:
                    return False
        return True



    def convert6(self, s: str, numRows: int) -> str:
        str = "LEETCODEISHIRING"
        ret = int[numRows]

        col = []
        for i in range(numRows):
            col.append()


    def intToRoman(num: int) -> str:
        pass


    def ff(self):
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

    def reverse7(self, x: int) -> int:
        stack = []
        gt = (x >= 0)

        absx = abs(x)
        while absx != 0:
            if absx < 10:
                yu = absx
            else:
                yu = absx % 10
            stack.append(yu)
            absx = (absx-yu) / 10

        ret = 0
        while len(stack) > 0:
            i = stack.pop(0)
            ret = ret * 10 + i

        ret = 0 if int(ret) > pow(2, 31) -1 else int(ret)
        return ret if gt else -ret



    def lengthOfLongestSubstring(s: str) -> int:
        word = ''
        loc = 0
        for i, itm_i in enumerate(s):
            if itm_i not in s[loc:i]:
                if len(s[loc:i + 1]) >= len(word):
                    word = s[loc:i+1]
            else:
                loc = loc + word.index(itm_i)+1
        return len(word)


    def isPalindrome9(self, x: int) -> bool:
        """
        回文
        :param x:
        :return:
        """
        s = list(str(x))
        while len(s) > 1:
            l = s.pop(0)
            r = s.pop()
            if (l != r):
                return False
        return True



    def longestCommonPrefix14(self, strs: List[str]) -> str:
        """
        最长公共前缀
            输入：strs = ["flower","flow","flight"]
            输出："fl"
        :param strs:
        :return:
        """
        c = None
        word = []
        loc = -1
        stop = False
        if len(strs) == 1:
            word = strs[0]
        else:
            while not stop:
                loc += 1
                for i, itm in enumerate(strs):
                    if loc > len(itm) -1:
                        stop = True
                        break
                    elif i == 0:
                        c = itm[loc]
                    elif itm[loc] == c:
                        if i == len(strs) - 1:
                            word.append(c)
                    else:
                        stop = True
                        break
        return "".join(word)









    def threeSum5_(self, nums: List[int]) -> List[List[int]]:
        """
        给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
        :param nums:
        :return:
        """
        def do(nums: List[int], stack: List[int]) -> List[List[int]]:
            if len(stack) == 3:
                if sum(stack) == 0:
                    result.append(stack[:])
                return

            totals = nums[:]
            for i in stack:
                totals.remove(i)

            for s in totals:
                stack.append(s)
                do(nums, stack)
                stack.pop()

        result = []
        stack = []
        do(nums, stack)

        # for i in result:
        #     i.sort()
        # res = []
        # for i in result:
        #     if i not in res:
        #         res.append(i)

        return result








    def threeSumClosest16(self, nums: List[int], target: int) -> int:
        """
        最接近三数之和
        输入：nums = [-1,2,1,-4], target = 1
        输出：2
        解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
        :param nums:
        :param target:
        :return:
        """
        def do(nums: List[int], stack: List[int]) -> List[List[int]]:
            if len(stack) == 3:
                nonlocal result
                nonlocal target
                if result is None or abs(stack[0] + stack[1] + stack[2] - target) < abs(
                        result[0] + result[1] + result[2] - target):
                    result = stack[:]
                return

            totals = nums[:]
            for i in stack:
                totals.remove(i)

            for s in totals:
                stack.append(s)
                do(nums, stack)
                stack.pop()

        result = None
        stack = []
        sum_no = 0
        do(nums, stack)

        return sum(result)



    def letterCombinations17(self, digits: str) -> List[str]:
        if digits == "":
            return []
        MAP = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        results = ['']

        for num in digits:
            results = [r + d for r in results for d in MAP[num]]
        return results



    def searchInsert35(self, nums: List[int], target: int) -> int:
        loc = -1
        for i, itm in enumerate(nums):
            if target <= itm:
                # print(i)
                loc = i
                nums.insert(i, itm)
                # print(nums)
                break
            if i == len(nums) - 1:
                loc = len(nums)
                nums.insert(i + 1, itm)
                break
        return loc



    def isValidSudoku36(self, board: List[List[str]]) -> bool:
        # bo = np.array([np.array(i) for i in board])
        bo = np.array(board)
        for row in bo:
            # r = np.setdiff1d(row,'.')
            r = np.array(row[row != '.'])
            if len(r) != len(set(r)):
                # print(set(r))
                return False
        for i in range(8):
            col = np.array(bo[:,i])
            # c = np.setdiff1d(col,'.')
            # print(bo[:,i])
            c = col[col != '.']
            if len(c) != len(set(c)):
                return False
        # print(bo[0,:])
        # print(bo[:,])

        for row in [[0,1,2],[3,4,5],[6,7,8]]:
            for col in [[0,1,2],[3,4,5],[6,7,8]]:
                local9 = np.array([bo[i,j] for i in row for j in col])
                # local9 = np.setdiff1d(local9,'.')
                # print(type(local9))
                # print(local9)
                loc = local9[local9 != '.']
                print(loc)
                if len(loc) != len(set(loc)):
                    # print(set(loc))
                    return False
        return True


    def threeSum15(self, nums: List[int]) -> List[List[int]]:
        """
        三数之和
        输入：nums = [-1,0,1,2,-1,-4]
        输出：[[-1,-1,2],[-1,0,1]]
        :param nums:
        :return:
        """
        def do(nums: List[int], stack: List[int]) -> List[List[int]]:
            if len(stack) == 3:
                print(stack)
                if sum(stack) == 0:
                    result.append(stack[:])
                return

            totals = nums[:]
            for i in stack:
                totals.remove(i)

            for s in totals:
                stack.append(s)
                do(nums, stack)
                stack.pop(0)

        result = []
        stack = []
        do(nums, stack)
        return result









    def longestCommonPrefix(self, strs: List[str]) -> str:
        c = None
        word = []
        loc = -1
        stop = False
        while not stop:
            loc += 1
            for i, itm in enumerate(strs):
                if loc > len(itm) - 1:
                    stop = True
                    break
                elif i == 0:
                    c = itm[loc]
                elif itm[loc] == c:
                    if i == len(strs) - 1:
                        word.append(c)
                    continue
        return "".join(word)















# 102
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def backtrace(root: TreeNode, stack: List[TreeNode]):
            if root is None:
                return []

            st = []
            if root.left is not None and root.right is not None:
                st.append([root.left, root.right])
                result.append(st)

            # if root.left is None and root.right is None:
            #     return

            left = root.left
            if left is not None:
                stack.append(left)
                backtrace(left, stack)
                stack.pop()

            right = root.right
            if right is not None:
                stack.append(right)
                backtrace(right, stack)
                stack.pop()

        stacks = []
        result = []
        backtrace(root, stacks)
        return result

#104
