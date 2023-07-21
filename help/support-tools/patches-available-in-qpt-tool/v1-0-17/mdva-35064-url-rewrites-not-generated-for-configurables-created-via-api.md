---
title: 'MDVA-35064: URL rewrites not generated for configurables created via API'
description: The MDVA-35064 patch fixes the issue where URL rewrites are not being generated for "All store views" for products created via API. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.17 is installed. Please note that the issue was fixed in Adobe Commerce 2.4.3.
exl-id: 0898c5b3-d361-4bcb-af3a-7f76ac8a23e1
feature: REST, Categories, Configuration
---
# MDVA-35064: URL rewrites not generated for configurables created via API

The MDVA-35064 patch fixes the issue where URL rewrites are not being generated for "All store views" for products created via API. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.17 is installed. Please note that the issue was fixed in Adobe Commerce 2.4.3.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

Adobe Commerce on cloud infrastructure 2.3.5-p1

**Compatible with Adobe Commerce versions:**

Adobe Commerce on-premises and Adobe Commerce on cloud infrastructure 2.3.3-2.4.2

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

When configurable products are created via API, the URL rewrites are not generated.

<u>Steps to reproduce</u>:

1. Create a new website, store, and store view.
1. Create a new category.
1. Create a new product and assign it to the newly created category.
1. Assign the product to the main website and the new website.
1. Check the URL table and make sure it contains entries for the product, category/product for each store on each website.
1. Remove product for the second website.

<u>Expected results</u>:

The URL table contains entries for product, category/product only for the stores on the first website.

<u>Actual results</u>:

The URL table contains URL rewrites for all stores on all websites.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to the [Patches available in QPT](https://support.magento.com/hc/en-us/sections/360010506631-Patches-available-in-QPT-tool-) section.
