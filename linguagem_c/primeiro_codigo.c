#include <stdio.h>

int main() {
    // Declaração e inicialização das variáveis inteiras
    int n1 = 0, n2 = 0, n3 = 0;
    int soma = 0, subtracao = 0, multiplicacao = 0;
    float divisao = 0;
    int comp1 = 0, comp2 = 0, condicao_logica = 0;

    // Entrada de dados
    printf("\n Digite o primeiro numero inteiro: ");
    scanf("%d", &n1);
    
    printf("\n Digite o segundo numero inteiro: ");
    scanf("%d", &n2);
    
    printf("\n Digite o terceiro numero inteiro: ");
    scanf("%d", &n3);

    // 1. Operações Aritméticas
    soma = n1 + n2 + n3;
    subtracao = n1 - n2 - n3;
    multiplicacao = n1 * n2 * n3;
    divisao = (float)n1 / n2 / n3;

    printf("\n--- RESULTADOS ARITMETICOS ---");
    printf("\n Soma = %d", soma);
    printf("\n Subtracao = %d", subtracao);
    printf("\n Multiplicacao = %d", multiplicacao);
    printf("\n Divisao = %.2f", divisao);

    // 2. Operações Relacionais (retornam 1 para Verdadeiro ou 0 para Falso)
    comp1 = (n1 > n2);
    comp2 = (n2 < n3);

    printf("\n\n--- VERIFICACOES RELACIONAIS (1 = Verdadeiro | 0 = Falso) ---");
    printf("\n O primeiro numero (%d) e maior que o segundo (%d)? Resultado: %d", n1, n2, comp1);
    printf("\n O segundo numero (%d) e menor que o terceiro (%d)? Resultado: %d", n2, n3, comp2);

    // 3. Operação Lógica (retorna 1 se ambas forem verdadeiras, ou 0 caso contrário)
    condicao_logica = (n1 > 0) && (n2 % 2 == 0);

    printf("\n\n--- VALIDACAO LOGICA (1 = Ambas Verdadeiras | 0 = Falso) ---");
    printf("\n O primeiro e positivo E o segundo e par? Resultado: %d\n", condicao_logica);
    return 0;
}