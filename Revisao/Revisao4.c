#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define QTD 3

struct ponto
{
	float x, y;
};
typedef struct ponto Ponto;

void atribui(Ponto *p);
Ponto* criaAlloc();
float calcDistancia(Ponto *p1, Ponto *p2);

int main(int argc, char** argv)
{
	Ponto **vet;
	int i;
	
	vet = (Ponto**)malloc(QTD * sizeof(Ponto*));
	
	for(i = 0; i < QTD; i++){
		vet[i] = criaAlloc();
		atribui(vet[i]);
	}
	
	for(i = 0; i < QTD - 1; i++){
		printf("\nDistancia do vet %d: %f", i, calcDistancia(vet[i], vet[i + 1]));
	}
	
	for(i = 0; i < QTD; i++){
		free(vet[i]);
	}
	free(vet);
	
	return 0;
}

float calcDistancia(Ponto *p1, Ponto *p2){
	return sqrt(pow((p2->x - p1->x), 2) + pow((p2->y - p1->y), 2));
}

void atribui(Ponto *pp){
	printf("Digite o valor de X: ");
	scanf("%f", &pp->x);
	printf("Digite o valor de Y: ");
	scanf("%f", &pp->y);
}

Ponto* criaAlloc(){
	return (Ponto*)malloc(sizeof(Ponto));
}