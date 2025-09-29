#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv)
{
	int *p; 
	
	p = (int*)malloc(3 * sizeof(int));
	
	p[0] = 10;
	p[1] = 20;
	p[2] = 30;
	
	p = realloc(p, 4 * sizeof(int));
	
	printf("%d, %d, %d", p[0], p[1], p[2]);
	
	free(p);
	
	return 0;
}