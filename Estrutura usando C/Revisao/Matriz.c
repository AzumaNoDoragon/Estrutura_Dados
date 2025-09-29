#include <stdio.h>
#include <stdlib.h>

int** transposta(int** mat, int col, int lin){
	int** mt, i, j;
	mt = (int**)malloc(sizeof(int*) * lin);
	for(i = 0; i < lin; i++){
		mt[i] = (int*)malloc(sizeof(int) * col);
	}
	
	for(i = 0; i < lin; i++){
		for(j = 0; j < col; j++){
			mt[i][j] = mat[j][i];
		}
	}
	return mt;
}

int main(int argc, char** argv)
{
	int **mat, **trans, l = 3, c = 3, i, j;
	mat = (int**)malloc(l * sizeof(int));
	for(i = 0; i < l; i++){
		mat[i] = (int*)malloc(c * sizeof(int));
		
	}
	int x = 1;
	for(i = 0; i < l; i++){
		for(j = 0; j < c; j++){
			mat[i][j] = x; x++;
		}
	}
	
	for(i = 0; i < l; i++){
		for(j = 0; j < c; j++){
			printf("%d\t", mat[i][j]);
		}
		printf("\n");
	}
	
	trans = transposta(mat, l, c);
	
	printf("\n Transposta: \n");
	
	for(i = 0; i < l; i++){
		for(j = 0; j < c; j++){
			printf("%d\t", trans[i][j]);
		}
		printf("\n");
	}
	
	for(i = 0; i < l; i++) free(mat[i]);
	free(mat);
	for(i = 0; i < c; i++) free(trans[i]);
	free(trans);
	
	return 0;
}