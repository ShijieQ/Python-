class Solution:
    def twoSum(self, nums, target):
        mp = {}
        for i in range(len(nums)):
            if nums[i] in mp:
                return [mp[nums[i]], i]
            else:
                mp[target - nums[i]] = i


import json
def stringToIntegerList(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

def main():
    import io
    import sys
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            line = next(lines)
            target = int(line);
            
            ret = Solution().twoSum(nums, target)
            if ret:
                out = integerListToString(ret);
                print(out)
            else:
                print("NULL")
        except StopIteration:
            break

if __name__ == '__main__':
    main()