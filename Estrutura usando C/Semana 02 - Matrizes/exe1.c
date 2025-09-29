#include <stdio.h>
#include <stdlib.h>

int** criarMatrizPonteiros(int linhas, int colunas) {
	int i;
    int **matriz = (int**) malloc(linhas * sizeof(int*));
    if (matriz == NULL) {
        printf("Erro de memória!\n");
        exit(1);
    }
    for (i = 0; i < linhas; i++) {
        matriz[i] = (int*) malloc(colunas * sizeof(int));
        if (matriz[i] == NULL) {
            printf("Erro de memória!\n");
            exit(1);
        }
    }
    return matriz;
}

void liberarMatrizPonteiros(int **matriz, int linhas) {
	int i;
    for (i = 0; i < linhas; i++) {
        free(matriz[i]);
    }
    free(matriz);
}

int* criarMatrizSimples(int linhas, int colunas) {
    int *matriz = (int*) malloc(linhas * colunas * sizeof(int));
    if (matriz == NULL) {
        printf("Erro de memória!\n");
        exit(1);
    }
    return matriz;
}

void preencherMatrizPonteiros(int **mat, int l, int c) {
	int i, j;
    for (i = 0; i < l; i++) {
        for (j = 0; j < c; j++) {
            printf("Elemento [%d][%d]: ", i, j);
            scanf("%d", &mat[i][j]);
        }
    }
}

void preencherMatrizSimples(int *mat, int l, int c) {
	int i, j;
    for (i = 0; i < l; i++) {
        for (j = 0; j < c; j++) {
            printf("Elemento [%d][%d]: ", i, j);
            scanf("%d", &mat[i * c + j]);
        }
    }
}

void imprimirMatrizPonteiros(int **mat, int l, int c) {
	int i, j;
    for (i = 0; i < l; i++) {
        for (j = 0; j < c; j++) {
            printf("%3d ", mat[i][j]);
        }
        printf("\n");
    }
}

void imprimirMatrizSimples(int *mat, int l, int c) {
	int i, j;
    for (i = 0; i < l; i++) {
        for (j = 0; j < c; j++) {
            printf("%3d ", mat[i * c + j]);
        }
        printf("\n");
    }
}

int main() {
	int i, j;
    int linhas, colunas;

    printf("Digite o numero de linhas: ");
    scanf("%d", &linhas);
    printf("Digite o numero de colunas: ");
    scanf("%d", &colunas);

    printf("\n=== MATRIZ COM VETOR DE PONTEIROS ===\n");
    int **matP = criarMatrizPonteiros(linhas, colunas);
    preencherMatrizPonteiros(matP, linhas, colunas);

    printf("\nMatriz original:\n");
    imprimirMatrizPonteiros(matP, linhas, colunas);

    printf("\nMatriz transposta:\n");
    for (j = 0; j < colunas; j++) {
        for (i = 0; i < linhas; i++) {
            printf("%3d ", matP[i][j]);
        }
        printf("\n");
    }

    liberarMatrizPonteiros(matP, linhas);

    printf("\n=== MATRIZ COM VETOR SIMPLES ===\n");
    int *matS = criarMatrizSimples(linhas, colunas);
    preencherMatrizSimples(matS, linhas, colunas);

    printf("\nMatriz original:\n");
    imprimirMatrizSimples(matS, linhas, colunas);

    printf("\nMatriz transposta:\n");
    for (j = 0; j < colunas; j++) {
        for (i = 0; i < linhas; i++) {
            printf("%3d ", matS[i * colunas + j]);
        }
        printf("\n");
    }

    free(matS);

    return 0;
}
