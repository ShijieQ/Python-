# 0001.py
# author: ShijieQ   email: ShijieQ@outlook.com
# created 2019-07-07T12:54:48.703Z+08:00

import json


class Solution:
    def twonums(self, nums, target):
        mp = {}
        for i in range(len(nums)):
            if nums[i] in mp:
                return [mp[nums[i]], i]
            else:
                mp[target - nums[i]] = i


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


if __name__ == '__main__':
    ret = Solution().twonums([2, 7, 11, 15], 9)
    ans = integerListToString(ret)
    print(ans)
