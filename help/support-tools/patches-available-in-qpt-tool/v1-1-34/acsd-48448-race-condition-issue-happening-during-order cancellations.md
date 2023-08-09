---
title: "ACSD-48448: Race condition issue during order cancellations causing duplicated entry in inventory_reservation table"
description: Apply the ACSD-48448 patch to fix the Adobe Commerce performance issue where the Race condition issue is happening during the order cancellations, which causes duplicated entry in the inventory_reservation table.
feature:
role:
---
# ACSD-48448: Race condition issue during order cancellations causing duplicated entry in inventory_reservation table

The ACSD-48448 patch fixes the issue where the Race condition issue is happening during the order cancellations, which causes duplicated entry in the inventory_reservation table. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.34 is installed. The patch ID is ACSD-48448. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.7.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.2-p2 and 2.4.6

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.4.2 - 2.4.6-p1

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

Race condition issue is happening during the order cancellations, which causes duplicated entry in the inventory_reservation table.

<u>Steps to reproduce</u>:

1. Place an order.
1. Check the `inventory_reservation` table to make sure there is a record for `order_placed` event.
1. Run the attached script to cancel the order in parallel (remember to change the URL and orderID)