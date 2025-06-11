---
title: Disable Adobe Commerce Banner output to improve site performance
description: This article provides a fix for low site performance. Low site performance can be caused by the `Magento_Banner` module being enabled but not used. Disabling the module output can improve site performance. Review the article for resolution steps.
exl-id: 90a8bd21-1f2c-4cfe-8213-17f877e20de8
feature: Configuration
role: Developer
---
# Disable Adobe Commerce Banner output to improve site performance

This article provides a fix for low site performance. Low site performance can be caused by the `Magento_Banner` module being enabled but not used. Disabling the module output can improve site performance. Review the article for resolution steps.

>[!NOTE]
>
>If you use the Adobe Commerce Banner functionality, see the [High throughput AJAX requests cause poor performance](/help/troubleshooting/miscellaneous/high-throughput-ajax-requests-cause-poor-performance.md) article in our support knowledge base for recommendations on how to avoid performance issues caused by excessive Ajax requests.

## Affected products and versions

* Adobe Commerce on cloud infrastructure v.2.x.x
* Adobe Commerce on-premises v.2.2.x and 2.3.x

## Issue

The `Magento_Banner` module is enabled, but not used.

To check if this is the case:

For Adobe Commerce on cloud infrastructure 2.2.x:

1. Log in to the Commerce Admin.
1. Navigate to **[!UICONTROL Content]** > **[!UICONTROL Elements]** > **[!UICONTROL Banners]**.
1. If the grid displayed on this page is empty, you do not have any banners.

If you do not see the **[!UICONTROL Banners]** option under **[!UICONTROL Content]** > **[!UICONTROL Elements]**, it means that you have already applied the recommendations from this article.

For Adobe Commerce on cloud infrastructure 2.3.x and newer (the functionality was [renamed in v 2.3.x](https://commerce-docs.github.io/devdocs-archive/2.3/guides/v2.3/release-notes/ReleaseNotes2.3.0Commerce.html#banner-now-dynamic-block)):

1. Log in to the Commerce Admin.
1. Navigate to **[!UICONTROL Content]** > **[!UICONTROL Elements]** > **[!UICONTROL Dynamic Blocks]**.
1. If the grid displayed on this page is empty, you do not have any dynamic blocks (banners).

If you do not see the **[!UICONTROL Dynamic Blocks]** option under **[!UICONTROL Content]** > **[!UICONTROL Elements]**, it means that you have already applied the recommendation from this article. To see the banners option again, reverse the process. 

## Cause

When the `Magento_Banner` module is enabled, Adobe Commerce sends Ajax requests from the storefront to the server to get the banner information. These Ajax requests have a performance impact, especially in high-load (high-volume and high-traffic) conditions. If the functionality is not used, it is recommended that you disable the module output. It is not recommended to disable the module, because of the dependency issues.

## Solution

>[!WARNING]
>
>We strongly recommend testing changes on [Staging/Integration environment](/help/announcements/adobe-commerce-announcements/integration-environment-enhancement-request-pro-and-starter.md) first, before applying it to Production. We also recommend having a recent backup before any manipulations.

1. Disable the `Magento_Banner` module output, as described in [Disable module output](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/files/disable-module-output) in our developer documentation. The module name you need to use is `Magento_Banner`.
1. Deploy your code. For Adobe Commerce on cloud infrastructure, deploy as described in the [Deploy your store](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/deploy/staging-production) article in our developer documentation.
1. After disabling the module output, the menu no longer appears in the admin. 
1. You will no longer see Banner or Dynamic option under **[!UICONTROL Content]** > **[!UICONTROL Elements]**. To show the options again, [enable the module output](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/files/disable-module-output?lang=en#disable-module-output-in-a-simple-deployment).

