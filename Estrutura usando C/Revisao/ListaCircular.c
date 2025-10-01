// Gabriel Santos Afini da Silva
#include <stdio.h>
#include <stdlib.h>

struct lista {
    int info;
    struct lista *prox;
};
typedef struct lista Lista;

Lista* novoNo(int valor);
Lista* inserirOrdenado(Lista* cabeca, int valor);
void dividirLista(Lista* cabeca, Lista** l1, Lista** l2);
Lista* concatenar(Lista* l1, Lista* l2);
int contarNos(Lista* cabeca);
void imprimirLista(Lista* cabeca);
Lista* removerValor(Lista* cabeca, int valor);

int main() {
    Lista *lista1 = NULL, *lista2 = NULL, *l1 = NULL, *l2 = NULL;

    lista1 = inserirOrdenado(lista1, 10);
    lista1 = inserirOrdenado(lista1, 5);
    lista1 = inserirOrdenado(lista1, 30);
    lista1 = inserirOrdenado(lista1, 20);
    printf("Lista1 apos insercao ordenada: ");
    imprimirLista(lista1);

    dividirLista(lista1, &l1, &l2);
    printf("\nDivisao da lista1:\n");
    printf("L1: ");
    imprimirLista(l1);
    printf("L2: ");
    imprimirLista(l2);

    lista2 = inserirOrdenado(lista2, 15);
    lista2 = inserirOrdenado(lista2, 25);
    printf("\nLista2 apos insercao: ");
    imprimirLista(lista2);

    Lista* concatenada = concatenar(l1, lista2);
    printf("\nConcatenacao (L1 + Lista2): ");
    imprimirLista(concatenada);

    concatenada = removerValor(concatenada, 20);
    printf("\nLista apos remover valor 20: ");
    imprimirLista(concatenada);

    printf("\nTotal de nos na lista final: %d\n", contarNos(concatenada));

    return 0;
}
Lista* novoNo(int valor) {
    Lista* no = (Lista*) malloc(sizeof(Lista));
    if (!no) exit(1);
    no->info = valor;
    no->prox = no;
    return no;
}

void imprimirLista(Lista* cabeca) {
    if (!cabeca) {
        printf("(lista vazia)\n");
        return;
    }
    Lista* aux = cabeca;
    do {
        printf("%d -> ", aux->info);
        aux = aux->prox;
    } while (aux != cabeca);
    printf("(volta para %d)\n", cabeca->info);
}

void dividirLista(Lista* cabeca, Lista** l1, Lista** l2) {
    if (!cabeca || cabeca->prox == cabeca) {
        *l1 = cabeca;
        *l2 = NULL;
        return;
    }

    Lista *slow = cabeca, *fast = cabeca;
    while (fast->prox != cabeca && fast->prox->prox != cabeca) {
        fast = fast->prox->prox;
        slow = slow->prox;
    }

    *l1 = cabeca;
    *l2 = slow->prox;

    slow->prox = *l1;
    if (fast->prox == cabeca)
        fast->prox = *l2;
    else
        fast->prox->prox = *l2;
}

Lista* concatenar(Lista* l1, Lista* l2) {
    if (!l1) return l2;
    if (!l2) return l1;

    Lista* fim1 = l1;
    while (fim1->prox != l1) fim1 = fim1->prox;

    Lista* fim2 = l2;
    while (fim2->prox != l2) fim2 = fim2->prox;

    fim1->prox = l2;
    fim2->prox = l1;

    return l1;
}

Lista* removerValor(Lista* cabeca, int valor) {
    if (!cabeca) return NULL;

    Lista *atual = cabeca, *anterior = NULL;

    while (atual->info == valor) {
        Lista* fim = cabeca;
        while (fim->prox != cabeca) fim = fim->prox;

        if (atual->prox == cabeca) {
            free(atual);
            return NULL;
        }

        fim->prox = atual->prox;
        cabeca = atual->prox;
        free(atual);
        atual = cabeca;
    }

    do {
        anterior = atual;
        atual = atual->prox;
        if (atual->info == valor) {
            anterior->prox = atual->prox;
            free(atual);
            atual = anterior;
        }
    } while (atual->prox != cabeca);

    return cabeca;
}

int contarNos(Lista* cabeca) {
    if (!cabeca) return 0;

    int count = 0;
    Lista* aux = cabeca;
    do {
        count++;
        aux = aux->prox;
    } while (aux != cabeca);

    return count;
}

Lista* inserirOrdenado(Lista* cabeca, int valor) {
    Lista* no = novoNo(valor);

    if (!cabeca) return no;

    if (valor < cabeca->info) {
        Lista* fim = cabeca;
        while (fim->prox != cabeca) fim = fim->prox;
        fim->prox = no;
        no->prox = cabeca;
        return no;
    }

    Lista* atual = cabeca, *anterior = NULL;
    do {
        anterior = atual;
        atual = atual->prox;
        if (valor < atual->info) break;
    } while (atual != cabeca);

    anterior->prox = no;
    no->prox = atual;
    return cabeca;
}