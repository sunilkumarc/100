package sap.hiring.challenge;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class Building {
	int x, y;

	public Building(int x, int y) {
		this.x = x;
		this.y = y;
	}
}

public class Question1 {

	public static Boolean canEscape(Building building, int N, int M) {
		int x = building.x;
		int y = building.y;
		if (x == 1 || x == M || y == 1 || y == N)
			return true;
		return false;
	}

	public static List<Building> getNeighbours(int[][] matrix, Building building, int N, int M, int J, int[][] visited) {
		List<Building> neighbours = new ArrayList<>();

		int x = building.x - 1;
		int y = building.y - 1;

		int left = y - 1;
		if (left >= 0 && visited[x][left] == 0 && (matrix[x][y] - matrix[x][left] <= J))
			neighbours.add(new Building(x + 1, left + 1));

		int top = x - 1;
		if (top >= 0 && visited[top][y] == 0 && (matrix[x][y] - matrix[top][y] <= J))
			neighbours.add(new Building(top + 1, y + 1));

		int right = y + 1;
		if (right < M && visited[x][right] == 0 && (matrix[x][y] - matrix[x][right] <= J))
			neighbours.add(new Building(x + 1, right + 1));

		int bottom = x + 1;
		if (bottom < M && visited[bottom][y] == 0 && (matrix[x][y] - matrix[bottom][y] <= J))
			neighbours.add(new Building(bottom + 1, y + 1));

		return neighbours;
	}

	public static List<Building> findPath(int[][] matrix, int N, int M, Building building, int J) {
		Stack<Building> stack = new Stack<>();
		stack.push(building);
		List<Building> path = new ArrayList<>();
		List<Building> neighbours = new ArrayList<>();
		int [][] visited = new int[N][M];

		for (int j = 0; j < N; ++j) {
			for (int k = 0; k < M; ++k) {
				visited[j][k] = 0;
			}
		}

		visited[building.x][building.y] = 1;

		while (!stack.isEmpty()) {
			building = stack.pop();
			path.add(building);

			if (Question1.canEscape(building, N, M)) {
				return path;
			}

			neighbours = Question1.getNeighbours(matrix, building, N, M, J, visited);
			for (Building neighbour : neighbours) {
				stack.push(neighbour);
			}
		}

		return null;
	}

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine().trim());
		String[] line;

		for (int i = 0; i < T; ++i) {
			line = br.readLine().trim().split(" ");
			int N = Integer.parseInt(line[0]);
			int M = Integer.parseInt(line[1]);

			int[][] matrix = new int[N][M];
			for (int j = 0; j < N; ++j) {
				line = br.readLine().trim().split(" ");
				for (int k = 0; k < line.length; ++k) {
					matrix[j][k] = Integer.parseInt(line[k]);
				}
			}
			int Dx, Dy, J;
			line = br.readLine().trim().split(" ");
			Dx = Integer.parseInt(line[0]);
			Dy = Integer.parseInt(line[1]);
			J = Integer.parseInt(line[2]);
			List<Building> path = new ArrayList<>();
			path = Question1.findPath(matrix, N, M, new Building(Dx, Dy), J);

			if (path == null)
				System.out.println("NO");
			else {
				System.out.println("YES");
				for (Building building : path) {
					System.out.println(building.x + " " + building.y);
				}
			}
		}
	}
}
