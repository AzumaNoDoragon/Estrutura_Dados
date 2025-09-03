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
	
	while(i != j){
		atual = atual->prox;
		i++;
	}
	
	novo->prox = atual->prox;
	atual->prox = novo;
	
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

Lista* removePos(Lista *l, int v){
	Lista *p = l, *ant, *aux;
	
	while(p != NULL && p->info != v){
		ant = p;
		p = p->prox;
	}
	if(p){
		return l;
	}else{
		if(p == l){
			aux = p->prox;
			free(p);
			return aux;
		}else{
			aux->prox = p->prox;
			free(p);
			return l;
		}
	}
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
	
	for(i = 0; i <= 5; i++){
		l1 = atribuiFinal(l1, i);
	}
	
	apresenta(l1);
	busca(l1, 5);
	
	/*printf("\n");
	l1 = inserePos(l1, 30, 2);
	apresenta(l1);
	printf("\n");
	l1 = inserePos(l1, 40, 3);
	apresenta(l1);
	
	printf("\n\n");
	l1 = removePos(l1, 2);
	apresenta(l1);*/
	
	printf("\n\n");
	l1 = eliminar(l1);
	if(l1 == NULL)
		printf("Vazio");
	//apresenta(l1);
	
	return 0;
}