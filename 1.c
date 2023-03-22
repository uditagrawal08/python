#include<stdio.h>
void containsDuplicate(int* nums, int numsSize)
{
int temp,min,i,j;
    for(i=0;i<numsSize;i++)
    {
        min=i;
        for(j=i+1;j<numsSize;j++)
        {
            if(nums[j]<nums[min])
            min=j;
        }
        if(min!=i)
        {
            temp=nums[i];
            nums[i]=nums[min];
            nums[min]=temp;
            }}
            for(int i=0;i<numsSize;i++)
            {
                printf("%d",nums[i]);
            }
}
void main()
{   int numsSize=6;
    int arr[6]={0,4,2,5,3,6};
    containsDuplicate(arr,numsSize);
    
}