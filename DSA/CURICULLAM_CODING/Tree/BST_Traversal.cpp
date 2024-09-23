#include<iostream>

using namespace std;

struct tree
{
    char data;
    tree* left;
    tree* right;
    
    tree(char val)
    {
         data = val;
         left = right = nullptr;
    }
};

tree* insert(tree* root , char data)
{
    //To check whether root node is empty
    if(root == nullptr)
    {
         return new tree(data);
    }
    //Check and insert on left data node
    if(data < root -> data)
    {
         root -> left = insert(root -> left , data);
    }
    else
    {    
         //else insert in right node
         root -> right = insert(root -> right , data);
    }
    return root;
}

void inorderTrav(tree* root)
{
     if(root != nullptr)
     {
          inorderTrav(root -> left);//traverse left node
          cout<<root -> data<<" "; //Processing the node
          inorderTrav(root -> right);//traverse right node
     }
}

void preorderTrav(tree* root)
{
     if(root != nullptr)
     {
         cout<<root -> data<<" ";//Processing the node
         preorderTrav(root -> left);//traverse the left node
         preorderTrav(root -> right);//traverse the right node
     }
}

int main()
{
     tree* root = nullptr;
     string name;
     
     cout<<"Enter you name: ";
     getline(cin , name);
     
     //Insert char of name inside BST
     for(char c : name)
     {
          if(c != ' ')
          {
               root = insert(root , c);
          }
     }
     
     // Perform Inorder and Preorder Traversals
     cout << "Inorder Traversal: ";
     inorderTrav(root);
     cout << endl;
     
     cout << "Preorder Traversal: ";
     preorderTrav(root);
     cout << endl;
     
     return 0;
}
