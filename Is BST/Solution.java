/*
Link: https://www.hackerrank.com/challenges/is-binary-search-tree
Hidden stub code will pass a root argument to the function below. Complete the function to solve the challenge. Hint: you may want to write one or more helper functions.

The Node class is defined as follows:
    class Node {
        int data;
        Node left;
        Node right;
    }
*/
boolean checkBSTUtil(Node root, int min, int max) {
	if (root == null)
		return true;

	if (root.data < min || root.data > max)
		return false;

	return checkBSTUtil(root.left, min, root.data - 1) && checkBSTUtil(root.right, root.data + 1, max);
}

boolean checkBST(Node root) {
	return checkBSTUtil(root, 0, 10000);
}
