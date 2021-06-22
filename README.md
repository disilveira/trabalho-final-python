# trabalho-final-python

## Integrantes

- Diego Henrique de Almeida Silveira
- Francisco Grynberg Bignotto

## Descrição do sistema

Para contas a pagar, o sistema deverá armazenar, no mínimo, as datas de vencimento e pagamento, o valor, a descrição da conta, sua classificação, a forma de pagamento e a situação.
A classificação virá de um outro cadastro, podendo ser, por exemplo 'telecomunicações', 'água', 'energia', 'alimentação', etc.
Da mesma maneira, a forma de pagamento (ex: boleto, crédito, débito, depósito, etc.).
Para a situação, basta uma enumeração com os tipos "pago" e "a pagar".

Para contas a receber, no mínimo os campos data de expectativa, de recebimento, o valor, descrição, a classificação, a forma de recebimento, e a situação.
Para a classificação, também deverá ser usado um cadastro separado (ex: serviço prestado, salário, vendas).
Para a forma de recebimento, pode ser o mesmo de contas a pagar (dinheiro, depósito, ...).
E para a situação, basta uma enumeração com os tipos "recebido" e "a receber".

Deverá ser possível emitir um relatório (HTML) que liste as contas a pagar no período (por data de vencimento). E também um relatório que liste as contas a receber no período (expectativa).

Deverá ainda produzir uma tela que apresente o fluxo de caixa.
Esse fluxo deverá ser exibido mês a mês (pelo menos 6 meses).
Você deverá apresentar o fluxo previsto (a receber e a pagar) e o realizado (recebido e pago).
Para tanto, pode utilizar da mesma tabela, ou apresentar tabelas diferentes.
O fluxo deverá exibir o saldo inicial, as receitas por classificação, e um totalizador de receitas.
Em seguida, nas linhas, as despesas por classificação e um totalizador de despesas.
No final da tabela, apresentar o saldo final, e a lucratividade no período (diferença entre o saldo final e inicial).
O saldo inicial de um mês é o saldo final do último mês.
O usuário poderá informar, para o primeiro mês, o saldo manualmente.