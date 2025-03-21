---
title: Apply a patch to continue offering DHL as shipping carrier
description: This article provides a patch, allowing merchants using Adobe Commerce 2.4.4 and earlier to continue offering DHL shipping, after the DHL schema 6.0 gets deprecated in the end of July - September 2022.
exl-id: 4350e83a-495b-41b4-a526-dae5923e9d41
feature: Orders, Shipping/Delivery, Upgrade
role: Developer
---
# Apply a patch to continue offering DHL as shipping carrier


## Affected products and versions

* Adobe Commerce 2.4.4 and earlier, all deployment methods.

## Issue

DHL is introducing a 6.2 schema version and is deprecating version 6.0 by the end of July - September 2022. Adobe Commerce 2.4.4 and earlier DHL integration only supports version 6.0.

## Solution

Adobe Commerce 2.4.5, scheduled for release in August 2022, will contain the upgraded integration with DHL using the version 6.2 schema. Until the new version is released (or in case you choose not to upgrade), we encourage you to apply the AC-3022 patch, implementing the version 6.2 DHL schema support, to continue offering DHL shipments in your store after the deprecation.

## Patch

The patch ID is AC-3022 available in the Quality Patches Tool version 1.1.16.
Refer to the [Quality Patches Tool (QPT) > Usage](https://experienceleague.adobe.com/en/docs/commerce-operations/tools/quality-patches-tool/usage) article in our developer documentation for information on how to use QPT and install patches.

The patch is applicable for the following Adobe Commerce versions:

* 2.4.0 - 2.4.4-p1
* 2.3.7

## Related reading

* [Shipping Carriers > DHL](https://experienceleague.adobe.com/en/docs/commerce-admin/stores-sales/delivery/shipping-carriers/dhl) in our user guide
* [Delivery Methods](https://experienceleague.adobe.com/en/docs/commerce-admin/config/sales/delivery-methods) in our user guide
