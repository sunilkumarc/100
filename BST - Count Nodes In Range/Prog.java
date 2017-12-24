// https://practice.geeksforgeeks.org/problems/count-bst-nodes-that-lie-in-a-given-range/1

/*
Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.*/

// A Binary Search Tree node
/*class Node
{
    int data;
    Node left, right;
    Node(int item)
    {
        data = item;
        left = right = null;
    }
}*/
class Prog
{   
    int getCount(Node root, int low, int high) {
        if (root == null)
            return 0;
            
        if (root.data >= low && root.data <= high) {
            return 1 + getCount(root.left, low, high) + getCount(root.right, low, high);
        } else {
            if (root.data < low) {
                return getCount(root.right, low, high);
            } else {
                return getCount(root.left, low, high);
            }
        }
    }
    
    int getCountOfNode(Node root, int low, int high) 
    {
        int res = getCount(root, low, high);
        return res;
    }
}