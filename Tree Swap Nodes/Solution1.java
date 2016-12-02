// https://www.hackerrank.com/challenges/swap-nodes-algo

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

class Node {
	int data;
	Node left;
	Node right;

	Node(int data) {
		this.data = data;
		this.left = null;
		this.right = null;
	}
}

class Tree {
	List<Node> nodes = new ArrayList<>();

	Tree(int N) {
		for (int i = 0; i <= N; ++i) {
			Node node = new Node(i);
			nodes.add(node);
		}
	}

	void insert(int index, int l, int r) {
		if (l == -1)
			nodes.get(index).left = null;
		else
			nodes.get(index).left = nodes.get(l);

		if (r == -1)
			nodes.get(index).right = null;
		else
			nodes.get(index).right = nodes.get(r);
	}

	void inorderTraversal(Node root) {
		if (root != null) {
			inorderTraversal(root.left);
			System.out.print(root.data + " ");
			inorderTraversal(root.right);
		}
	}

	void inorder() {
		this.inorderTraversal(this.nodes.get(1));
		System.out.println();
	}

	void swap(Node root, int depth, int originalDepth) {
		if (root != null) {
            if (depth == 1) {
                Node temp;
                temp = root.left;
                root.left = root.right;
                root.right = temp;

                swap(root.left, originalDepth, originalDepth);
                swap(root.right, originalDepth, originalDepth);
            } else {
                swap(root.left, depth-1, originalDepth);
                swap(root.right, depth-1, originalDepth);
            }
        }
	}

	void swapAtDepth(int depth) {
		swap(this.nodes.get(1), depth, depth);
	}
}

public class Solution1 {

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine().trim());
		String [] line;
		int left, right, T;

		if (N > 0) {
			Tree tree = new Tree(N);

			for (int index = 1; index <= N; ++index) {
				line = br.readLine().trim().split(" ");
				left = Integer.parseInt(line[0]);
				right = Integer.parseInt(line[1]);

				tree.insert(index, left, right);
			}

			T = Integer.parseInt(br.readLine().trim());
			for (int i = 0; i < T; ++i) {

				int depth = Integer.parseInt(br.readLine().trim());
				tree.swapAtDepth(depth);
				tree.inorder();
			}
		}
	}
}
