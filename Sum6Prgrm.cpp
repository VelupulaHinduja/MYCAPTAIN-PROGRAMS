#include<stdio.h>
int sum(int n){
	if(n>0){
		return(n%10+sum(n/10));
	}
	else
	{
		return(0);
	}
}
int main(){
	int n;
	 printf("Enter number");
	 scanf("%d",&n);
	 printf("The sum of digits is :%d",sum(n));
}
