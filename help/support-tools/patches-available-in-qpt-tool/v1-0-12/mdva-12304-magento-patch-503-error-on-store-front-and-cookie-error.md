---
title: 'MDVA-12304: 503 error on store front and cookie error'
description: This MDVA-12304 Adobe Commerce patch solves 503 errors on store fronts, with *Unable to send the cookie. Maximum number of cookies would be exceeded.* error message in logs. This is a known Adobe Commerce 2.2.5 issue. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.12 is installed.
exl-id: b4b1a2f7-f328-488f-86b8-576b908792fb
---
# MDVA-12304: 503 error on store front and cookie error

This MDVA-12304 Adobe Commerce patch solves 503 errors on store fronts, with *Unable to send the cookie. Maximum number of cookies would be exceeded.* error message in logs. This is a known Adobe Commerce 2.2.5 issue. This patch is available when the [Quality Patches Tool (QPT)](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.0.12 is installed.

## Affected products and versions

* **The patch is created for Adobe Commerce version:** Adobe Commerce on-premises 2.2.5.
* **Compatible with Adobe Commerce versions:** Adobe Commerce (all deployment methods) 2.x.x.

>[!NOTE]
>
>The patch might become applicable to other versions with new Quality Patches Tool releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://devdocs.magento.com/quality-patches/tool.html#patch-grid). Use the patch ID as a search keyword to locate the patch.

## Issue

Customers get a 503 error when navigating the store front. In the `var/log/exception.log` file there is the following error message *Unable to send the cookie. Maximum number of cookies would be exceeded.*

The issue occurs because the Adobe Commerce default cookies limit is set to 50, and if the client's browser hits the limit, Commerce throws an exception. The solution provided in the patch increases the cookie limit to 200.

 <u>Steps to reproduce:</u>

The 503 error can display at any point when the customer is trying to log in and view their cart.

In the `var/log/exception.log` file there is the following error message *Unable to send the cookie. Maximum number of cookies would be exceeded.*

 <u>Actual result:</u> The customer cannot check their cart or complete their order.

 <u>Expected result:</u> The customer can check their cart and complete their order.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [Software Update Guide > Apply Patches](https://devdocs.magento.com/guides/v2.4/comp-mgr/patching/mqp.html) in our developer documentation.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.


## Related reading

To learn more about Quality Patches Tool, refer to:

* [Quality Patches Tool released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using Quality Patches Tool](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://devdocs.magento.com/quality-patches/tool.html#patch-grid) in our developer documentation.
