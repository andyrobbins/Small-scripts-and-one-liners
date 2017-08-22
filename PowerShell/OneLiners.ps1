#Get process owners from a remtoe system
$owners = @{}; gwmi win32_process -computername <computername> |% {$owners[$_.handle] = $_.getowner().user}; get-process -computername | select processname,Id,@{l="Owner";e={$owners[$_.id.tostring()]}}
