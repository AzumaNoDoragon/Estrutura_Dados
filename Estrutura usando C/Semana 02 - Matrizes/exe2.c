#include <stdio.h>
#include <stdlib.h>

int** criarMatrizPonteiros(int linhas, int colunas) {
	int i;
    int **mat = (int**) malloc(linhas * sizeof(int*));
    if (!mat) { printf("Erro de memória!\n"); exit(1); }
    for (i = 0; i < linhas; i++) {
        mat[i] = (int*) malloc(colunas * sizeof(int));
        if (!mat[i]) { printf("Erro de memória!\n"); exit(1); }
    }
    return mat;
}

void liberarMatrizPonteiros(int **mat, int linhas) {
	int i;
    for (i = 0; i < linhas; i++) free(mat[i]);
    free(mat);
}

void preencherMatrizPonteiros(int **mat, int l, int c) {
	int i, j;
    for (i = 0; i < l; i++)
        for (j = 0; j < c; j++) {
            printf("Elemento [%d][%d]: ", i, j);
            scanf("%d", &mat[i][j]);
        }
}

void imprimirMatrizPonteiros(int **mat, int l, int c) {
	int i, j;
    for (i = 0; i < l; i++) {
        for (j = 0; j < c; j++)
            printf("%4d ", mat[i][j]);
        printf("\n");
    }
}

int** multiplicarMatrizPonteiros(int **A, int m, int p, int **B, int n) {
	int i, j, k;
    int **M = criarMatrizPonteiros(m, n);
    for (i = 0; i < m; i++)
        for (j = 0; j < n; j++) {
            M[i][j] = 0;
            for (k = 0; k < p; k++)
                M[i][j] += A[i][k] * B[k][j];
        }
    return M;
}

int* criarMatrizSimples(int linhas, int colunas) {
    int *mat = (int*) malloc(linhas * colunas * sizeof(int));
    if (!mat) { printf("Erro de memória!\n"); exit(1); }
    return mat;
}

void preencherMatrizSimples(int *mat, int l, int c) {
	int i, j;
    for (i = 0; i < l; i++)
        for (j = 0; j < c; j++) {
            printf("Elemento [%d][%d]: ", i, j);
            scanf("%d", &mat[i * c + j]);
        }
}

void imprimirMatrizSimples(int *mat, int l, int c) {
	int i, j;
    for (i = 0; i < l; i++) {
        for (j = 0; j < c; j++)
            printf("%4d ", mat[i * c + j]);
        printf("\n");
    }
}

int* multiplicarMatrizSimples(int *A, int m, int p, int *B, int n) {
	int i, j, k;
    int *M = criarMatrizSimples(m, n);
    for (i = 0; i < m; i++)
        for (j = 0; j < n; j++) {
            M[i * n + j] = 0;
            for (k = 0; k < p; k++)
                M[i * n + j] += A[i * p + k] * B[k * n + j];
        }
    return M;
}

int main() {
    int m, p, n, i, j;

    printf("Digite as dimensões da matriz A (m x p): ");
    scanf("%d %d", &m, &p);

    printf("Digite a dimensão n da matriz B (p x n): ");
    scanf("%d", &n);

    int **A_p = criarMatrizPonteiros(m, p);
    int *A_s = criarMatrizSimples(m, p);

    printf("\nPreenchendo Matriz A:\n");
    preencherMatrizPonteiros(A_p, m, p);
    for (i = 0; i < m; i++)
        for (j = 0; j < p; j++)
            A_s[i * p + j] = A_p[i][j];

    int **B_p = criarMatrizPonteiros(p, n);
    int *B_s = criarMatrizSimples(p, n);

    printf("\nPreenchendo Matriz B:\n");
    preencherMatrizPonteiros(B_p, p, n);
    for (i = 0; i < p; i++)
        for (j = 0; j < n; j++)
            B_s[i * n + j] = B_p[i][j];

    printf("\n=== Multiplicação usando VETOR DE PONTEIROS ===\n");
    int **M_p = multiplicarMatrizPonteiros(A_p, m, p, B_p, n);
    imprimirMatrizPonteiros(M_p, m, n);

    printf("\n=== Multiplicação usando VETOR SIMPLES ===\n");
    int *M_s = multiplicarMatrizSimples(A_s, m, p, B_s, n);
    imprimirMatrizSimples(M_s, m, n);

    liberarMatrizPonteiros(A_p, m);
    liberarMatrizPonteiros(B_p, p);
    liberarMatrizPonteiros(M_p, m);
    free(A_s);
    free(B_s);
    free(M_s);
    return 0;
}
