---
title: "ACSD-51230: Gift card account is deleted"
description: Apply the ACSD-51230 patch to fix the Adobe Commerce issue where the gift card account is deleted when the partial refund of a simple product is processed from an order.
---
# ACSD-51230: Gift card account is deleted 

The ACSD-51230 patch fixes the issue where the gift card account is deleted when the partial refund of a simple product is processed from an order. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.32 is installed. The patch ID is ACSD-51230. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.7.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.3

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.3.7 - 2.4.6

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

The gift card account is deleted when the partial refund of a simple product is processed from an order.

<u>Steps to reproduce</u>:

1. Create an order with Gift Card and a simple product (eg. add: SKU: GI000XX000XXX, SKU: PC046CP042076) – (any payment and shipping method works).
1. Place an order with this bundled product with a quantity greater than 1.