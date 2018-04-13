<?php
	include 'object_test.php';
	$ac = $_POST['youraccount'];
	$pwd = $_POST['yourpwd'];
	$type = $_POST['type'];
	$bir = $_POST['birthday'];
	$need = $_POST['need'];
	$a = new db;
	$conn = $a->connect_db();
	if(false)
	{
		echo "alert('oops')";
	}
	else
	{
		echo "alert('gogogo')";	
	}
	$a->register($conn,$ac,$pwd,$type,$bir,$need);
/*	$name = $_POST['yourname'];
	$bir = $_POST['yourbirthday'];
	$ac = $_POST['youraccount'];
	$pwd = $_POST['yourpwd'];
	$servername = "test2";
	$acc = "root";
	$password = "1234";

	try{
		$conn = new PDO("mysql:host=localhost;dbname=$servername",$acc,$password);
		$conn->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);

		$fact = $conn->query("SELECT * FROM user WHERE account='$ac';");

		foreach($fact as $row){
			$data = $row['account'];
		}

		if($data==$ac){    //我需要那個跳轉頁面，就是會說The account had been used這句話的頁面，幾秒後就跳到header所指的
			echo "The account had been used<br>";
			header("Location:http://localhost/membersystem/register.html");
			exit;
		}
		else{
			$sql = $conn->prepare("INSERT INTO user(name,birthday,account,pwd) VALUES(:n,:b,:a,:p);");
			$sql->bindParam(':n',$name);
			$sql->bindParam(':b',$bir);
			$sql->bindParam(':a',$ac);
			$sql->bindParam(':p',$pwd);
			$sql->execute();
			header("Location:http://localhost/membersystem/member.html");
			exit;		
		}

	}catch(PDOException $e){
		echo $e->getMessage()."<br>";
	}*/
?>