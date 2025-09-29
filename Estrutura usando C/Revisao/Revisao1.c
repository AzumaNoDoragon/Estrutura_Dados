#include <stdio.h>

void troca(int *n1, int *n2);

int main(int argc, char** argv){
	int n1 = 10, n2 = 20;
	
	troca(&n1, &n2);
	
	printf("n1 = %d", n1);
	printf("\nn2 = %d", n2);
	
	return 0;
}

void troca(int *n1, int *n2){
	int aux;
	
	aux = *n1;
	*n1 = *n2;
	*n2 = aux;
}