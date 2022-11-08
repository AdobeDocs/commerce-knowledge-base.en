---
title: 'MDVA-35910: form validation broken when "Login as Customer" disabled'
description: The MDVA-35910 patch solves the issue where the create customer account form validation is broken when the **Login as Customer** extension is disabled. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.19 is installed. The patch ID is MDVA-35910. Please note that the issue was fixed in Adobe Commerce version 2.4.3.
exl-id: fa63d725-33f0-4422-bcd5-d62dfee01b65
---
# MDVA-35910: form validation broken when "Login as Customer" disabled

The MDVA-35910 patch solves the issue where the create customer account form validation is broken when the **Login as Customer** extension is disabled. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.19 is installed. The patch ID is MDVA-35910. Please note that the issue was fixed in Adobe Commerce version 2.4.3.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

Adobe Commerce on cloud infrastructure 2.4.1

**Compatible with Adobe Commerce versions:**

Adobe Commerce (all deployment methods) 2.4.1-2.4.2

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

<u>Steps to reproduce</u>:

1. Navigate to **Stores > Configuration > Customers**. Disable **Login as Customer** in the Admin.
1. Under **Login as Customer**, set **Enable Extension** = *No*.
1. Save the Config, and flush the cache.
1. Navigate back to the storefront, and click **Register** (Create a customer account).
1. Fill out the account form, and confirm if the validation under **Confirm Email** is working or not.

<u>Expected results</u>:

The customer account creation process completes with no errors.

<u>Actual results</u>:

The customer account creation process does not complete, and javascript console errors show instead.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
