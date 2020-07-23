#include<iostream>
using namespace std;
int main(){
	int ar[5],*p;
	cout<<"Enter elements:";
	for(int i=0;i<5;i++){
		cin>>ar[i];
	}
	p=ar;
	cout<<"You entered:";
	for(int i=0;i<5;i++){
		cout<<*p<<endl;
		p++;
	}
}
