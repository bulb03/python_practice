<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
	請輸入要修改的欄位，不想改就留白

	<?php
		session_start();
		$dbname = "test2";
		$ac = "root";
		$pwd="1234";
		$account = $_SESSION['account'];
		try{
			if($account!=NULL){
				$conn = new PDO("mysql:host=localhost;dbname=$dbname",$ac,$pwd);
				$conn->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);

				$sql = $conn->prepare("SELECT * FROM user WHERE account=$account;");
				$sql->execute();
				$data = $sql->fetchAll();

				foreach($data as $i){	
					$name = $i['name'];
					$day = $i['birthday'];
					$password = $i['pwd'];
				}

				echo "<form method='POST' action='http://localhost/membersystem/dealupdatedata2.php'>";
				echo "姓名：<input type='text' name='name' value=$name>";
				echo "生日：<input type='date' name='day' value=$day>";
				echo "密碼：<input type='text' name='password' value=$password>";
				echo "<input type='submit' value='submit'>";
				echo "</form>";
			}
			else{
				echo "You have to login\n";
				header("http://localhost/membersystem/member.html");
			}
		}catch(PDOException $e){
			echo $e->getMessage()."<br>";
		}
	?>
</body>
</html>