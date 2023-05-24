---
title: 'Deployment error: *error 7 while downloading ... port 443: Connection refused*'
description: 'This article provides a solution for the deployment error: *"error 7 while downloading ... port 443: Connection refused"*.'
---

# Deployment error: *error 7 while downloading ... port 443: Connection refused* on Adobe Commerce

This article provides a fix for the issue when deployment fails with the following error message in the deploy log:

```bash
W: In CurlDownloader.php line 370:
W:
W:   curl error 7 while downloading https://repo.packagist.org/p2/magento/module
W:   -sitemap.json: Failed to connect to repo.packagist.org port 443: Connection
W:    refused
```

## Affected versions

Adobe Commerce on cloud infrastructure, [all supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf)

## Issue

 <u>Steps to reproduce</u>:

 Trigger a deployment by pushing the code to the Staging or Production environment.

 <u>Expected behavior</u>:

 Deployment is successful.

 <u>Actual behavior</u>:

 Deployment fails and you see the following error: *error 7 while downloading ... port 443: Connection refused*.

## Cause

 This may be due to the cache connection being lost to the repo. 

## Solution

 Ask a Super User on the project to run this command:

 ```bash
 mgc clear-build-cache -p <project ID>
 ```
 
To check who on the project is a Super User, refer to [View a user's project role](/docs/commerce-cloud-service/user-guide/project/user-access.html?lang=en#view-a-user’s-project-role) in the Commerce on Cloud Infrastructure Guide. 

## Recommended reading

* [Adobe Commerce deployment troubleshooter](/docs/commerce-knowledge-base/kb/troubleshooting/deployment/magento-deployment-troubleshooter.html).
* [Adobe Commerce on cloud repo could not be accessed: 403 Forbidden or 404 Not Found error when deploying](/docs/commerce-knowledge-base/kb/troubleshooting/deployment/magento-commerce-cloud-repo-could-not-be-accessed-403-forbidden-or-404-not-found-error-when-deploying.html).
* [Deployment fails with “Error building project: The build hook failed with status code 1”](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/troubleshooting/deployment/deployment-fails-with-error-building-project-the-build-hook-failed-with-status-code-1.html).
* [Deployment fails with “Error building project: The build hook failed with status code 1”](/docs/commerce-knowledge-base/kb/troubleshooting/deployment/deployment-fails-with-error-building-project-the-build-hook-failed-with-status-code-1.html)


