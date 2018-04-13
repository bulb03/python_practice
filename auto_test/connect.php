<?php
	$servername = "localhost";
	$dbname = "test2";
	$account = "root";
	$password = "1234";

	try{
		$conn = new PDO("mysql:host=$servername;dbname=$dbname",$account,$password);
		$conn->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);

		
	}
	catch(PDOException $e){
		echo $e->getMessage()."<br>";
	}
?>