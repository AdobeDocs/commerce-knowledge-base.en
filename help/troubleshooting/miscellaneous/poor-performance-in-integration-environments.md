---
title: Poor performance in integration environments
description: This article provides a solution for the issue where the Pro integration environments and Starter staging environments are performing poorly.
feature: Integration, Staging
role: Developer
exl-id: 46110dbc-2f54-4654-95e2-39e8ae1e6979
---
# Poor performance in integration environments

This article provides a solution for the issue where the Pro integration environments and Starter staging environments are performing poorly.

## Affected products and versions:

* Adobe Commerce on cloud infrastructure (all versions)

## Issue

Your Pro integration environment or Starter staging environment is performing poorly.

## Cause

Depending on the size of your catalog/data or the requirements of your third-party integrations/customizations, the resources available in the integration environments might have exceeded.

## Solution

To address performance issues, ensure that you are following the best practices for best performance in the integration environment. You might also need to request an upgrade of the environments to enhance integration. 

First, determine if your environment is on the [Enhanced Integration configuration](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/announcements/commerce-announcements/integration-environment-enhancement-request-pro-and-starter).

* [Pro Architecture](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/architecture/pro-architecture#integration-environment)
* [Starter Architecture](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/architecture/starter-architecture#staging-environment)

Check the deployment log using one of these methods.

### Method 1:

Run the following command using the Cloud CLI:

`magento-cloud activity:log -e <branch name>`

### Method 2:

Check the most recent deployment log for that environment in the [Cloud Console](https://console.adobecommerce.com).

At the end of the deployment log, if you see something like this—the first line shows the size=XL, and the remaining lines show the size=L—then that means that you are on the Enhanced Integration configuration.

```
Environment configuration
mymagento (type: php:8.2, size: XL, disk: 5120)
mysql (type: mysql:10.6, size: L, disk: 5120)
redis (type: redis:7.2, size: L)
opensearch (type: opensearch:2, size: L, disk: 1024)
rabbitmq (type: rabbitmq:3.12, size: L, disk: 1024)
```

If you are not on the Enhanced Integration configuration, you may [request the enhancement/upgrade](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/announcements/commerce-announcements/integration-environment-enhancement-request-pro-and-starter).
If you're already on the Enhanced Integration configuration or you're still encountering performance issues after the upgrade, make sure to follow the best practices for optimal performance in the integration environment: 

* [Pro Architecture](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/architecture/pro-architecture#integration-environment)
* [Starter Architecture](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/architecture/starter-architecture#staging-environment)

If you have fulfilled the above recommendations, [submit a support request](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide#submit-ticket) for additional assistance.
