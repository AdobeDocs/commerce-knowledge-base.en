---
title: The var/export folder permission issue Adobe Commerce on cloud
description: This article provides a solution to an issue where you are not able to export product data due to a file permissions issue on the server in the `var/export/email` folder. Symptoms include Product and Catalog exports not available in the user interface, but are visible when using SSH.
exl-id: 68120d3b-f5df-43a5-91f6-2ec519cc25ac
feature: Cloud, Communications, Data Import/Export, Paas, Roles/Permissions
role: Developer
---
# The var/export folder permission issue Adobe Commerce on cloud

This article provides a solution to an issue where you are not able to export product data due to a file permissions issue on the server in the `var/export/email` folder. Symptoms include Product and Catalog exports not available in the user interface, but are visible when using SSH.

## Affected products and versions

Adobe Commerce on cloud infrastructure, 2.3.0-2.3.7-p2, 2.4.0-2.4.3-p1

## Issue

You cannot export files in the `var/export/email` or `var/export/archive` folder.
This failed deploy due to permissions on `var/export/email` or `var/export/email/archive` because that archive folder gets created under email and if I just do the export/email sometimes there’s still an issue) other than adding something to account for the subfolder `var/export/email/archive`.

<u>Steps to reproduce</u>:

In the Admin, go to **System** > *Data Transfer* > **Export**.
Select the CSV files to save in the `var/export/` folder.

<u>Expected result</u>:

CSV files are visible and can be exported.

<u>Actual result</u>:

CSV files are not visible. You also see a permission denied message: *RecursiveDirectoryIterator::__construct(/app/project id>/var/export/email): failed to open dir: Permission denied*

You receive the same message for all export types: Advanced Pricing, Customer Finances, Customer Main File, and Customer Addresses.

## Cause

This is caused by a folder created inside `/var` which has imperfect permissions: `d-wxrwsr-T`. The T sticky bit means the users can only delete the files they own but the missing executable means they cannot create files in the directory.

This is often noticed when the system creates a folder called `export`, that holds a folder called `email`, that holds a folder called `archive`.

 To check if the directory has these misconfigured permissions, run the following command in the CLI/Terminal:

`ls -ld var/export/`

The output if permissions are misconfigured will be:

`d-wxrwsr-T 3 web web 4096 Aug 15 19:12 var/export/`


## Solution

To address this, update the permissions of the folders to 777 then all the files recursively, by running the following commands:

```bash
chmod 777 var/export/
chmod 777 var/export/email/
chmod 777 var/export/email/archive/
chmod 777 -R var/export/
```

## Related reading

* [Export](https://experienceleague.adobe.com/en/docs/commerce-admin/systems/data-transfer/data-export) in our user guide.
