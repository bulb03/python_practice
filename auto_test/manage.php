<html>
<head>
	<meta charset="utf8">
	<meta lang="zh-tw">
</head>
<body>
	<?php
		session_start();
		if($_SESSION['account']!=null){
			//echo "<a href='http://localhost/membersystem/updatedatas.php'>修改會員資料</a>";
			echo "<a href='http://localhost/membersystem/updatedata.html'><input type='button' value='修改會員資料'></a>";
			echo "<a href='http://localhost/membersystem/showyourdata.php'><input type='button' value='顯示你的資料'></a>";
			echo "<a href='http://localhost/membersystem/logout.php'><input type='button' value='登出'></a>";
		}
		else{
			echo "You can't visit the page<br>";
			header("Location:http://localhost/membersystem/member.html");
		}
	?>

</body>
</html>