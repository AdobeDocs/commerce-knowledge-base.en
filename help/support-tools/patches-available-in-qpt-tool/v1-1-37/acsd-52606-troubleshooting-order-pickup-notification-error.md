---
title: "ACSD-52606: Error message displayed when the user clicks "Notify Order is Ready for Pickup"
description: Apply the ACSD-52606 patch to fix the Adobe Commerce issue where an error message is displayed when the user clicks on "Notify Order is Ready for Pickup".
feature: Orders, User Account
role: Admin, Developer
---
# ACSD-52606: Error message displayed when the user clicks "Notify Order is Ready for Pickup"

The ACSD-52606 patch fixes the issue where an error message "Your order is not ready for pickup" is displayed when the user clicks "Notify Order is Ready for Pickup". This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.37 is installed. The patch ID is ACSD-52606. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.7.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.4

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.4.0 - 2.4.6-p2

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

An error message "Your order is not ready for pickup" is displayed on the screen when the user clicks "Notify Order is Ready for Pickup".

<u>Preconditions</u>:

Inventory modules installed.

<u>Steps to reproduce</u>:

1. Install fresh instance.
1. Create a new source and stock.
1. Assign the new source to the default website.
1. Enable pick-up location for the newly created source.
1. Go to **[!UICONTROL Stores]** -> **[!UICONTROL Configuration]** -> **[!UICONTROL Sales]** -> **[!UICONTROL Delivery Methods]** -> **[!UICONTROL In-Store Delivery]** -> **[!UICONTROL enable In-Store Delivery]**.
1. Create a simple product "In Stock" with QTY=0 for all stocks and Manage Stock = No and assign it to both sources.
1. . Create an order with that product from the frontend, choosing In-Store Pickup as the delivery method.
1. In Admin, go to **[!UICONTROL Sales]** -> **[!UICONTROL Orders]** -> **[!UICONTROL Invoice that order]**.
1. Click "Notify order is ready for pickup".

<u>Expected results</u>:

Customer should be notified without errors.

<u>Actual results</u>:

User get error message "Your order is not ready for pickup".

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or Magento Open Source on-premises: [[!DNL Quality Patches Tool] > Usage](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html) in the [!DNL Quality Patches Tool] guide.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/upgrade/apply-patches.html) in the Commerce on Cloud Infrastructure guide.

## Related reading

To learn more about [!DNL Quality Patches Tool], refer to:

* [[!DNL Quality Patches Tool] released: a new tool to self-serve quality patches](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) in our support knowledge base.
* [Check if patch is available for your Adobe Commerce issue using [!DNL Quality Patches Tool]](/help/support-tools/patches-available-in-qpt-tool/check-patch-for-magento-issue-with-magento-quality-patches.md) in our support knowledge base.

For info about other patches available in QPT, refer to [[!DNL Quality Patches Tool]: Search for patches](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html) in the [!DNL Quality Patches Tool] guide.