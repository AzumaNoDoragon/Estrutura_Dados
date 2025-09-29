#include <stdio.h>
#include <stdlib.h>

void copiarVetor(int *vetOrigem, int *vetDestino, int tam) {
	int i;
    for (i = 0; i < tam; i++) {
        *(vetDestino + i) = *(vetOrigem + i);
    }
}

int main() {
    int tam, i;

    printf("Digite o tam do vetor: ");
    scanf("%d", &tam);

    int *vet1 = (int*) malloc(tam * sizeof(int));
    int *vet2 = (int*) malloc(tam * sizeof(int));

    if (vet1 == NULL || vet2 == NULL) {
        printf("Erro: memoria nao alocada!\n");
        exit(1);
    }

    printf("\nDigite os valores do vetor:\n");
    for (i = 0; i < tam; i++) {
        printf("Posicao %d: ", i);
        scanf("%d", vet1 + i);
    }

    copiarVetor(vet1, vet2, tam);

    printf("\nVetor copiado: ");
    for (i = 0; i < tam; i++) {
        printf("%d ", *(vet2 + i));
    }
    printf("\n");

    free(vet1);
    free(vet2);

    return 0;
}
