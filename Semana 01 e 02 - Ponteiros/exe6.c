#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int codigo;
    char nome[50];
    float preco;
} Produto;

Produto* criarVetor(int tamanho) {
    Produto *vetor = (Produto*) malloc(tamanho * sizeof(Produto));
    if (vetor == NULL) {
        printf("Erro: memória não alocada!\n");
        exit(1);
    }
    return vetor;
}

void cadastrarProduto(Produto *vetor, int indice) {
    printf("\n--- Cadastro de Produto %d ---\n", indice + 1);

    printf("Código: ");
    scanf("%d", &vetor[indice].codigo);

    printf("Nome: ");
    scanf(" %[^\n]", vetor[indice].nome);

    printf("Preço: ");
    scanf("%f", &vetor[indice].preco);
}

void imprimirProdutos(Produto *vetor, int qtd) {
	int i;
    if (qtd == 0) {
        printf("\nNenhum produto cadastrado!\n");
        return;
    }

    printf("\n--- Lista de Produtos ---\n");
    for (i = 0; i < qtd; i++) {
        printf("\nProduto %d\n", i + 1);
        printf("Código: %d\n", vetor[i].codigo);
        printf("Nome: %s\n", vetor[i].nome);
        printf("Preço: R$ %.2f\n", vetor[i].preco);
    }
}

int buscarProduto(Produto *vetor, int qtd, int codigo) {
	int i;
    for (i = 0; i < qtd; i++) {
        if (vetor[i].codigo == codigo) {
            return i;
        }
    }
    return -1;
}

void alterarProduto(Produto *vetor, int qtd, int codigo) {
    int pos = buscarProduto(vetor, qtd, codigo);

    if (pos == -1) {
        printf("\nProduto não encontrado!\n");
        return;
    }

    printf("\n--- Alterar Produto (Código %d) ---\n", codigo);

    printf("Novo nome: ");
    scanf(" %[^\n]", vetor[pos].nome);

    printf("Novo preço: ");
    scanf("%f", &vetor[pos].preco);

    printf("Produto alterado com sucesso!\n");
}

int main() {
    int opcao, capacidade, qtd = 0;
    Produto *produtos;

    printf("Digite o tamanho inicial do vetor de produtos: ");
    scanf("%d", &capacidade);

    produtos = criarVetor(capacidade);

    do {
        printf("\n===== MENU =====\n");
        printf("1 - Cadastrar Produto\n");
        printf("2 - Listar Produtos\n");
        printf("3 - Buscar Produto por Código\n");
        printf("4 - Alterar Produto por Código\n");
        printf("0 - Sair\n");
        printf("Escolha: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                if (qtd == capacidade) {
                    capacidade *= 2;
                    produtos = (Produto*) realloc(produtos, capacidade * sizeof(Produto));
                    if (produtos == NULL) {
                        printf("Erro: memória não realocada!\n");
                        exit(1);
                    }
                }
                cadastrarProduto(produtos, qtd);
                qtd++;
                break;

            case 2:
                imprimirProdutos(produtos, qtd);
                break;

            case 3: {
                int codigo;
                printf("Digite o código do produto: ");
                scanf("%d", &codigo);
                int pos = buscarProduto(produtos, qtd, codigo);
                if (pos == -1) {
                    printf("Produto não encontrado!\n");
                } else {
                    printf("\nProduto encontrado:\n");
                    printf("Código: %d\n", produtos[pos].codigo);
                    printf("Nome: %s\n", produtos[pos].nome);
                    printf("Preço: R$ %.2f\n", produtos[pos].preco);
                }
                break;
            }

            case 4: {
                int codigo;
                printf("Digite o código do produto que deseja alterar: ");
                scanf("%d", &codigo);
                alterarProduto(produtos, qtd, codigo);
                break;
            }

            case 0:
                printf("Encerrando o programa...\n");
                break;

            default:
                printf("Opção inválida!\n");
        }
    } while (opcao != 0);

    free(produtos);
    return 0;
}
