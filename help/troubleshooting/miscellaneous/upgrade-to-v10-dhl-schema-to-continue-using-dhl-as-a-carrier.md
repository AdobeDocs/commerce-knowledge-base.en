---
title: Upgrade to v10 DHL schema to continue offering DHL shipping
labels: patch,troubleshooting,Magento,Adobe Commerce,cloud infrastructure,on-premises,DHL,v10 schema,upgrade,deprecation,v6 schema,2.3.7,2.4.0,2.4.1,2.4.2,2.4.3,2.4.3-p2,2.4.3-p3,2.4.4

description: This article provides a solution to allow merchants to continue offering DHL shipping after the DHL schema 6.2 gets deprecated in December 2022, by upgrading to schema 10.0 or by applying the AC-3023 patch.
---

# Upgrade to version 10.0 DHL schema to continue offering DHL shipping

This article provides a solution to allow merchants to continue offering DHL shipping after the DHL schema version 6.2 gets deprecated in the end of December 2022.

## Affected products and versions

* Adobe Commerce 2.4.5 and earlier versions, all deployment methods.

## Issue

In August 2022, we released the [upgrade of DHL schema version 6.2. along with a fix patch](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/adobe-commerce-dhl-upgrade-patch.html?lang=en) to continue offering DHL shipping. DHL is again introducing a newer schema – version 10.0 – in October 2022, and the previous version (6.2 schema) will get deprecated in the end of December 2022. Adobe Commerce 2.4.5 and earlier DHL integration only supports version 6.2.

## Solution

Adobe Commerce 2.4.5-p1 and 2.4.4-p2 which is scheduled for release in October 2022, will contain the new DHL schema version 10.0. So merchants who upgrade to 2.4.5-p1 and 2.4.4-p2 will not have to do anything since they will have the new DHL schema integrated with their new Adobe Commerce versions. We encourage merchants to upgrade to 2.4.5-p1 and 2.4.4-p2 before the deprecation of DHL schema 6.2. in the end of December 2022.

For merchants who do not wish to upgrade to 2.4.5-p1 and 2.4.4-p2 will need to apply a fix patch if they want to continue offering DHL shipping.

## Patch

The patch ID is AC-3023 available in the Quality Patches Tool version 1.1.21.

Refer the following links on how to use Quality Patches Tool and install patches depending on your deployment methods: 

* Adobe Commerce on-premise: [Quality Patches Tools > Usage](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/usage.html) in Adobe Experience League.
* Adobe Commerce on cloud infrastructure: [Upgrades and Patches > Apply Patches](https://devdocs.magento.com/cloud/project/project-patch.html) in our developer documentation.

**The patch is applicable for the following Adobe Commerce versions (all deployment methods):**

* 2.3.7, 2.4.0, 2.4.1, 2.4.2, 2.4.3, 2.4.3-p2, 2.4.3-p3, 2.4.4

## Useful links

* [Quality Patches Tool > Release Notes](https://experienceleague.adobe.com/docs/commerce-operations/tools/quality-patches-tool/release-notes.html?lang=en) in Adobe Experience League.

* [Quality Patches Tools landing page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html) in Adobe Experience League.

## Related reading

* [Apply a patch to continue offering DHL as shipping carrier](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/adobe-commerce-dhl-upgrade-patch.html?lang=en) in Adobe Experience League. 

* [Shipping Carriers > DHL](https://docs.magento.com/user-guide/shipping/dhl.html) in our user guide.
* [Delivery Methods](https://docs.magento.com/user-guide/configuration/sales/delivery-methods.html) in our user guide.
