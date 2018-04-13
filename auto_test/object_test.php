<?php
	/**
	* 
	*/
	class db
	{
		private $table_user="user";
		function connect_db(){
			try{
				$servername = "localhost";
				$dbname = "test2";
				$account = "root";
				$password = "1234";	

				//資料庫連線
				session_start();
				$conn = new PDO("mysql:host=$servername;dbname=$dbname",$account,$password);
				$conn->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
				return $conn;
			}
			catch(PDOException $e){
				echo $e->getMessage()."<br>";
			}			
		}

		function login($conn,$ac,$pwd)
		{
			try{
				//輸入mysql指令，使用prepare
				$new_pwd = md5($pwd); 
				$usepdo = $conn->prepare("SELECT account,pwd FROM ".$this->table_user." WHERE account=:acc AND pwd=:pw;");
				$usepdo->bindParam(':acc',$ac);
				$usepdo->bindParam(':pw',$new_pwd);
				$usepdo->execute();
				
				//取得傳回值

				$sql = $usepdo->fetchAll();

				echo "<script>alert('".$sql[0]["account"]." ".$sql[0]["pwd"]."')</script>";

/*				foreach ($sql as $row) {
					echo "<script>alert('".$row["account"]." ".$row["pwd"]."')</script>";
				}*/

				if($sql){                                 //這組if else無法判斷當打錯的資料，因為我sql語法打錯
					echo "login successfully<br>";
					$_SESSION['account'] = $ac;
					header("Location:http://localhost/membersystem/manage.php");
				}  //end if
				else{
					echo "Wrong accout or password<br>";
					header("Location:http://localhost/membersystem/manage.php");
				
				}  //end else
			}
			catch(PDOException $e){
				echo $e->getMessage()."<br>";
			}
		}

		function logout()
		{
			session_start();              //請記得加上這句，如果你要使用session的相關功能
			if($_SESSION['account']!=null){
				unset($_SESSION['account']);
				echo "log out successfully<br>";
				header("Location:http://localhost/membersystem/member.html");
			}
			else{
				echo "Log in first<br>";
				header("Location:http://localhost/membersystem/member.html");
			}
		}
		function register($conn,$ac,$pwd,$type,$bir, $need)
		{
			try
			{
				$ne = "";

				$fact = $conn->query("SELECT * FROM user WHERE account='$ac';");

				foreach($fact as $row){
					$data = $row['account'];
				}

				foreach ($need as $row) {
					echo "windows.alert($row);";
					$ne += $row;
				}

				if($data==$ac){    //我需要那個跳轉頁面，就是會說The account had been used這句話的頁面，幾秒後就跳到header所指的
					echo "The account had been used<br>";
					header("Location:http://localhost/membersystem/register.html");
					exit;
				}

				else{
					$new_pwd = md5($pwd);
					$sql = $conn->prepare("INSERT INTO user(account,pwd,type,birthday,need) VALUES(:a,:p,:t,:b,:n);");
					$sql->bindParam(':a',$ac);
					$sql->bindParam(':p',$new_pwd);
					$sql->bindParam(':t',$type);
					$sql->bindParam(':b',$bir);
					$sql->bindParam(':n',$ne);
					$sql->execute();
					header("Location:http://localhost/membersystem/member.html");
					exit;		
				}
			}
			catch(PDOException $e)
			{
				echo "<script>console.log('"+"register failed"+"')</script> location.href=member.html";
			}
		}

		function get_data($conn)
		{
			try
			{
				if($_SESSION['account'])
				{
					$sql = $conn->prepare("SELECT * FROM user WHERE account=:a;");
					$sql->bindParam(':a',$_SESSION['account']);
					$sql->execute();

					$data = $sql->fetchAll();
					return $data;
				}
			}
			catch(PDOException $e)
			{
				echo $e->getMessage()."<br>";
			}			
		}

		// function update_pwd($conn,$acc,$pwd)
		// {
		// 	try
		// 	{
		// 		if($acc)
		// 		{
		// 			$new_pwd = md5($pwd);
		// 			$sql = $conn->prepare("UPDATE user SET pwd=:pwd WHERE account=:a;");
		// 			$sql->bindParam(':pwd',$new_pwd);
		// 			$sql->bindParam(':a',$acc);			
		// 			$sql->execute();

		// 			$data = $sql->fetchAll();

		// 			if($data)
		// 			{
		// 				$_SESSION['account'] = $acc;
		// 				header("Location:http://localhost/membersystem/manage.php");
		// 			}
		// 			else
		// 			{
		// 				header("Location:http://localhost/membersystem/member.html");
		// 			}
		// 		}
		// 	}
		// 	catch(PDOException $e)
		// 	{
		// 		echo $e->getMessage()."<br>";
		// 	}					
		// }
	}

?>