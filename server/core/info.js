function save(){
    var client = new ClientJS();
    var userAgent = client.getUserAgent();
    var browser = client.getBrowser();
    var browserVersion = client.getBrowserVersion();
    var OS = client.getOS();
    var osVersion = client.getOSVersion();
    var CPU = client.getCPU();
    var currentResolution = client.getCurrentResolution();
    var availableResolution = client.getAvailableResolution();
    var language = client.getLanguage();
    var core = navigator.hardwareConcurrency;

    var url;
    function readTextFile(file)
    {
        var rawFile = new XMLHttpRequest();
        rawFile.open("GET", file, false);
        rawFile.onreadystatechange = function ()
        {
            if(rawFile.readyState === 4)
            {
                if(rawFile.status === 200 || rawFile.status == 0)
                {
                    url = rawFile.responseText;
                }
            }
        }
        rawFile.send(null);
    }

    readTextFile("info/redirectUrl");
    
    
    $.ajax({
        type: 'POST',
        url: 'core/save.php',
        data: {userAgent:userAgent,OS:OS,browser:browser,osVersion:osVersion,availableResolution:availableResolution,browserVersion:browserVersion,CPU:CPU,currentResolution:currentResolution,language:language,numCore:core},
        success : console.log("OK"),
        complete: function(r){
            window.location.href = url
         },
        mimeType: 'text'
        });

}
