class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        # the idea here is to iterate all the numbers and pick the numbers range that should satisify one codition current_number = 1 + previous_number which ever satisfies we should move to next element unless and until the numbers are present in the array that could be a parit ex 2,3,4,5,6,8,9 => here 2->6 can be a pairt the loop will break at 6,8 where 8 is not satisfying the thumb rule which is current_number = 1 + previous_number
        result = list()

        # handling empty array
        if not nums:
            return result

        # initiating start and previous with 0th element of the array
        start = nums[0]
        previous = nums[0]

        # no iterating from the first element of the array
        for current in nums[1:]:
            # validating the thumb rule
            if current == 1 + previous:
                # then we will assign previous to current
                previous = current
            else:
                if start == previous:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{previous}")
                # setting up a new range
                start = current
                previous = current
        # for the final unfinished ranges
        # for the single element
        if start == previous:
            result.append(str(start))
        else:
            result.append(f"{start}->{previous}")
        return result    