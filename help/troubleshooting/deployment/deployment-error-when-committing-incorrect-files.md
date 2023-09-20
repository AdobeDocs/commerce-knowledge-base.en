---
title: "Deployment errors when committing incorrect files"
description: "This article provides a solution for for the issue when you are getting deployment errors that are caused by incorrect commits to the repository of files/folders that shouldn't have been added."
feature: Deploy
role: Developer
---
# Deployment errors when committing incorrect files

This article provides a fix for the issue when you are getting deployment errors that are caused by incorrect commits to the repository of files/folders that shouldn't have been added.

## Affected products and versions

Adobe Commerce on cloud infrastructure (all versions)

## Issue

You are getting deployment errors when you commit to the repository of files/folders. For example, the following error is caused due to an attempt to connect to the DB when it's not currently available during the [Build Phase](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/deploy/process.html#build-phase):

```SQL
SQLSTATE[HY000] [2002] php_network_getaddresses: getaddrinfo for database.i  
          nternal failed: Name or service not known                                    
                                                                                       
        
        In Abstract.php line 124:
                                                                                       
          SQLSTATE[HY000] [2002] php_network_getaddresses: getaddrinfo for database.i  
          nternal failed: Name or service not known                                    
                                                                                       
        
        In Abstract.php line 124:
                                                                                       
          PDO::__construct(): php_network_getaddresses: getaddrinfo for database.inte  
          rnal failed: Name or service not known       
```

## Cause

Certain files/folders shouldn't be committed to the repository, as they cause a break in the [deployment workflow](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/deploy/process.html).

## Solution

Remove these files/folders from your repository if they are present:

* `app/etc/env.php`
* `pub/media/catalog`
* `vendor`
