#include <stdio.h>

int main()
{
    float inss, salario, ir, salario_liquido;
    printf("calculo do salario liquido com desconto do inss e ir \n\n");
    printf("Digite o seu salario bruto\n");
    scanf("%f", &salario);
    
    if (salario <= 1320){
        inss = salario * 0.075;
    }else if (salario > 1320 && salario <= 2571.29){
        inss = salario * 0.09;
    }else if (salario > 2571.29 && salario <= 3856.94){
        inss = salario * 0.12;
    }else if(salario > 3856.94 && salario <= 7507.49){
        inss = salario * 0.14;
    }
    //calcular o ir
    if (salario <= 1903.98 ){
        ir = salario * 0;
    }else if (salario > 1903.98 && salario <= 2826.65){
        ir = salario * 0.075;
    }else if ( salario > 2826.65 && salario <= 3751.05){
        ir = salario * 0.15;
    }else if (salario > 3751.05 && salario <= 4664.68){
        ir = salario * 0.225;
    }else if (salario > 4664.68){
        ir = salario * 0.275;
    }

    //calcular valor liquido ja que temos os valores do inss e do ir
    
    salario_liquido = (salario - inss)- ir;
    
    //mostrar na tela os resultados
    
    printf("Desconto do inss:%.2f\n\n",inss); //.2f duas casas decimais
    printf("Desconto do ir:%.2f\n\n",ir);
    printf("Salario liquido incluido os descontos:%.2f\n\n", salario_liquido);
    

    return 0;
}