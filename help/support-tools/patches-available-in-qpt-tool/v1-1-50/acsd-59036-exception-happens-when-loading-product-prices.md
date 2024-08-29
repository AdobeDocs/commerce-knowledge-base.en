---
title: 'ACSD-59036: An exception happens when loading product prices with both lower and upper bound equal to $0' 
description: Apply the ACSD-59036 patch to fix the Adobe Commerce issue where an exception happens when loading product prices with both lower and upper bounds equal to *$0*. 
feature: Search 
role: Admin, Developer
---

# ACSD-59036: An exception happens when loading product prices with both lower and upper bounds equal to *$0*

The ACSD-59036 patch fixes the issue where an exception happens when loading product prices with both lower and upper bounds equal to *$0*. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.1.50 is installed. The patch ID is ACSD-59036. Please note that this issue is scheduled to be fixed in Adobe Commerce 2.4.8.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

Adobe Commerce (all deployment methods) 2.4.7

**Compatible with Adobe Commerce and Magento Open Source versions:**

Adobe Commerce (all deployment methods) 2.4.7 - 2.4.7-p2

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

An exception happens when loading product prices with both lower and upper bounds equal to *$0*.

<u>Steps to reproduce</u>:

1. Create 13 simple products
1. Assign all 13 products to a category
1. Set the price of one product to $1322.94
1. Set the price of all other products to zero ($0)
1. Configure OpenSearch as a search engine
1. In Stores > Configuration > Catalog > Storefront, Set the PLP count to 16
1. Set "Price Navigation Step Calculation" to "Automatic (equalize product counts)"
1. Run full reindex
1. Open the category page
   
<u>Expected results</u>:

The category page displays all products.

<u>Actual results</u>:

An error happens

    ```JSON

    report.CRITICAL: OpenSearch\Common\Exceptions\BadRequest400Exception: {"error":{"root_cause":[{"type":"x_content_parse_exception","reason":"[1:193] [bool] failed to parse field [must]"}],"type":"x_content_parse_exception","reason":"[1:193] [bool] failed to parse field [filter]","caused_by":{"type":"x_content_parse_exception","reason":"[1:193] [bool] failed to parse field [must]","caused_by":{"type":"illegal_argument_exception","reason":"field name is null or empty"}}},"status":400} in /vendor/opensearch-project/opensearch-php/src/OpenSearch/Connections/Connection.php:664
    ```

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [[!DNL Quality Patches Tool] > Usage](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html) in the [!DNL Quality Patches Tool] guide.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/upgrade/apply-patches.html) in the Commerce on Cloud Infrastructure guide.

## Related reading

To learn more about [!DNL Quality Patches Tool], refer to:

* [[!DNL Quality Patches Tool] released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using [!DNL Quality Patches Tool]](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [[!DNL Quality Patches Tool]: Search for patches](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html) in the [!DNL Quality Patches Tool] guide.

