public class MatrixMul {
    public static void main(String[] args) {
        int[][] A = {{1,2,3},{4,5,6}}; // 2x3
        int[][] B = {{7,8},{9,10},{11,12}}; // 3x2
        int[][] C = new int[2][2];
        for (int i = 0; i < 2; i++)
            for (int j = 0; j < 2; j++)
                for (int k = 0; k < 3; k++)
                    C[i][j] += A[i][k] * B[k][j];
        System.out.println("Result matrix:");
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) System.out.print(String.format("%4d", C[i][j]));
            System.out.println();
        }
    }
}
