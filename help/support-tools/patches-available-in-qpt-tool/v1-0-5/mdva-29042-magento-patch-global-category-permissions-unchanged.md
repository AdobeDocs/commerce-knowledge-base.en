---
title: 'MDVA-29042: global category permissions unchanged'
description: The MDVA-29042 patch fixes the issue where catalog permissions were changed to "*Allow*" automatically after a new product was added to the shared catalog in the Commerce Admin. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.5 is installed. Please note that the issue was fixed in Adobe Commerce 2.3.6 with the B2B extension.
exl-id: 491b8881-87ec-4820-8f87-54961682e961
feature: Catalogs, Categories, Customer Service
---
# MDVA-29042: global category permissions unchanged

The MDVA-29042 patch fixes the issue where catalog permissions were changed to "*Allow*" automatically after a new product was added to the shared catalog in the Commerce Admin. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.5 is installed. Please note that the issue was fixed in Adobe Commerce 2.3.6 with the B2B extension.

## Affected products and versions

Adobe Commerce (all deployment methods) 2.3.3 to 2.3.4-p2 with B2B extension

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

Deselecting a customer group from the global category permissions in the Commerce Admin does not automatically set that customer group to "*Deny*" within category permissions.

<u>Prerequisites</u>:

* B2B instance with a customer group defined and selected under **STORES** > **Configuration** > **CATALOG** > **Catalog** > **Category Permissions** for:
    * **Allow Browsing Category**
    * **Display Product Prices**
    * **Allow Adding to Cart**
* Under each **Category**, the customer group is defined as "*Allow*" for:
    * **Browsing Category**
    * **Display Product Prices**
    * **Add to Cart**

<u>Steps to reproduce</u>:

1. In the Commerce Admin, go to **STORES** > **Configuration** > **CATALOG** > **Catalog** > **Category Permissions** and de-select the customer group from:
    * **Allow Browsing Category**
    * **Display Product Prices**
    * **Allow Adding to Cart**
1. Click the **Save Config** button.
1. Wait for the indexers to run.
1. Look at **CATALOG** > **Categories** > **Category Permissions**.

<u>Expected results</u>:

**Category Permissions** will be set to "*Deny*" for all categories for the customer group.

<u>Actual results</u>:

No change to any category permissions for the customer group.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.

To learn more about B2B company functionality, refer to the following articles in our developer documentation:

* [B2B Developer Guide](https://devdocs.magento.com/guides/v2.4/b2b/bk-b2b.html)
* [Manage company roles](https://devdocs.magento.com/guides/v2.4/b2b/roles.html)
* [Adobe Commerce Enterprise B2B Extension configuration paths reference](https://devdocs.magento.com/guides/v2.4/config-guide/prod/config-reference-b2b.html)
