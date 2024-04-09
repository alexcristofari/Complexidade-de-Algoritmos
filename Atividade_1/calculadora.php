<?php

function calcularValor($valor1, $valor2) {
    $resultado = $valor1 + $valor2;
    return resultado;
}

$valor1 = intval(redline("Digite primeiro valor inteiro"));
$valor2 = intval(redline("Digite segundo valor inteiro"));

$resultadoCalculado = calcularValor($valor1, $valor2);
echo "o valor é: $resultadoCalculado";




