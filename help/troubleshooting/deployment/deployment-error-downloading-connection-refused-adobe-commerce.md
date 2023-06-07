---
title: 'Deployment error: *error 7 while downloading ... port 443: Connection refused*'
description: 'This article provides a solution for the deployment error: *"error 7 while downloading ... port 443: Connection refused"*.'
---

# Deployment error: *error 7 while downloading ... port 443: Connection refused* 

This article provides a fix for the issue when deployment fails with the following error message:

```bash
W: In CurlDownloader.php line 370:
W:
W:   curl error 7 while downloading https://repo.packagist.org/p2/magento/module
W:   -sitemap.json: Failed to connect to repo.packagist.org port 443: Connection
W:    refused
```

## Affected versions

Adobe Commerce on cloud infrastructure, [all supported versions](https://www.adobe.com/content/dam/cc/en/legal/terms/enterprise/pdfs/Adobe-Commerce-Software-Lifecycle-Policy.pdf)

## Issue

 <u>Steps to reproduce</u>:

 Trigger a deployment.

 <u>Expected behavior</u>:

 Deployment is successful.

 <u>Actual behavior</u>:

 Deployment fails, and the following error: *curl error 7 while downloading ... port 443: Connection refused* appears in the deploy log.

## Cause

 This might be due to the cache connection being lost to the repo. 

## Solution

 Ask a Super User on the project to run this command:

 ```bash
 mgc clear-build-cache -p <project ID>
 ```
 
To check who on the project is a Super User, refer to [View a user's project role](/docs/commerce-cloud-service/user-guide/project/user-access.html?lang=en#view-a-user’s-project-role) in the Commerce on Cloud Infrastructure Guide. 

## Recommended reading

* [Adobe Commerce deployment troubleshooter](/docs/commerce-knowledge-base/kb/troubleshooting/deployment/magento-deployment-troubleshooter.html).
* [Adobe Commerce on cloud repo could not be accessed: 403 Forbidden or 404 Not Found error when deploying](/docs/commerce-knowledge-base/kb/troubleshooting/deployment/magento-commerce-cloud-repo-could-not-be-accessed-403-forbidden-or-404-not-found-error-when-deploying.html).
* [Deployment fails with “Error building project: The build hook failed with status code 1”](/docs/commerce-knowledge-base/kb/troubleshooting/deployment/deployment-fails-with-error-building-project-the-build-hook-failed-with-status-code-1.html).


