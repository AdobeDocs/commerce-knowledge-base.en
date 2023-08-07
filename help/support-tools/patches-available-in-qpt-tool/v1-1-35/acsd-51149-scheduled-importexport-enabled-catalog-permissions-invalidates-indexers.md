---
title: "ACSD-51149: Scheduled [!UICONTROL ImportExport] with enabled [!UICONTROL Catalog Permissions] invalidates indexers"
description: Apply the ACSD-51149 patch to fix the Adobe Commerce performance issue where the scheduled ImportExport with enabled Catalog Permissions invalidates indexers.
---
# ACSD-51149: Scheduled ImportExport with enabled Catalog Permissions invalidates indexers

The ACSD-51149 patch fixes the issue where the scheduled [!UICONTROL ImportExport] with enabled [!UICONTROL Catalog Permissions] invalidates indexers. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.35 is installed. The patch ID is ACSD-51149. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.7.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.5

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.3.7 - 2.4.6-p1

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [[!DNL Quality Patches Tool]: Search for patches page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

Scheduled [!UICONTROL ImportExport] with enabled [!UICONTROL Catalog Permissions] invalidates indexers.

<u>Steps to reproduce</u>:

1. Enable Catalog Permissions.
1. Set all indexers to *[!UICONTROL Update by Schedule]*.
1. Create a simple product.
1. Export this product via **[!UICONTROL System]** > **[!UICONTROL Data Transfer]** > **[!UICONTROL Export]**.
1. Download the exported CSV, and put it into the `<AC root folder>/var/import`.
1. Create a scheduled product import with downloaded CSV.