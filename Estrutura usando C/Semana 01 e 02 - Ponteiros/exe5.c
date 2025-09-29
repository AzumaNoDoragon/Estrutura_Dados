#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char nome[50];
    char cargo[50];
    float salario;
} Funcionario;

Funcionario* criarVetor(int tamanho) {
    Funcionario *vetor = (Funcionario*) malloc(tamanho * sizeof(Funcionario));
    if (vetor == NULL) {
        printf("Erro: memória não alocada!\n");
        exit(1);
    }
    return vetor;
}

void cadastrarFuncionario(Funcionario *vetor, int indice) {
    printf("\n--- Cadastro de Funcionário %d ---\n", indice + 1);

    printf("Nome: ");
    scanf(" %[^\n]", vetor[indice].nome);

    printf("Cargo: ");
    scanf(" %[^\n]", vetor[indice].cargo);

    printf("Salário: ");
    scanf("%f", &vetor[indice].salario);
}

void imprimirFuncionarios(Funcionario *vetor, int qtd) {
	int i;
    if (qtd == 0) {
        printf("\nNenhum funcionário cadastrado!\n");
        return;
    }

    printf("\n--- Lista de Funcionários ---\n");
    for (i = 0; i < qtd; i++) {
        printf("\nFuncionário %d\n", i + 1);
        printf("Nome: %s\n", vetor[i].nome);
        printf("Cargo: %s\n", vetor[i].cargo);
        printf("Salário: R$ %.2f\n", vetor[i].salario);
    }
}

int main() {
    int opcao;
    int capacidade = 2;
    int qtd = 0;
    Funcionario *funcionarios = criarVetor(capacidade);

    do {
        printf("\n===== MENU =====\n");
        printf("1 - Cadastrar Funcionário\n");
        printf("2 - Listar Funcionários\n");
        printf("0 - Sair\n");
        printf("Escolha: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                if (qtd == capacidade) {
                    capacidade *= 2;
                    funcionarios = (Funcionario*)realloc(funcionarios, capacidade * sizeof(Funcionario));
                    if (funcionarios == NULL) {
                        printf("Erro: memória não realocada!\n");
                        exit(1);
                    }
                }
                cadastrarFuncionario(funcionarios, qtd);
                qtd++;
                break;

            case 2:
                imprimirFuncionarios(funcionarios, qtd);
                break;

            case 0:
                printf("Encerrando o programa...\n");
                break;

            default:
                printf("Opção inválida!\n");
        }
    } while (opcao != 0);

    free(funcionarios);
    return 0;
}
