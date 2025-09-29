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

Lista* atribui(Lista* l, int v){
	Lista* novo;
	novo = (Lista*)malloc(sizeof(Lista));
	novo->info = v;
	novo->prox = l;
	return novo;
}

void apresenta(Lista *l){
	if(l != NULL){
		printf("%d\n", l->info);
		apresenta(l->prox);
	}
}

int main(int argc, char** argv)
{
	Lista *l1;
	l1 = inicializa();
	l1 = atribui(l1, 6);
	l1 = atribui(l1, 4);
	l1 = atribui(l1, 2);
	
	apresenta(l1);
	
	return 0;
}