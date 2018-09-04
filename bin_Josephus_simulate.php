<?php

$n = 20;
$m = 13;
$k = 9;

$list = [];

for ($i = 1; $i <= $n; $i++) {

    array_push($list, $i);
}

echo " List : $n  From : $m  Step : $k  \r\n";

echo y($list, $m, $k);

function y(&$n, $m, $k)
{

    if (count($n) < 1 && $m < 1) {

        echo " error params N or M ";exit;
    }
    p($n);

    if (count($n) == 1) {

        return 'the king is ' . $n[0];

    } else {

        if ($m != 1) {

            $n = change($n, $m);
        }

        $key = $k % count($n);
        $key = !$key ? count($n) - 1 : $key - 1;
        unset($n[$key]);
        $n = change($n, $key + 1);
        return y($n, 1, $k);

    }

}

function change($n, $m)
{

    $b = array_slice($n, 0, $m - 1, true);
    $e = array_splice($n, $m - 1);
    $n = array_merge($e, $b);
    $n = array_values($n);
    return $n;

}

function p($a)
{

    foreach ($a as $v) {

        echo $v . " ";

    }
    echo "\r\n";
}
