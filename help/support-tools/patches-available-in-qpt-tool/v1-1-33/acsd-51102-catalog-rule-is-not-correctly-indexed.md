---
title: "ACSD-51102: Catalog rule that is applied to a large number of products is not correctly indexed"
description: Apply the ACSD-51102 patch to fix the Adobe Commerce issue where a catalog rule that is applied to a large number of products is not correctly indexed when the rule is enabled by a scheduled update.
---
# ACSD-51102: Catalog rule that is applied to a large number of products is not correctly indexed

The ACSD-51102 patch fixes the issue where a catalog rule that is applied to a large number of products is not correctly indexed when the rule is enabled by a scheduled update. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.1.32 is installed. The patch ID is ACSD-51102. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.7.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.3-p1

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.4.2 - 2.4.6

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

A catalog rule that is applied to a large number of products is not correctly indexed when the rule is enabled by a scheduled update.

Prerequisites:

* Cron job is setup and runs every minute.

<u>Steps to reproduce</u>:

1. Create an order with a *Gift Card* and a *simple product* (e.g., *add: SKU: GI000XX000XXX, SKU: PC046CP042076*) – (any payment and shipping method works).
2. Invoice the order.
3. Go to **[!UICONTROL Marketing]** > **[!UICONTROL Gift Card accounts]**. An account is created for the gift card.
4. Now go to **[!UICONTROL Order]**, and create a **[!UICONTROL Credit Memo]**.
5. Change the quantity for the *Gift Card* to 0 and update it. This will create a partial refund for the *simple product*.
6. Click on **[!UICONTROL Refund]**.
7. Now refresh the **[!UICONTROL Marketing]** > **[!UICONTROL Gift Card accounts]**. The newly created account is deleted.

<u>Expected results</u>

The gift card account is available for use as the refund was not created for the gift card.

<u>Actual results</u>

The gift card account is deleted, and the gift card is not refunded.
