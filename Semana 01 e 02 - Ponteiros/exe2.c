#include <stdio.h>
#include <stdlib.h>

int* criarVetor(int tamanho) {
    int *vetor = (int*) malloc(tamanho * sizeof(int));
    if (vetor == NULL) {
        printf("Erro: memoria nao alocada!\n");
        exit(1);
    }
    return vetor;
}

void preencherVetor(int *vetor, int tamanho) {
	int i;
	
    for (i = 0; i < tamanho; i++) {
        printf("Digite o valor para a posição %d: ", i);
        scanf("%d", &vetor[i]);
    }
}

void imprimirVetor(int *vetor, int tamanho) {
	int i;
	
    printf("\nValores do vetor: ");
    for(i = 0; i < tamanho; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n");
}

int main() {
    int tam;
    int *vet;

    printf("Digite o tamanho do vetor: ");
    scanf("%d", &tam);

    vet = criarVetor(tam);
    preencherVetor(vet, tam);
    imprimirVetor(vet, tam);

    free(vet);
    return 0;
}
