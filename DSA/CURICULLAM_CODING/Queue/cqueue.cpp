#include <iostream>

#define MAX 100  // Define the queue limit

using namespace std;

class CQueue 
{
    private:
        int size;
        int front;
        int rear;
        int arr[MAX]; // Create array holds maximum memory of queue initially

    public:
        CQueue(int n) 
        {
            front = -1; 
            rear = -1;
            size = n;  // Assign size of queue to the token_no
        }

        bool isEmpty() 
        {
            return (front == -1);
        }

        bool isFull() 
        {
            return ((rear + 1) % size == front);
        }

        void cenqueue(int value) 
        {
            if (isFull()) // display queue is full
            {
                cout << "Circular Queue is full, Insertion is not possible \n";
                return;
            }	 	  	 	   	      	 	      		     	      	 	

            if (isEmpty()) // If queue is empty set front = 0
            {
                front = 0;
            }

            rear = (rear + 1) % size; // Increment rear and perform modulo (%) operation to join rear to front at the end of queue
            arr[rear] = value;  // Assign the rear pos element to value
        }

        void cdequeue() 
        {
            if (isEmpty()) 
            {
                cout << "Circular Queue is empty, Deletion is not possible \n";
                return;
            }

            int value = arr[front]; // Assign value and place front pointer 
            cout << "Deleted value: " << value << endl;

            if (front == rear) 
            {
                front = rear = -1;  // Queue is now empty
            } 
            else 
            {
                front = (front + 1) % size; // If front and rear are not in the same place then perform modulo again to connect back the queue for efficient memory usage
            }
        }

        void display() 
        {
            if (isEmpty()) 
            {
                cout << "Queue is empty \n";
                return;
            }	 	  	 	   	      	 	      		     	      	 	

            cout << "Queue contents are: \n";
            int i = front;

            while (true) 
            {
                cout << arr[i] << " ";
                if (i == rear) 
                    break;
                i = (i + 1) % size;
            }
            cout << endl;
        }
};

int main() 
{
    int n;
    cout << "Enter the number of patients (size of queue): \n";
    cin >> n; 

    CQueue q(n);

    int ch;
    do 
    {
        cout << "\nMenu: \n1. Insert into circular queue \n2. Delete from circular queue \n3. Display \n4. Exit\n";
        cin >> ch;

        switch (ch) 
        {
            case 1: 
            {
                if (!q.isFull()) 
                {
                    int token_no;
                    cout << "Enter the token number: \n";
                    cin >> token_no;  // Input the token number of patients
                    q.cenqueue(token_no);
                }	 	  	 	   	      	 	      		     	      	 	
                else 
                {
                    cout << "Queue is full!\n";
                }
                break;
            }

            case 2:
                q.cdequeue();
                break;
        
            case 3:
                q.display();
                break;
             
            case 4:
                exit(0);
    
            default: 
                cout << "\nError in the queue operation\n";
        }
    } 
    while (ch != 4);

    return 0;
}
	 	  	 	   	      	 	      		     	      	 	
