---
title: Fix data not updated in [!DNL Commerce Data Exporter] feeds and [!DNL cron] logs errors with changelog table don't exist
description: This article provides a solution for fixing data synchronization issues caused by using of wrong view id in [!DNL Commerce Data Exporter mview] subscription.
feature: Data Import/Export, Saas, Logs
role: Developer
exl-id: 50f2223b-bfcf-4c3c-b0f1-dbcc4365edc2
---
# Fix data not updated in [!DNL Commerce Data Exporter] feeds and [!DNL cron] logs errors with changelog table don't exist

This article provides a solution for fixing data synchronization issues caused by using the wrong view id in the [!DNL Data Exporter] [[!DNL Mview]](https://developer.adobe.com/commerce/php/development/components/indexing/#mview) subscription. The [!DNL Mview] subscription is used to track changes for database tables.

## Affected products and versions

Adobe Commerce instances where custom code has been applied to data export functionality (`commerce-data-exporter` or `saas-exporter`). The error occurs if the installed [[!DNL SaaS] Data Export version is 103.3.0](https://experienceleague.adobe.com/en/docs/commerce-merchant-services/saas-data-export/release-notes#release-6) or later, and the code directly references the `catalog_data_exporter_products` index.

## Issue

Merchants may find that data updates are missing from the Catalog [!DNL Data Exporter] feed tables and see the following errors in the [!DNL cron] job logs:

```
[2024-05-27T19:00:04.627604+00:00] report.ERROR: Cron Job indexer_clean_all_changelogs has an error: Table catalog_data_exporter_products_cl does not exist. Statistics: {"sum":0,"count":1,"realmem":0,"emalloc":0,"realmem_start":305135616,"emalloc_start":283210384} [] [] 
```

## Cause

Due to name changes in feed tables, indexes, and change log tables in the [!DNL Commerce Data Export] [version 103.3.0](https://experienceleague.adobe.com/en/docs/commerce-merchant-services/saas-data-export/release-notes#release-9) release, the [!DNL Mview] subscriptions in custom extensions that use [!DNL Commerce Data Export] extensions may not work properly.

In this case, the *table does not exist* error occurs because the `catalog_data_exporter` table name was changed to `cde_products_feed`, and you have custom code that references the old name in the [!DNL Data Exporter Mview] subscription.

## Solution

In the customized extension, edit the [!DNL Mview] configuration file (```./etc/mview.xml```) to change the `catalog_data_exporter_products` table name to *`cde_products_feed`*.  

The following example shows the code that specifies the tables tracked by the [!DNL Mview] subscription:

```
<view id="cde_products_feed" class="Magento\CatalogDataExporter\Model\Indexer\ProductFeedIndexer" group="indexer">
     <subscriptions>
         <table name="custom_table" entity_column="product_id" />
     </subscriptions>
</view>
```
 
## Related reading

* [[!DNL SaaS] Data Export Extension Release Notes](https://experienceleague.adobe.com/en/docs/commerce-merchant-services/saas-data-export/release-notes) in the Adobe Commerce Data Export Guide for [!DNL SaaS] Services
* [Best practices for modifying database tables](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/development/modifying-core-and-third-party-tables#why-adobe-recommends-avoiding-modifications) in the Commerce Implementation Playbook
