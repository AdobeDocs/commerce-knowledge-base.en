---
title: Enable cache to avoid performance degradation
description: This article explains how to solve a slow site issue caused by certain Adobe Commerce cache types being disabled.
exl-id: e4e5a753-efa3-4552-aaf6-28e44efcfa5b
feature: Cache, Observability
role: Developer
---
# Enable cache to avoid performance degradation

This article explains how to solve a slow site issue caused by certain Adobe Commerce cache types being disabled.

## Affected products and versions

* Adobe Commerce on cloud infrastructure 2.2.x, 2.3.x
* Adobe Commerce on-premises 2.2.x, 2.3.x

## Issue

You notice performance degradation. For example, the Checkout page is loading slowly, or the Apdex value decrease in New Relic.

## Cause

One reason for performance degradation might be certain Adobe Commerce cache types being disabled.

## Solution

1. First, check the status of your Adobe Commerce cache, to see if this is the issue. For this, [SSH to your environment](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/secure-connections#ssh) and run the following command:

    ```bash
    php bin/magento cache:status
    ```

    This would display the status of each cache type ("0" for disabled, "1" for enabled). Or you can get this information in the `app/etc/env.php` file.

1. Investigate the disabled cache types. All Adobe Commerce cache types should be enabled, unless you received alternative guidance from Adobe. Third party extensions must not require disabling Adobe Commerce cache.
1. If the investigation confirms that some cache types are disabled by mistake, enable them by running the following command for each cache type: `php bin/magento cache:enable <your_disabled_cache_type>`

If there are concerns and/or questions whether a certain Adobe Commerce cache type can or should be disabled, [contact Adobe Commerce support](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket) asking for recommendations.

## Related reading

Adobe Commerce cache documentation in our developer documentation:

* [Adobe Commerce cache overview](https://developer.adobe.com/commerce/frontend-core/guide/caching/)
* [Manage the cache](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/cli/manage-cache)

Other possible reasons for performance issues and solutions for them:

* [Disable Adobe Commerce Banner output to improve site performance](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26909)
* [MySQL tables are too large](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26945)
* [Slow performance, slow and long running crons](/help/troubleshooting/miscellaneous/slow-performance-slow-and-long-running-crons.md)