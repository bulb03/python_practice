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
	<a href="http://localhost/membersystem/manage.php"><input type="button" value="按此返回管理頁面"></a>
</body>
</html>
<table>
<?php
	$a = ["schoolName", "purpose", "memberType", "date", "num"];
	for ($i=0; $i<count($a)-1 ; $i++) { 
		echo $a[$i];
	}
	echo "<script>console.log('Hello')</script>";
	include 'object_test.php';
	$a = new db;
	$conn = $a->connect_db();
	$data = $a->get_data($conn);
	foreach($data as $row){
	// 	echo "<tr><td>帳號</td><td>".$row['account']."</td></tr>";
	// 	echo "<tr><td>類型</td><td>".$row['type']."</td></tr>";
	 	echo "<tr><td><a href=\"member.html\">生日</a></td><td></a>".$row['birthday']."</td></tr>";
	 	$timestamp = strtotime($row['birthday']);
	 	echo "<tr><td>日</td><td>".date("Y/m/d",$timestamp)."</td></tr>";
	 	echo "<tr><td>需求</td><td>".$row['need']."</td></tr>";
	// 	//php轉換mysql的datetime方法
	// 	//https://www.phpini.com/php/php-convert-mysql-date-format
	// 	//M：會出現英文的月份簡寫
	// 	//m：會出現數字的月份
	// 	//http://blog.webgolds.com/view/341
	}
?>
</table>