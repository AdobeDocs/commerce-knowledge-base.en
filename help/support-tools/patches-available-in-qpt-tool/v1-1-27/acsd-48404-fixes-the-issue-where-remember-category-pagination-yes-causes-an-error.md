---
title: "ACSD-48404: Fixes the issue where Remember Category Pagination = Yes causes an error when pressing the browser's back button."
description: Apply the ACSD-48404 patch to fix the Adobe Commerce issue where "Remember Category Pagination = Yes" causes an error when pressing the browser's back button.
---

# ACSD-48404: fixes the issue where 'remember category pagination = yes' causes an error when pressing the browser's back button.

The ACSD-48404 patch solves/fixes the issue where "Remember Category Pagination = Yes" causes an error when pressing the browser's back button. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 2.4.7 is installed. The patch ID is ACSD-48404. Please note that the issue was fixed/is scheduled to be fixed in Adobe Commerce 2.4.7. (this is optional if the issue really was fixed).

## Affected products and versions

**The patch is created for Adobe Commerce version:**
* Adobe Commerce 2.4.3-p3

**Compatible with Adobe Commerce versions:**
* Adobe Commerce >=2.4.0 <2.4.4

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

'remember category pagination = yes' causes an error when pressing the browser's back button.


<u>Steps to reproduce</u>:

1. Go to Stores -> Configuration -> Catalog -> Catalog -> Storefront. Set "Remember Category Pagination" to Yes.
1. Open a category on the Storefront.
1. Select a value that is not the default value in the "Show Per Page" dropdown. After selecting an option the page reloads.
1. Once the page has been reloaded, click on any product on the catalog page.
1. On the opened product detail page, click the Back button of the browser.

<u>Expected results</u>:
The catalog page is opened again.

<u>Actual results</u>:
The category page returns an error.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [[!DNL Quality Patches Tool] > Usage](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html) in the [!DNL Quality Patches Tool] guide.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/upgrade/apply-patches.html) in the Commerce on Cloud Infrastructure guide.

## Additional steps required after the patch installation

(This section is optional; there might be some steps required after applying the patch to fix the issue.) 

## Related reading

To learn more about [!DNL Quality Patches Tool], refer to:

* [[!DNL Quality Patches Tool] released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using [!DNL Quality Patches Tool]](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html) in the [!DNL Quality Patches Tool] guide.