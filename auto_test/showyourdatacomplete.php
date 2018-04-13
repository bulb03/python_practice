<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
	<style>
		table,tr,td{
			border:1px black solid;
		}
	</style>
</head>
<body>
	<a href="http://localhost/shoppingcart/controller.html"><input type="button" value="按此返回管理頁面"></a>
</body>
</html>
<?php
	session_start();
	$servername = "localhost";
	$dbname = "test2";
	$ac = "root";
	$pwd = "1234";

	try{
		if($_SESSION['pwd']){
			$conn = new PDO("mysql:host=$servername;dbname=$dbname",$ac,$pwd);
			$conn->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);

			$sql = $conn->prepare("SELECT * FROM user;");
			$sql->execute();

			$data = $sql->fetchAll();
			echo "<table><tr><td>id</td><td>姓名</td><td>生日</td><td>帳號</td><td>密碼</td></tr>";
			foreach($data as $row){
				echo "<tr><td>".$row['id']."</td>"."<td>".$row['name']."</td>"."<td>".$row['birthday']."</td>"."<td>".$row['account']."</td>"."<td>".$row['pwd']."</td></tr>";
			}
			echo "</table>";
		}
	}catch(PDOException $e){
		echo $e->getMessage()."<br>";
	}
?>