class Node {
	int key;
	Node left;
	Node right;
	int height;

	Node(int value) {
		key = value;
		left = null;
		right = null;
		height = 1;
	}
}

class AVLTree {
	Node root;

	int height(Node root) {
		if (root == null)
			return 0;

		return root.height;
	}

	int findHeight() {
		return height(root);
	}

	Node search(Node root, int value) {
		if (root == null)
			return null;
		else {
			if (value == root.key)
				return root;
			else if (value < root.key)
				return search(root.left, value);
			else
				return search(root.right, value);
		}
	}

	boolean find(int value) {
		Node node = search(root,value);

		if (node == null)
			return false;

		return true;
	}

	int max(int one, int two) {
		return (one > two) ? one : two;
	}

	Node insertNode(Node root, int value) {
		if (root == null)
			root = new Node(value);
		else {
			if (value < root.key)
				root.left = insertNode(root.left, value);
			else
				root.right = insertNode(root.right, value);
		}

		root.height = max(height(root.left), height(root.right)) + 1;

		return root;
	}

	void insert(int value) {
		root = insertNode(root, value);
	}

	void inorder(Node root) {
		if (root != null) {
			inorder(root.left);
			System.out.println(root.key);
			inorder(root.right);
		}
	}

	void inorderTraversal() {
		inorder(root);
	}
}

public class AVLTreeExample {
	public static void main(String[] args) {
		AVLTree avl = new AVLTree();
		avl.insert(20);
		avl.insert(30);
		avl.insert(10);
		avl.insert(5);

		avl.inorderTraversal();
		System.out.println("Searching for 10 : " + avl.find(10));
		System.out.println("Searching for 11 : " + avl.find(11));
		System.out.println("Searching for 20 : " + avl.find(20));
		System.out.println("Height of the tree : " + avl.findHeight());
	}
}
