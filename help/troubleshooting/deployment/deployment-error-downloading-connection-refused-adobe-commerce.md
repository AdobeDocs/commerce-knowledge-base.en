---
title: "Deployment error: *error 7 while downloading ... port 443: Connection refused* on Adobe Commerce"
description: This article provides a solution for deployment error *error 7 while downloading ... port 443: Connection refused*.
---

# Deployment error: "error 7 while downloading ... port 443: Connection refused" on Adobe Commerce

This article provides a fix for the issue when deployment fails with the following error message in the deployment log:

```console
W: In CurlDownloader.php line 370:
W:
W:   curl error 7 while downloading https://repo.packagist.org/p2/magento/module
W:   -sitemap.json: Failed to connect to repo.packagist.org port 443: Connection
W:    refused
```

## Affected versions

* Adobe Commerce on cloud infrastructure, [all supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf)

## Issue

 <u>Steps to reproduce</u>:

 Trigger a deploy by pushing the code to the Staging or Production environment.

 <u>Expected behavior</u>:

 Deployment is successful.

 <u>Actual behavior</u>:

 In the deployment logs you see the following error: ``error 7 while downloading ... port 443: Connection refused" on Adobe Commerce.

## Cause

 This may be due to the lost cache connection to the repo.

## Solution

 Please ask a Super Admin on the project to run this command:

 ```bash
 mgc clear-build-cache -p <project ID>
 ```

## Recommended reading

* [Best practices for builds and deployment](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/deploy/best-practices.html) in our Commerce on Cloud Infrastructure Guide.

