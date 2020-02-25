//https://leetcode.com/problems/non-decreasing-array/
int checkPossibility(int *nums, int numsSize)
{
    int toModify = 0;
    for (int i = 1; i < numsSize; i++)
    {
        if (nums[i] < nums[i - 1])
        {
            if (++toModify > 1)
                return (0);
            if (i > 1 && nums[i] < nums[i - 2] && i < numsSize - 1 && nums[i + 1] < nums[i - 1])
                return (0);
        }
    }

    return (1);
}
