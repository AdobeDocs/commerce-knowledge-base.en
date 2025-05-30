---
title: Cached images are not loaded after 2.2.X to 2.3.X upgrade
description: This article provides the solution for the issue with cached images not being displayed after upgrading from Adobe Commerce on cloud infrastructure 2.2.X to 2.3.X.
exl-id: 3e6bd5aa-bd5d-4880-8b78-64f280647abe
feature: Cache, Upgrade
role: Developer
---
# Cached images are not loaded after 2.2.X to 2.3.X upgrade

This article provides the solution for the issue with cached images not being displayed after upgrading from Adobe Commerce on cloud infrastructure 2.2.X to 2.3.X.

## Affected versions and editions:

* Adobe Commerce on cloud infrastructure Pro plan architecture 2.2.X, 2.3.X

## Issue

After Adobe Commerce is upgraded from 2.2.X to 2.3.X, the cached product images are not available, and a 404 page is displayed instead.

The issue is caused by the incorrect Nginx configuration set in `.magento.app.yaml`: `index.php` (or none) is used for the `"/media"` location instead of `passthru: /get.php`.

## Solution

1. Check your `.magento.app.yaml` configuration file, at the `"/media"` location. The correct configuration looks like following:

   ```yaml
   "/media":
       root: "pub/media"
       allow: true
       scripts: false
       expires: 1y
       passthru: "/get.php"
   ```
   
1. If `passthru` is not set to `"/get.php"` and `expires` is not set, take the following steps.
1. Correct the configuration file.
    * Starter Plan: correct the file yourself and push the changes.
    * Pro Plan:
    * Integration: correct the file yourself and push the changes.
    * Staging and Production: correct the file yourself, push the changes, and create an [Adobe Commerce support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket) to have it applied.

1. Enable Fastly image optimization in the Commerce Admin (Fastly must be configured prior), as described in <https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/cdn/fastly-image-optimization>.

If the configuration is correct, but you are still experiencing the issue, continue the investigation or contact [Adobe Commerce Support](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket).
