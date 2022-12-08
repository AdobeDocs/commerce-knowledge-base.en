
title: "ACSD-47137: improve [!DNL Image Gallery] loading speed pub/media folder big"
description: Apply the ACSD-47137 patch to improve the loading speed of the [!UICONTROL Image Gallery] when the [!UICONTROL pub/media] folder is very big.

# ACSD-47137: improve [!DNL Image Gallery] loading speed when pub/media folder big

The ACSD-47137 patch improves the loading speed of the [!UICONTROL Image Gallery] when the [!UICONTROL pub/media] folder is very big. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.1.24 is installed. The patch ID is ACSD-47137. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.6.

## Affected products and versions

**The patch is created for Adobe Commerce version:**
* Adobe Commerce (all deployment methods) 2.4.4

**Compatible with Adobe Commerce versions:**
* Adobe Commerce (all deployment methods) 2.4.4 - 2.4.5-p1

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

 The loading speed of the [!UICONTROL Image Gallery] is slow when the [!UICONTROL pub/media] folder is very big.

<u>Steps to reproduce</u>:

1. Go to the [!DNL Commerce] Admin > **[!UICONTROL STORES]** > **[!UICONTROL Settings]** > **[!UICONTROL Configuration]** > **[!UICONTROL Advanced]** > **[!UICONTROL System]** > Media Gallery > **[!UICONTROL Enable Old Media Gallery]** to _No_.
1. Clean the config cache.
1. Log out and log in as an admin user again.
1. On the Admin sidebar, to **[!UICONTROL Catalog]** > **[!UICONTROL Categories]** and select the root category.
1. Expand the **[!UICONTROL Content]** section and click on **[!UICONTROL Select from Gallery]**.
1. When loading the page, Adobe Commerce sends `media_gallery/directories/gettree` request to load the media folder tree.

<u>Expected results</u>:

The `media_gallery/directories/gettree` request should load content only from the necessary directories, other than looping the entire path list from the `pub/media/` folder.

<u>Actual results</u>:

The `media_gallery/directories/gettree` request takes a long time to load when the `pub/media/` folder has lots of content.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [[!DNL Quality Patches Tool] > Usage](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html) in the [!DNL Quality Patches Tool] guide.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/upgrade/apply-patches.html) in the Commerce on Cloud Infrastructure guide.

## Related reading

To learn more about [!DNL Quality Patches Tool], refer to:

* [[!DNL Quality Patches Tool] released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using [!DNL Quality Patches Tool]](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [Patches available in QPT](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html) in the [!DNL Quality Patches Tool] guide.
