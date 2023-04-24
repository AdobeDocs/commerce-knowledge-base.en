---
title: 'MDVA-31759 patch: CSV import ignores attribute updates'
description: The MDVA-31759 patch fixes the issue where CSV import ignores additional attributes with *Dropdown* and *Text Area* types. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.9 is installed. Please note that the issue was fixed in Adobe Commerce 2.4.2.
exl-id: 5426866c-893f-4abe-bfbc-6e7b30dd8dab
---
# MDVA-31759 patch: CSV import ignores attribute updates

The MDVA-31759 patch fixes the issue where CSV import ignores additional attributes with *Dropdown* and *Text Area* types. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.9 is installed. Please note that the issue was fixed in Adobe Commerce 2.4.2.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

Adobe Commerce on cloud infrastructure 2.4.0

**Compatible with Adobe Commerce versions:**

Adobe Commerce on cloud infrastructure and Adobe Commerce on-premises 2.3.0 - 2.4.1

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

CSV import ignores additional attributes with *Dropdown* and *Text Area* types.

<u>Steps to reproduce</u>:

1. Log in to the Commerce Admin.
1. Create a product attribute with the following configuration:
    * **Default Label**: *G003*
    * **Catalog Input Type for Store Owner**: *Text Area* or *Dropdown*
    * **Attribute Code**: *G003*
    * **Scope**: *Global*
1. Add the above attribute to the default attribute set.
1. Create a product with the default attribute set and specify a value for the new attribute.
1. Export the product to CSV.
1. Update the attribute value in the **additional\_attributes** column.
1. Import the updated CSV.

<u>Expected results</u>:

The G003 attribute value is updated.

<u>Actual results</u>:

The G003 attribute value is not updated.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to the [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
