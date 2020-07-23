#include<iostream>
using namespace std;
int main(){
	int age;
	cout<<"Enter Age of a user :";
	cin>>age;
	if(age>=18){
		cout<<"\nYou are eligible";
	}
	else{
		cout<<"\nYou are not eligible for voting\n";
		cout<<"Wait for "<<18-age<<"year(s)";
	}
}
