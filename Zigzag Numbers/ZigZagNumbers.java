
public class ZigZagNumbers {
	public static String ZigZag(int n) {

		long[] factorial = new long[n + 1];
		long[] zig = new long[n + 1];
		for (int i = 0; i < n + 1; i++) {
			zig[i] = 0;
		}

		factorial[0] = 1;
		
		for (int i = 1; i <= n; i++)
			factorial[i] = factorial[i - 1] * i;

		zig[0] = 1;
		zig[1] = 1;
		long sum;
		String result = "";

		for (int i = 2; i < n; i++) {
			sum = 0;
			for (int k = 0; k <= i - 1; k++) {
				sum += (factorial[i - 1] / (factorial[i - 1 - k] * factorial[k])) * zig[k] * zig[i - 1 - k];
			}
			
			zig[i] = (sum / 2);

		}
		for (int i = 0; i < zig.length -1; i++) {
			result += zig[i] + " ";
		}
		return result;
	}
}
