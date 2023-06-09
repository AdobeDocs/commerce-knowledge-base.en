---
title: "ACSD-51291: Admin with restricted access to one website can add images/videos to multiple product websites"
description: Apply the ACSD-51291 patch to fix the Adobe Commerce issue where the changes made to a page's text content via [!DNL Page Builder] are not saved.
---
# ACSD-51291: Changes to page's text content via [!DNL Page Builder] aren't saved

The ACSD-51291 patch fixes the issue where the changes made to a page's text content via [!DNL Page Builder] are not saved. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.1.32 is installed. The patch ID is ACSD-51291. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.7.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.5-p2

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.4.3 - 2.4.4-p3, 2.4.5 - 2.4.5-p2

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

Restricted admin with access to one website can add images/videos to the product assigned to multiple websites.

<u>Steps to reproduce</u>

1. Log in as admin.
1. Create second website, store and store view.
1. Create second admin role with all resources for the second website, store and store view only.
1. Create second admin and assign it to the new restricted admin role.
1. Create new product and assign it to both default and new websites.
1. Log out from main admin.
1. Log in as new restricted admin.
1. Edit created product, which is assigned to both websites.
1. Open **[!UICONTROL Images and Videos]** tab.

<u>Expected results</u>:

"Restricted admin is allowed to perform actions with images or videos, only when the admin has rights to all websites which the product is assigned to." message is displayed. "Add Video" button is not active.

<u>Actual results</u>:

Restricted admin can add images and videos if product is assigned to the website, which is not accessible to the restricted admin.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [[!DNL Quality Patches Tool] > Usage](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html) in the [!DNL Quality Patches Tool] guide.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/upgrade/apply-patches.html) in the Commerce on Cloud Infrastructure guide.

## Related reading

To learn more about [!DNL Quality Patches Tool], refer to:

* [[!DNL Quality Patches Tool] released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using [!DNL Quality Patches Tool]](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [[!DNL Quality Patches Tool]: Search for patches](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html) in the [!DNL Quality Patches Tool] guide.
