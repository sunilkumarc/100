import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Question2 {
	/*
	 * Empty keys and values are allowed, but the equals sign must be present
	 * (e.g. "=value", "key="). If the key or value is empty, empty String
	 * should be returned. If the given String is empty, an empty Map should be
	 * returned. If the given String is null, null should be returned. If the
	 * given String has an invalid format, an IllegalArgumentException should be
	 * thrown.
	 */
	static public Map<String, String> decode(String s) {
		Map<String, String> result = new HashMap<>();
		s = s.trim();

		if (s.equals(""))
			return result;

		if (s == null) {
			return null;
		}

		String[] keyValues = s.split("&");
		for (String keyValue : keyValues) {
			String[] keyVals = keyValue.split("=");
			if (keyVals.length == 0) {
				if (keyValue.contains("="))
					result.put("", "");
				else
					throw new IllegalArgumentException();
			} else if (keyVals.length == 1) {
				result.put(keyVals[0], "");
			} else if (keyVals.length != 2) {
				throw new IllegalArgumentException();
			} else {
				result.put(keyVals[0], keyVals[1]);
			}
		}

		return result;
	}

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String exp = br.readLine().trim();
		Map<String, String> result = decode(exp);

		if (result == null)
			System.out.println("null");
		else {
			for (String key : result.keySet()) {
				System.out.println(key + " : " + result.get(key));
			}
		}

		/*String[] strs = "123=".split("=");
		System.out.println(strs.length);
		System.out.println(strs[0] + ":" + strs[1]);*/
	}
}
