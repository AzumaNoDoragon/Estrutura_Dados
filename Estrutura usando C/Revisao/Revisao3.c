#include <stdio.h>

struct ponto
{
	float x, y;
};
typedef struct ponto Ponto;

void atribui(Ponto *p);

int main(int argc, char** argv)
{
	Ponto p;
	
	atribui(&p);
	
	printf("%f", p.x);
	printf("\n%f", p.y);
	
	return 0;
}

void atribui(Ponto *pp){
	pp->x = 5;
	pp->y = 6;
}