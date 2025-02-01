int removeElement(int* nums, int numsSize, int val) {
    int ptr=0;
    for(int i=0;i<numsSize;i++)
    {
        if(nums[i]!=val)
        {
            nums[ptr]=nums[i];
            ptr++;
        }
    }
    return ptr;
}