#include <stdio.h>
#include <stdlib.h>

struct ponto{
	float x, y;
};
typedef struct ponto Ponto;

struct lista{
	int info;
	struct lista *prox;
};
typedef struct lista Lista;

Lista* inicializa(){
	return NULL;
}

void apresenta(Lista *l){
	if(l != NULL){
		printf("[%d]->&%p& ", l->info, &l->info);
		apresenta(l->prox);
	}
}

Lista* atribuiInicio(Lista* l, int v){
	Lista* novo;
	novo = (Lista*)malloc(sizeof(Lista));
	novo->info = v;
	novo->prox = l;
	return novo;
}

Lista* inserePos(Lista *l, int v, int j){
	int i = 1;
	Lista *novo, *atual = l;
	
	novo = (Lista*)malloc(sizeof(Lista));
	novo->info = v;
	
	if (l == NULL) {
        novo->prox = NULL;
        return novo;
    }
    
    if (j <= 1) {
        novo->prox = l;
        return novo;
    }
    
    while (i < j - 1 && atual->prox != NULL) {
        atual = atual->prox;
        i++;
    }
    
    novo->prox = atual->prox;
    atual->prox = novo;

	return l;
}

Lista* insereNaTerceiraPos(Lista *l, int v){
	return inserePos(l, v, 3);
}

Lista* insereNaQuartaPos(Lista *l, int v){
	return inserePos(l, v, 4);
}

Lista* insereOrdenado(Lista *l, int v) {
    Lista *novo, *ant = NULL, *atual = l;

    novo = (Lista*)malloc(sizeof(Lista));
    novo->info = v;

    if(l == NULL || v < l->info){
        novo->prox = l;
        return novo;
    }

    while(atual != NULL && atual->info < v){
        ant = atual;
        atual = atual->prox;
    }

    novo->prox = atual;
    ant->prox = novo;

    return l;
}

Lista* atribuiFinal(Lista *l, int v){
	Lista *novo, *p=l;
	novo = (Lista*)malloc(sizeof(Lista));
	novo->info = v;
	novo->prox = NULL;
	if(l == NULL){
		return novo;
	} else {
		while(p->prox!=NULL){
			p = p->prox;
		}
		p->prox = novo;
		return l;
	}
}

void busca(Lista *l, int v){
	while(l != NULL && l->info != v){
		l = l->prox;
	}
	l ? printf("\nBusca de index: %d\n", l->info) : printf("\nNão encontrado!");
}

Lista* removePos(Lista *l, int v) {
    Lista *p = l, *ant = NULL;

    while (p != NULL && p->info != v) {
        ant = p;
        p = p->prox;
    }

    if (p == NULL) {
        return l;
    }

    if (ant == NULL) {
        l = p->prox;
        free(p);
        return l;
    }

    ant->prox = p->prox;
    free(p);
    return l;
}

Lista* eliminar(Lista* l){
	if(l != NULL){
		eliminar(l->prox);
		free(l);
	}
	return NULL;
}

int main(int argc, char** argv)
{
	Lista *l1;
	int i;
	l1 = inicializa();
	apresenta(l1);
	
	for(i = 3; i <= 5; i++){
		l1 = atribuiFinal(l1, i);
	}
	printf("Lista criada\n");
	apresenta(l1);
	busca(l1, 5);
	
	printf("\n");
	printf("Inserir na 3ª Pos\n");
	l1 = insereNaTerceiraPos(l1, 6);
	apresenta(l1);
	printf("\n");
	printf("Inserir na 4ª Pos\n");
	l1 = insereNaQuartaPos(l1, 7);
	apresenta(l1);
	
	printf("\n\n");
	printf("Remover a 4ª\n");
	l1 = removePos(l1, 4);
	apresenta(l1);
	
	printf("\n\n");
	printf("Inserir o 4\n");
	l1 = insereOrdenado(l1, 4);
	apresenta(l1);
	
	printf("\n\n");
	l1 = eliminar(l1);
	printf("Eliminar\n");
	if(l1 == NULL){
		printf("Vazio");
	}
	
	return 0;
}