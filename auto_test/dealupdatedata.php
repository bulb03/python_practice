<?php
	session_start();
	$dbname = "test2";
	$account = "root";
	$pwd = "1234";


	try{
		if($_SESSION['account']!=NULL){
			$conn = new PDO("mysql:host=localhost;dbname=$dbname",$account,$pwd);
			$conn->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
			
			$ac = $_SESSION['account'];
			$name = $_POST['name'];
			$password = $_POST['password'];

			$i =  0;

			$arr = array($name,$password);            //紀錄要改的值


			//從資料庫拿原本的資料，以便蓋過沒有要改的部分
			$getoriginaldata = $conn->prepare("SELECT name,pwd FROM user where account=:g;"); 
			$getoriginaldata->bindParam(':g',$ac);
			$getoriginaldata->execute();
			//將取得的資料給放進$sql裡
			$sql = $getoriginaldata->fetchAll();
			
			foreach($sql as $data){ //????? 為啥$sql['name']、$sql['pwd']就不行???非得要在foreach裡???
				$a= $data['name'];
				$b= $data['pwd'];
			}

			//用來判斷哪些欄位為空(不想改)，不想改就用原本的資料蓋過去
			for($i=0;$i<count($arr);$i++){
				if(empty($arr[$i])){
					switch($i){
						case 0:
							$arr[0]=$a;
						break;
						case 1:
							$arr[1] = $b;
						break;
					}
				}
				else{
					continue;
				}
			}
			
			//更新資料庫
			$result = $conn->prepare("UPDATE user SET name=:name, pwd=:password WHERE account=:ac;");    
			//我必須讓birthday欄位可以接收NULL?測試後，如果有些欄位不想改而空著，會連帶改變資料庫裡的資料
			//直接不給改birthday，省事
			$result->bindParam(':name',$arr[0]);
			$result->bindParam(':password',$arr[1]);
			$result->bindParam(':ac',$ac);

			$result->execute();

			echo "Finishing update<br>";
			header('Location:http://localhost/membersystem/manage.php');  //導回會員中心
		}
	}catch(PDOException $e){
		echo $e->getMessage()."<br>";
	}
?>