---
title: "ACSD-46520: Incorrect order status when refunded using store credits"
labels: QPT patches,Quality Patches Tool,Support Tools,Magento,Adobe Commerce,cloud infrastructure,on-premises,QPT 1.1.20,incorrect,order status,refund,store,credits,2.4.3,2.4.3-p1,2.4.3-p2,2.4.3-p3,2.4.4,2.4.4-p1,2.4.5
description: This article provides a solution for the issue where users get an incorrect order status when refunded using store credits.
---

# ACSD-46520: Incorrect order status when refunded using store credits

The ACSD-46520 patch solves the issue where users get an incorrect order status when refunded using store credits. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](https://support.magento.com/hc/en-us/articles/360047139492) 1.1.20 is installed. The patch ID is ACSD-46520. Please note that the issue was fixed in Adobe Commerce 2.4.5.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.3 and 2.4.2

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.4.3 - 2.4.5

>![info]
>
>Note: the patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

Users get an incorrect order status when refunded using store credits.

<u>Steps to reproduce</u>:

1. Create a customer account in the frontend and log in.
1. Assign store credits to the customer from the Admin. The store credits should be able to pay the whole order.
1. Place an order using the store credits.
1. Invoice the order.
1. Create a credit memo to refund the full amount of the order.
    * Check **[!UICONTROL Refund to store credit]**
1. Check the order status.

<u>Expected results</u>:

The order status is **Closed**.

<u>Actual results</u>:

The order status is **Complete**, which is not the correct status.

## Apply the patch

To apply individual patches, use the following links depending on your deployment method:

* Adobe Commerce or [!DNL Magento Open Source] on-premises: [Quality Patches Tools > Usage](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html) in Adobe Experience League.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

## Related reading

To learn more about [!DNL Quality Patches Tool], refer to:

* [[!DNL Quality Patches Tool] released: a new tool to self-serve quality patches](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/announcements/commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.html?lang=en) in Adobe Experience League.
* [Check if patch is available for your Adobe Commerce issue using [!DNL Quality Patches Tool]](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/support-tools/patches/check-patch-for-magento-issue-with-magento-quality-patches.html?lang=en) in Adobe Experience League.

For info about other patches available in QPT, refer to [Patches available in QPT](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html) in Adobe Experience League.
