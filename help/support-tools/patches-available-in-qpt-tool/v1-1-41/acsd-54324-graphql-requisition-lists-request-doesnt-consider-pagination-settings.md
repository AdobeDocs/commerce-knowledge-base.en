---
title: 'ACSD-54324: GraphQL requisition_lists request doesn't consider pagination settings'
description: Apply the ACSD-54324 patch to fix the Adobe Commerce issue where the GraphQL requisition_lists request does not consider pagination settings and returns all results.
feature: 
role: Admin, Developer
---
# ACSD-54324: GraphQL `requisition_lists` request doesn't consider pagination settings

The ACSD-54324 patch fixes the issue where the GraphQL `requisition_lists` request does not consider pagination settings and returns all results. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.41 is installed. The patch ID is ACSD-54324. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.7.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.6

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.4.5 - 2.4.6-p3

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

The GraphQL `requisition_lists` request does not consider pagination settings and returns all results.

<u>Steps to reproduce</u>:

1. Login to admin and Go to Admin > Store > Configuration > General > B2B Features > Enable Requisition List, set this field to Yes
1. Login to the frontend and go to My Requisition list from top menu or my account, create multiple requisitions ex : 7
1. After generating customer token, run the below GraphQL requisition_lists query for customer, ensure the page size is less than the total number of requisition list created by you. Ex : 4

    ```
    {
    customer {
    requisition_lists(pageSize: 4, currentPage: 1) {
    items

    { uid name description updated_at items_count }
    total_count
    }
    }
    }
    ```

<u>Expected results</u>:

* The number listed in page size should be returned in total_count not the total number of records. 
* Also, the number of items should be same as the page size

<u>Actual results</u>:

Total number of records is returned for total_count, even if page size is mentioned.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [[!DNL Quality Patches Tool] > Usage](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html) in the [!DNL Quality Patches Tool] guide.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/upgrade/apply-patches.html) in the Commerce on Cloud Infrastructure guide.

## Related reading

To learn more about [!DNL Quality Patches Tool], refer to:

* [[!DNL Quality Patches Tool] released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using [!DNL Quality Patches Tool]](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [[!DNL Quality Patches Tool]: Search for patches](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html) in the [!DNL Quality Patches Tool] guide.
