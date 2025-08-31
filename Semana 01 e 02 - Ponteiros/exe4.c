#include <stdio.h>
#include <string.h>

void imprimirReverso(char *str) {
    char *p = str;

    while (*p != '\0') {
        p++;
    }
    p--;
    
    while (p >= str) {
        printf("%c", *p);
        p--;
    }
    printf("\n");
}

int main() {
    char texto[100];

    printf("Digite uma string: ");
    gets(texto);

    printf("String invertida: ");
    imprimirReverso(texto);

    return 0;
}
