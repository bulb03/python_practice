<?php
include 'object_test.php';
/*	session_start();              //請記得加上這句，如果你要使用session的相關功能
	if($_SESSION['account']!=null){
		unset($_SESSION['account']);
		echo "log out successfully<br>";
		header("Location:http://localhost/membersystem/member.html");
	}
	else{
		echo "Log in first<br>";
		header("Location:http://localhost/membersystem/member.html");
	}*/
	$a = new db;
	$a->logout();
?>