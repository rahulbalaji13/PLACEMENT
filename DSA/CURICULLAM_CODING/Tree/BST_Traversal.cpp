#include<iostream>
#include<vector>
#include<string>

using namespace std;

struct tnode
{
     char data;
     tnode* left;
     tnode* right;
     
     tnode(char val)
     {
         data = val;
         left = nullptr;
         right = nullptr;
     }
};

tnode* insert(tnode* root, char data)
{
     if(root == nullptr)
     {
         return new tnode(data); 
     }
     
     if(data < root -> data)
     {
         root -> left = insert(root -> left , data);
     }
     
     else if(data > root -> data)
             {
                 root -> right = insert(root -> right , data);
             }
     
     return root;
}

void preorder(tnode* root)
{
     if(root != nullptr)
     {
         cout<<root -> data<<" ";
         preorder(root -> left);
         preorder(root -> right);
     }
}

void inorder(tnode* root)
{
     if(root != nullptr)
     {
         inorder(root -> left);
         cout<<root -> data<<" ";
         inorder(root -> right);
     }
}

int main()
{
     string name;
     
     cout<<"Enter the name: ";
     cin>>name;
     
     tnode* root = nullptr;
     
     for(char ch: name)
     {
         root = insert(root , ch);
     }
     
     cout<<"Preorder: ";
     preorder(root);
     cout<<endl;
     
     cout<<"Inorder: ";
     inorder(root);
     cout<<endl;
     
     return 0;
}
