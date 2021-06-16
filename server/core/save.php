<?php

use Core\Ip;

require_once("ip.php");
$ipInfo = ip::get_all_info();
$info["client"] = $_POST;
$info["ip_info"] = $ipInfo;
$info = json_encode($info);
$file = "../infoLogs/info.log";
file_put_contents($file, strval($info), FILE_APPEND);
return true;