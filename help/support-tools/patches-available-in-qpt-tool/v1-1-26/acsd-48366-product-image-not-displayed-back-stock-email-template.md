---
title: 'ACSD-48366: product image not displayed on [!UICONTROL Back to Stock] email template'
description: Apply the ACSD-48366 patch to fix the Adobe Commerce issue where the product thumbnail image is not displayed in product's stock alert email.
---
# ACSD-48366: product image not displayed on [!UICONTROL Back to Stock] email template

The ACSD-48366 patch fixes the issue where the product thumbnail image is not displayed in product's stock alert email. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.1.26 is installed. The patch ID is ACSD-48366. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.7.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.5

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.4.4 - 2.4.5-p1

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

The product image is not displayed on the [!UICONTROL Back to Stock] email template.

<u>Steps to reproduce</u>:

1. Enable *[!UICONTROL Product Alert]* for *[!UICONTROL Back in Stock]* by going to **[!UICONTROL Store]** > **[UICONTROL Configuration]** > **[!UICONTROL Catalog]** > **[!UICONTROL Product Alert]** > **[!UICONTROL Allow Alert When Produt Comes Back in Stock]** = *[!UICONTROL Yes]*.
1. Enable Display 