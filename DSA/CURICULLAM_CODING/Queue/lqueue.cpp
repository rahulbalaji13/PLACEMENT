#include<iostream>

#define MAX 50

using namespace std;

class Queue   //Queue class is best method to access variables all over the functions
{
  private:
            int front, rear, size;
                        
            int arr[MAX];
  
  public:
   
   Queue(int n)   //Constructor of Queue class in declared here...
   {
     front = 0;
     rear = -1;
     size = n;
     int value;
   }
   
   bool isFull()
   {
     return rear == size - 1;
   }
   
   void enqueue(int value)
   {
     if(isFull())
     {
         cout<<"Queue is full\n";
     }
       else
     {
         //rear = rear + 1;
         arr[++rear] = value;
         
         cout<<value<<" inserted into the queue\n"<<endl;
     }
   }
   
   void dequeue()
   {
       if(front == -1)
       {
           cout<<"Queue is empty\n";
           exit(0);
       }
       else
       {
           cout<<arr[front++]<<" is deleted from the queue\n"<<endl;
       }
   }
   
   void display()
   {
       if(front == -1)
       {
           cout<<"Queue is empty \n";
           exit(0);
       }
       else
       {
       
       cout<<"Queue contents are: \n";
       
       for(int i = front; i <= rear; i++)
       {
          cout<<arr[i]<<" ";
       }
       }
   }
   
};

int main()
{
  int height, n;
  
  cout<<"Enter the number of students: \n";
  cin>>n;
    
  Queue q(n);    //class Queue is assigned as variable 'q' with the function call of size/number of students
  
  int ch;
  
  do
  {
  cout<<"\n Menu: \n 1.Enqueue \n 2.Dequeue \n 3.Display \n 4.Exit\n"; 
  
  cout<<"Enter the choice: \n";
  cin>>ch;
  
  switch(ch)
  {
     case 1: 
             if(!q.isFull())
             {
             cout<<"Enter the height: \n";
             cin>>height;
             q.enqueue(height);
             }
             break;
             
             
      case 2: 
              q.dequeue();
              break;
             
              
      case 3: 
              q.display();
              break;
              
      case 4:
              cout<<"Exit..... \n";
              exit(0);
              
      default:
                cout<<"Please, Choose the correct option \n";
  
    }
  }
     while(ch != 4); 
   
    return 0;

}
