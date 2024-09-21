#include <iostream>
using namespace std;

struct Node 
{
    int coeff;  
    int pow;    
    Node* next; //Point to the next term 
};


Node* createNode(int coeff, int pow) 
{
    Node* newNode = new Node();
    newNode->coeff = coeff;
    newNode->pow = pow;
    newNode->next = nullptr;
    return newNode;
}

void insertTerm(Node*& head, int coeff, int pow) 
{
    Node* newNode = createNode(coeff, pow);
    
    if (head == nullptr) 
    {
        head = newNode;
    } 
    else 
    {
        Node* temp = head;
        while (temp->next != nullptr) 
        {
            temp = temp->next;
        }
        temp->next = newNode;
    }
}

void displayPolynomial(Node* head) 
{
    if (head == nullptr) 
    {
        cout << "0";
        return;
    }
    Node* temp = head;
    while (temp != nullptr) 
    {
        cout << temp->coeff << "x^" << temp->pow;
        if (temp->next != nullptr) 
        {
            cout << " + ";
        }
        temp = temp->next;
    }
    cout << endl;
}

Node* subtractPolynomials(Node* poly1, Node* poly2) //to find the difference between two polynomials
{
    Node* result = nullptr;
    Node* temp1 = poly1;
    Node* temp2 = poly2;

    while (temp1 != nullptr && temp2 != nullptr) 
    {
        if (temp1->pow == temp2->pow) 
        {
            // Subtract coefficients with the same power
            int newCoeff = temp1->coeff - temp2->coeff;
            if (newCoeff != 0) 
            {
                insertTerm(result, newCoeff, temp1->pow);
            }
            temp1 = temp1->next;
            temp2 = temp2->next;
        } 
        else if (temp1->pow > temp2->pow) 
        {
            // Copy the term from the first polynomial
            insertTerm(result, temp1->coeff, temp1->pow);
            temp1 = temp1->next;
        } 
        else 
        {
            // Subtract the term from the second polynomial (negative of its coefficient)
            insertTerm(result, -temp2->coeff, temp2->pow);
            temp2 = temp2->next;
        }
    }

    // If any terms are left in the first polynomial, copy them
    while (temp1 != nullptr) 
    {
        insertTerm(result, temp1->coeff, temp1->pow);
        temp1 = temp1->next;
    }

    // If any terms are left in the second polynomial, subtract them (negative of their coefficients)
    while (temp2 != nullptr) 
    {
        insertTerm(result, -temp2->coeff, temp2->pow);
        temp2 = temp2->next;
    }

    return result;
}

int main() 
{
    Node* poly1 = nullptr;
    Node* poly2 = nullptr;
    
    int n1, n2;
    int coeff, pow;

    // Accept the first polynomial
    cout << "Enter the number of terms in the first polynomial: ";
    cin >> n1;
    cout << "Enter the terms (coefficient and power) for the first polynomial:\n";
    
    for (int i = 0; i < n1; i++) 
    {
        cout << "Coefficient: ";
        cin >> coeff;
        cout << "Power: ";
        cin >> pow;
        insertTerm(poly1, coeff, pow);
    }

    // Accept the second polynomial
    cout << "Enter the number of terms in the second polynomial: ";
    cin >> n2;
    cout << "Enter the terms (coefficient and power) for the second polynomial:\n";
    
    for (int i = 0; i < n2; i++) 
    {
        cout << "Coefficient: ";
        cin >> coeff;
        cout << "Power: ";
        cin >> pow;
        insertTerm(poly2, coeff, pow);
    }

    // Display both polynomials
    cout << "\nFirst Polynomial: ";
    displayPolynomial(poly1);

    cout << "Second Polynomial: ";
    displayPolynomial(poly2);

    // Find the difference of the two polynomials
    Node* result = subtractPolynomials(poly1, poly2);

    // Display the result
    cout << "\nDifference of the two polynomials: ";
    displayPolynomial(result);

    return 0;
}
