#include <stdio.h>

void matrixAddition(int A[][100], int B[][100], int C[][100], int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            C[i][j] = A[i][j] + B[i][j];
        }
    }
}

void matrixSubtraction(int A[][100], int B[][100], int C[][100], int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            C[i][j] = A[i][j] - B[i][j];
        }
    }
}

void matrixMultiplication(int A[][100], int B[][100], int C[][100], int rows1, int cols1, int cols2) {
    for (int i = 0; i < rows1; i++) {
        for (int j = 0; j < cols2; j++) {
            C[i][j] = 0;
            for (int k = 0; k < cols1; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

void displayMatrix(int matrix[][100], int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int rows1, cols1, rows2, cols2;

    printf("Enter the number of rows and columns for the first matrix: ");
    scanf("%d %d", &rows1, &cols1);

    printf("Enter the number of rows and columns for the second matrix: ");
    scanf("%d %d", &rows2, &cols2);

    if (cols1 != rows2) {
        printf("Matrix multiplication is not possible. Columns of the first matrix must be equal to rows of the second matrix.\n");
        return 1;
    }

    int matrix1[100][100], matrix2[100][100], result[100][100];

    printf("Enter elements for the first matrix:\n");
    for (int i = 0; i < rows1; i++) {
        for (int j = 0; j < cols1; j++) {
            scanf("%d", &matrix1[i][j]);
        }
    }

    printf("Enter elements for the second matrix:\n");
    for (int i = 0; i < rows2; i++) {
        for (int j = 0; j < cols2; j++) {
            scanf("%d", &matrix2[i][j]);
        }
    }

    printf("Matrix Addition:\n");
    matrixAddition(matrix1, matrix2, result, rows1, cols1);
    displayMatrix(result, rows1, cols1);

    printf("Matrix Subtraction:\n");
    matrixSubtraction(matrix1, matrix2, result, rows1, cols1);
    displayMatrix(result, rows1, cols1);

    printf("Matrix Multiplication:\n");
    matrixMultiplication(matrix1, matrix2, result, rows1, cols1, cols2);
    displayMatrix(result, rows1, cols2);

    return 0;
}

