---
title: Performance issues caused by excessive Ajax requests
description: This article provides a patch for the known Adobe Commerce performance issue caused by excessive Ajax requests. The issue was fixed in Adobe Commerce 2.3.4.
exl-id: d9a69406-3970-4556-aa6a-1309b24366d8
feature: Configuration
role: Developer
---
# Performance issues caused by excessive Ajax requests

This article provides a patch for the known Adobe Commerce performance issue caused by excessive Ajax requests. The issue was fixed in Adobe Commerce 2.3.4.

## Issue

Adobe Commerce might be sending redundant [Ajax requests](/help/troubleshooting/miscellaneous/high-throughput-ajax-requests-cause-poor-performance.md) from the storefront to the server to get the banner information and customer information. These Ajax requests have a performance impact, especially in high-load (high-volume and high-traffic) conditions. So if the Banner functionality is not used, it is recommended that you completely [disable the Adobe Commerce Banner module output](/help/troubleshooting/miscellaneous/disable-magento-banner-output-to-improve-site-performance.md) and apply the patch to improve retrieving customer information.

## Patch

The patch is attached to this article. To download it, scroll down to the end of the article and click the file name or click the following link:

 [Download the MDVA-24597\_EE\_2.2.9\_COMPOSER\_v1.patch](assets/MDVA-24597_EE_2.2.9_COMPOSER_v1.patch.zip)

### Compatible Adobe Commerce versions

The patch is valid for the following products and versions:

* Adobe Commerce on cloud infrastructure 2.2.9
* Adobe Commerce on-premises 2.2.9

If you have a different version of Adobe Commerce, consider updating to the latest 2.3.x release. If this is not an option currently, please [contact Adobe Commerce Support](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket) and request a patch for your version.

## How to apply the patch

See [How to apply a composer patch provided by Adobe](/help/how-to/general/how-to-apply-a-composer-patch-provided-by-magento.md) for instructions.

## Attached Files
