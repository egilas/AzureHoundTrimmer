# AzureHoundTrimmer

`Azurehoundtrimmer.py` trims the AzGroupMember bloat in the Azurehound JSON output. 

Script tested on an Azurehound file that was 3.3 GB, which was trimmed down to 350 MB. 
Problem with current (as in 2024-07-02) version of Azurehound is that AzGroupMembers in the JSON field contains all user/group properties, not just IDs. In Azure AD's ("Entra") that are heavy on groups, this can make the JSON file go boom.

This issue addresses it, but it hasn't been included in Azurehound yet:
[https://github.com/BloodHoundAD/AzureHound/issues/69](https://github.com/BloodHoundAD/AzureHound/issues/69)

Usage:
```bash
python3 azurehoundtrimmer.py gigainputfile.json smalloutputfile.json
```
