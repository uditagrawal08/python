#include<stdio.h>

int add(int arr[])
{
      int len = sizeof(arr)/sizeof(arr[0]);

  int sum=0;
    if(len==0)
    return sum;
    else
    sum=sum(arr[len-1])+sum;
    
}
void main()
{
    int arr[]={1,2,3,4,5};
    printf("%d",len);
  printf("%d",add(arr));
}