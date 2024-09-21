#include <iostream>
#include <string>

using namespace std;

struct Student 
{
    int regNo;
    string name;
    int age;
    Student* next;
};

Student* createStudent(int regNo, string name, int age) //create node 
{
    Student* newStudent = new Student();
    newStudent->regNo = regNo;
    newStudent->name = name;
    newStudent->age = age;
    newStudent->next = nullptr;
    return newStudent;
}

void displayList(Student* head) //Display the cll
{
    if (head == nullptr) 
    {
        cout << "The list is empty.\n";
        return;
    }

    Student* temp = head;
    do 
    {
        cout << "RegNo: " << temp->regNo << ", Name: " << temp->name << ", Age: " << temp->age << endl;
        temp = temp->next;
        
    } while (temp != head);
}

void addStudent(Student*& head, int regNo, string name, int age) //add node at last of the cll
{
    Student* newStudent = createStudent(regNo, name, age);
    
    if (head == nullptr)
    {
        head = newStudent;
        newStudent->next = head;  // Circular link
    } 
    else 
    {
        Student* temp = head;
        
        while (temp->next != head) 
        {
            temp = temp->next;
        }
        temp->next = newStudent;
        newStudent->next = head;  // Circular link
    }
    displayList(head);
}

void removeStudent(Student*& head, int n) //remove nth node from cll
{
    if (head == nullptr) 
    {
        cout << "The list is empty, cannot remove.\n";
        return;
    }

    Student* temp = head;
    Student* prev = nullptr;

    // If the head node is to be removed
    if (n == 1) 
    {
        // If there's only one node in the list
        if (head->next == head) 
        {
            delete head;
            head = nullptr;
        } else 
        {
            // Find the last node
            while (temp->next != head) 
            {
                temp = temp->next;
            }
            
            Student* toDelete = head;
            temp->next = head->next;
            head = head->next;
            delete toDelete;
        }
        displayList(head);
        return;
    }

    // Traverse to the nth node
    temp = head;
    for (int i = 1; i < n; ++i) 
    {
        prev = temp;
        temp = temp->next;
        if (temp == head)
        {
            cout << "The position exceeds the number of students.\n";
            return;
        }
    }
    
    prev->next = temp->next;
    delete temp;
    displayList(head);
}

int main() 
{
    Student* head = nullptr;
    int choice, regNo, age, pos;
    string name;

    do 
    {
        cout << "\nMenu:\n";
        cout << "1. Add Student\n";
        cout << "2. Remove nth Student\n";
        cout << "3. Display List\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) 
        {
         case 1:
            cout << "Enter Register Number: ";
            cin >> regNo;
            cout << "Enter Name: ";
            cin.ignore();
            getline(cin, name);
            cout << "Enter Age: ";
            cin >> age;
            addStudent(head, regNo, name, age);
            break;
         
         case 2:
            cout << "Enter position to remove: ";
            cin >> pos;
            removeStudent(head, pos);
            break;
         
         case 3:
            displayList(head);
            break;
        
        case 4:
            cout << "Exiting...\n";
            break;
        
         default:
            cout << "Invalid choice. Try again.\n";
        }
    }  
     while (choice != 4);

     return 0;
}
