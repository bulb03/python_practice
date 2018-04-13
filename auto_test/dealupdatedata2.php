<?php
	session_start();
	$servername = "localhost";
	$dbname = "test2";
	$account = "root";
	$pwd = "1234";
	$ac = $_SESSION['account'];
	$name = $_POST['name'];
	$day = $_POST['birthday'];
	$password = $_POST['password'];

	try{
		if($ac!=NULL){
			$conn = new PDO("mysql:host=$servername;dbname=$dbname",$account,$pwd);
			$conn->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);

			$sql = $conn->prepare("UPDATE test2 SET :name,:birthday,:password WHERE account=$ac;");
			$sql->bindParam(':name',$name);
			$sql->bindParam(':birthday',$day);
			$sql->bindParam(':password',$password);
			$sql->execute();

			echo "finish updating<br>";
		}
		else{
			echo "You have to login<br>";
			header("http://localhost/membersystem/updatedatas.php");
		}
	}catch(PDOException $e){
		echo $e->getMessage()."<br>";
	}
?>