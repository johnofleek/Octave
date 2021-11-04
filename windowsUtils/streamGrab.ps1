# powershell script
# to download Latest Blueprint and associated 

# GET the Blueprint data for all Blueprints from Octave

# ./streamGrab.ps1 -user "Octaveuser" -authtoken "master" -company "linkwave_technologies -stream_id "s6156c4530a9fd107c3bfa332"


param (
    $user ,
    $authtoken,
    $company, 
    $streamid = "s6156c4530a9fd107c3bfa332"
)

If($user -eq $null -or $authtoken -eq $null -or $company -eq $null -or $streamid -eq $null)
{
    Write-Host "help"
    Write-Host "Enter commands like the following - look on octave.sierrawireless.io for your actual values"
    Write-Host './streamGrab.ps1 -user "yourOctaveUserName" -authtoken "YourOctaveMasterToken" -company "yourOctaveCompany" -streamid "streamid"'
    return;
}


#$user
#$authtoken
#$company

# GET https://octave-api.sierrawireless.io/v5.0/<company_name>/stream/<stream_id>

$uribase = "https://octave-api.sierrawireless.io/v5.0/" + $company + "/"


# echo "get the data"




$param = @{
    Uri         = $uribase + "event/" + $streamid + "?limit=10000"
    Method      = "GET"
    Headers     = @{ 'X-Auth-Token' = $authtoken
                     'X-Auth-User' = $user
                     }
}

# echo $param.Uri

$response = Invoke-RestMethod @param

# echo $response

#echo $response | ConvertTo-Json -Depth 100

Foreach ($body in $response.body)
{
    #echo $body.generatedDate
    
    $csvop = (([System.DateTimeOffset]::FromUnixTimeMilliseconds($body.generatedDate)).DateTime).ToString("s") + ","
    #echo $csvop
    
    $csvop = $csvop + $body.generatedDate + ','
    #echo $body.elems.virtual.measurements    | ConvertTo-Json -Depth 100
    
    $csvop = $csvop + $body.elems.virtual.measurements.strain + ',' + $body.elems.virtual.measurements.pressure

    #echo $body.creationDate 
    echo $csvop
}









