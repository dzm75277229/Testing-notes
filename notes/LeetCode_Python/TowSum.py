int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int *a;
    a=(int *)malloc(2*sizeof(int));//用a数组返回结果
    for(int i=0;i<numsSize;i++){
        for(int j=i+1;j<numsSize;j++){
            if(nums[i]+nums[j]==target){
                a[0]=i;
                a[1]=j;
                break;
            }
        }
    }
    return a;
}
