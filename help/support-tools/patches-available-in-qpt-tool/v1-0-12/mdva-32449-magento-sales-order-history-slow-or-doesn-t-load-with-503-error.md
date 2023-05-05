---
title: "MDVA-32449: sales order history slow or doesn't load with 503 error"
description: The MDVA-32449 patch solves the issue on Adobe Commerce where the sales order history loads slowly or does not load and displays a 503 error. This is an issue when 13000+ customers are assigned to a B2B company. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.12 is installed. Please note that this issue was fixed in Adobe Commerce 2.4.1.
exl-id: e3fd4db2-b706-4712-ba8e-270eaca7fdb2
---
# MDVA-32449: sales order history slow or doesn't load with 503 error

The MDVA-32449 patch solves the issue on Adobe Commerce where the sales order history loads slowly or does not load and displays a 503 error. This is an issue when 13000+ customers are assigned to a B2B company. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.12 is installed. Please note that this issue was fixed in Adobe Commerce 2.4.1.

## Affected products and versions

This is an issue when 13000+ customers are assigned to a B2B company.

**The patch is created for Adobe Commerce version:**

Adobe Commerce on cloud infrastructure 2.4.1

**Compatible with Adobe Commerce versions:**

Adobe Commerce on cloud infrastructure and Adobe Commerce on-premises 2.3.0 - 2.3.5-p2, 2.4.0, 2.4.1

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

Fixes the issue where the order history loads very slowly or does not load at all.

<u>Prerequisites</u>:

13000+ customers assigned to a B2B company

<u>Steps to reproduce</u>:

1. Log in to the storefront as the company admin.
1. Go to sales order history page.

<u>Expected results</u>:

The sales order history page loads normally.

<u>Actual results</u>:

The page loads very slowly or the page may not load and a timeout error is displayed.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to the [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
