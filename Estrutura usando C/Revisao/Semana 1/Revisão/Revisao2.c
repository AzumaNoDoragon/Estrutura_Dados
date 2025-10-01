#include <stdio.h>

int main(int argc, char** argv){
	int n = 10, *p, **pp;
	
	p = &n;
	pp = &p;
	
	printf("%d", **pp);
	
	return 0;
}
