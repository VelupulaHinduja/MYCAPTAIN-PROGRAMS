#include<iostream>
using namespace std;
int ifprime(int num);
int main(){
	int n,i;
	cout<<"Enter a positive integer:";
	cin>>n;
	if(ifprime(n-2)){
		cout<<n<<"= 2"<<" + "<<(n-2)<<endl;
	}
	for(i=3;i<=(n/2);i+=2){
		if(ifprime(i) && ifprime(n-i))
			cout<<n<<"= "<<i<<" + "<<(n-i)<<endl;
	}
	
}
int ifprime(int num){
	int i=2;
	if(num==1)
	return(0);
	for(i=2;i<num;i++)
	{
		if(num%i==0)
		{
			return(0);
		}
	}
	if(i==num)
	{
		return(1);
	}
}
