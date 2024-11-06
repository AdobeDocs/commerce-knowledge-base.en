---
title: Cache warming up and site unavailable on Adobe Commerce
description: This article provides a solution for when the page cache is warming up and there is a stuck deployment or site down.
exl-id: c91d5c1f-95e6-4240-be98-2acea49ae728
feature: Cache, Variables
role: Developer
---
# Cache warming up and site unavailable on Adobe Commerce

This article provides a solution for when the page cache is warming up and there is a stuck deployment or site down.

## Affected products and versions

* Adobe Commerce on cloud infrastructure, all [supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf).

## Issue

The cache warm up script, at the end of the post-deploy phase, sends requests at such a high rate that certain instances, like 4-cpu ones, cannot cope. Their nginx exhausts the number of workers.

 <u>Steps to reproduce</u>:

Start cache warm up operations.

 <u>Expected result</u>:

Pages or whole site loads.

 <u>Actual result</u>:

The site is unavailable or the response time is too high.

## Solution

Limit the number of concurrent connections during the cache warm-up. This requires adding the `WARM_UP_CONCURRENCY` post-deploy variable to specify the number of warm-up requests that the cache warm-up script can send concurrently. Setting this option can help manage the load on Adobe Commerce's cloud infrastructure. For steps, see [Post-deploy variables > WARM\_UP\_CONCURRENCY](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/configure/env/stage/variables-post-deploy#warm_up_concurrency) in our developer documentation.

## Related reading

 [Full-Page Cache](https://experienceleague.adobe.com/en/docs/commerce-admin/systems/tools/cache-management#full-page-caching) in our user guide
