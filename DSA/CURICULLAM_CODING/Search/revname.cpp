#include<iostream>
#include<vector>
#include<string>

using namespace std;

void revname(string &rstr, int begin, int last)
{
  if(begin >= last) //Compare the beginning and ending values
  {
    return;  //Return that beginnning letter was greater than ending letter
  }
  //Swap the beginning and ending characters
  
  char temp = rstr[begin];
  rstr[begin] = rstr[last];
  rstr[last] = temp;
  
  revname(rstr, begin + 1, last - 1); //Decrement the ending to reverse the string rstr given as input
}


int main()
{
  
  string myname;
  
  cout<<"My name is: ";
  getline(cin , myname);  //use getline to read the input of string letters
  
  revname(myname , 0 , myname.length()-1);  //Reverse the length of the name entered by decrementing the length of entered name
  
  cout<<"My reversed name is: "<<myname;
  
  return 0;
  
}	 	  	 	   	      	 	      		     	      	 	
