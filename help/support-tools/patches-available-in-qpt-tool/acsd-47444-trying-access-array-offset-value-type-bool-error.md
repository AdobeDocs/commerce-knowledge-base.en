---
title: "ACSD-47444: _Trying to access [!DNL array] offset on value of type bool_ error when accessing certain non-existing category paths for known products on PHP 7.4"
description: Apply the ACSD-47444 patch to fix the Adobe Commerce issue where there is a _Trying to access [!DNL array] offset on value of type bool_ error when accessing certain non-existing category paths for known products, on PHP 7.4.
---

# ACSD-47444: _Trying to access [!DNL array] offset on value of type bool_ error when accessing certain non-existing category paths for known products on PHP 7.4

The ACSD-47444 patch solves the issue where you see _Trying to access [!DNL array] offset on value of type bool_ error when accessing certain non-existing category paths for known products on PHP 7.4. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.1.22 is installed.  

## Affected products and versions

**The patch is created for Adobe Commerce version:**
* Adobe Commerce (all deployment methods) 2.4.2-p1

**Compatible with Adobe Commerce versions:**
* Adobe Commerce (all deployment methods) 2.4.0 - 2.4.2-p2

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

You experience the following error: _Trying to access [!DNL array] offset on value of type bool_ when accessing certain non-existing category paths for known products, on PHP 7.4.

<u>Prerequisites</u>:

PHP 7.4.

<u>Steps to reproduce</u>:

1. Create a new product.
1. Go to **[!UICONTROL Stores]** > **[!UICONTROL Settings]** > **[!UICONTROL Configuration}** > **[!UICONTROL CATALOG]** > **[!UICONTROL Catalog]**> **[!UICONTROL Search Engine Optimization]** > set **[!UICONTROL Generate "category/product" URL Rewrites]** = _No_.
1. Go to the storefront and visit the URL for the product.

<u>Expected results</u>:

404 page.

<u>Actual results</u>:

500 error:
_Notice: Trying to access [!DNL array] offset on value of type bool in /app/code/Magento/CatalogUrlRewrite/Model/Storage/DynamicStorage.php on line 182_

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [[!DNL Quality Patches Tool] > Usage](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html) in the [!DNL Quality Patches Tool] guide.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about [!DNL Quality Patches Tool], refer to:

* [[!DNL Quality Patches Tool] released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using [!DNL Quality Patches Tool]](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html) in the [!DNL Quality Patches Tool] guide.
