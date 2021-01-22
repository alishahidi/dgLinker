<?php
namespace core;

class ip{

    private static $allInfo;

    public static function get_info_from_ip(){
        $curl = curl_init();
        curl_setopt_array($curl, array(
        CURLOPT_URL => "http://ip-api.com/json/?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query",
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT => 30,
        CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
        CURLOPT_CUSTOMREQUEST => "GET",
        CURLOPT_HTTPHEADER => array(
            "cache-control: no-cache"
        ),
        ));

        $response = curl_exec($curl);
        $err = curl_error($curl);
        $response = json_decode($response, true);

        return $response;

    }


    public static function get_all_info(){
        self::$allInfo = array_merge(self::get_info_from_ip());
        self::$allInfo["ip"] = self::$allInfo["query"];
        unlink(self::$allInfo["query"]);
        return self::$allInfo;

    }
}