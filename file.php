<?php
header('Access-Control-Allow-Origin:*');//注意！跨域要加这个头 上面那个没有
header('Content-Type: application/json');
header('Content-Type: text/html;charset=utf-8');

$json_string = file_get_contents('json.json');
echo $json_string;
?>