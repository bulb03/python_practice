<?php
include 'object_test.php';
$a = new db;
$ac = $_POST['account'];
$pwd = $_POST['pwd'];
$conn = $a->connect_db();
$a->login($conn,$ac,$pwd);
?>