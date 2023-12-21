---
title: "ACSD-48910: Bundled product assigned multiple sources go out of stock after invoice and shipping"
description: Apply the ACSD-48910 patch to fix the Adobe Commerce issue where the bundled product assigned to multiple sources goes out-of-stock after an order is invoiced and shipped, even if it still has a non-zero quantity.
feature: CMS, Personalization
role: Admin, Developer
---
# ACSD-48910: Bundled product assigned multiple sources go out of stock after invoice and shipping

The ASCD-48910 patch fixes the issue where the bundled product assigned to multiple sources goes out of stock after an order is invoiced and shipped, even if it still has a non-zero quantity. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.1.42 is installed. The patch ID is ASCD-48910. Please note that the issue was fixed in Adobe Commerce 2.4.6.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.5-p3

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.4.5 - 2.4.5-p5

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

The bundled product assigned to multiple sources goes out of stock after invoicing and shipping, even if it's still available.


