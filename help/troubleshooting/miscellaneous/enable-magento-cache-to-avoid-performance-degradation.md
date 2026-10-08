---
title: Enable cache to avoid performance degradation
description: This article explains how to solve a slow site issue caused by certain Adobe Commerce cache types being disabled.
exl-id: e4e5a753-efa3-4552-aaf6-28e44efcfa5b
feature: Cache, Observability
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 4239b8a6-e74f-567d-a7a5-b98b9ead0ea4
    internal-label: Observability
  - id: e7dae43f-215c-4cdf-90d3-c5a461a6e669
    internal-label: Admin tools and workspace
subfeature_v2:
  - id: b673188e-f9fa-492a-b470-c8f949bf7827
    internal-label: Cache
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
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

If there are concerns and/or questions whether a certain Adobe Commerce cache type can or should be disabled, [contact Adobe Commerce support](https://experienceleague.adobe.com/en/docs/support-resources/adobe-support-tools-guide/adobe-commerce-support/adobe-commerce-help-center-user-guide) asking for recommendations.

## Related reading

Adobe Commerce cache documentation in our developer documentation:

* [Adobe Commerce cache overview](https://developer.adobe.com/commerce/frontend-core/guide/caching)
* [Manage the cache](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/cli/manage-cache)

Other possible reasons for performance issues and solutions for them:

* [Disable Adobe Commerce Banner output to improve site performance](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26909)
* [MySQL tables are too large](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26945)
* [Slow performance, slow and long running crons](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-42802)
