---
title: "ACSD-52929: Optimizing inventory indexing in async mode"
description: Apply the ACSD-52929 patch to fix the Adobe Commerce issue where the redundant requests to reindex the default source items appear when the inventory indexer is configured in async mode.
feature: Configuration, Inventory
role: Admin, Developer
---
# ACSD-52929: Optimizing inventory indexing in async mode

The ACSD-52929 patch fixes the issue where there are redundant requests to update the inventory items when using the async mode. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.38 is installed. The patch ID is ACSD-52929. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.7.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.5-p2

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.3.7 - 2.4.6-p2

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

Receiving redundant requests to update the inventory items when using the async mode.

<u>Steps to reproduce</u>:

1. Configure [!DNL Rabbit MQ]. 
1. Enable Asynchronous reindex strategy. Go to **[!UICONTROL Stores]** > **[!UICONTROL Config]** > **[!UICONTROL Catalog]** > **[!UICONTROL Inventory]** > **[!UICONTROL Inventory Indexer Setting]** > **[!UICONTROL Stock/Source reindex strategy = Asynchronous]**.
1. Create a custom inventory source.
1. Log into RabbitMQ dashboard and go to the queues tab.
1. Check 'inventory.indexer.sourceItem' queue and ensure it has 0 messages.
1. Open a simple product from the backend and add **[!UICONTROL stock only]** to the custom source and save the product.
1. Load the 'inventory.indexer.sourceItem' queue in RabbitMQ dashboard and then check the messages.

<u>Expected results</u>:

You should be able to see only one message in the queue for the custom source.

<u>Actual results</u>:

2 messages are shown in the queue: one for default source and the other for custom source.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [[!DNL Quality Patches Tool] > Usage](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html) in the [!DNL Quality Patches Tool] guide.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/upgrade/apply-patches.html) in the Commerce on Cloud Infrastructure guide.

## Related reading

To learn more about [!DNL Quality Patches Tool], refer to:

* [[!DNL Quality Patches Tool] released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using [!DNL Quality Patches Tool]](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [[!DNL Quality Patches Tool]: Search for patches](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html) in the [!DNL Quality Patches Tool] guide.
