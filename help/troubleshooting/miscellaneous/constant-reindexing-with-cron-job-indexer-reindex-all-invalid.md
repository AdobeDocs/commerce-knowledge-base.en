---
title: "Error: *Could not acquire lock for [!DNL cron] job: indexer_update_all_views*"
labels: troubleshooting,Could not acquire lock for cron job,error,indexing,crons,site performance
---

# Error: *Could not acquire lock for [!DNL cron] job: indexer_update_all_views*

This article provides a workaround for the issue when your site has performance issues caused by constant reindexing. This is caused by the [!DNL cron] job `indexer_reindex_all_invalid` continously running and caches are cleaned on reindex.

## Affected products and versions

* Adobe Commerce (Cloud & On-Premise.) 2.4.0+. As Category Permissions is a Commerce only feature it will not affect Magento Open Source.

## Issue

<!-- Are these the correct steps in the UI to see the error message and is this where users most commonly see the error message **could not acquire lock for cron job: indexer_update_all_views**? Are there other symptoms/errors/logs we should mention? -->

In New Relic > **Logs** > **Attributes** > apmApplicationNames >[Your APM aplication name] you see the following error message about the `indexer_update_all_views` [!DNL cron]:

*[timestamp] report.Warning. Could not acquire lock for [!DNL cron] job: indexer_update_all_views [] []*

There are other [!DNL crons] jobs pending and in an error state.

You can also see in **[!UICONTROL System]** > **[!UICONTROL Tools]** > **[!UICONTROL Index Management]** indexes are in an **[!UICONTROL IDLE]** state.

## Cause

When the core Adobe Commerce importer is run (manually or by CRON) then a set of plugins across multiple core modules are executed to determine what indexes should be invalidated.

The issue occurs when the **[!UICONTROL Category Permissions]** module is enabled in the Commerce Admin, if this is true then the module’s plugin always invalidates the Product & Category indexes (and linked indexes) when an import is executed. If the standard import types are examined then they all affect **[!UICONTROL Category Permissions]**. Invalidation is expected.

In addition, when a site has B2B modules enabled if **[!UICONTROL Shared Catalog]** is activated it turns on and locks **[!UICONTROL Category Permissions]**. Turning off **[!UICONTROL Shared Catalog]** will unlock **[!UICONTROL Category Permissions]** but not switch off.

This is the code that invalidates the indexes:

<!-- Is the below code php? -->

`Magento\CatalogPermissions\Model\Indexer\Plugin\Import`

```php
public function afterImportSource(\Magento\ImportExport\Model\Import $subject, $import)
{
    if ($this->config->isEnabled()) {
        $this->indexerRegistry->get(\Magento\CatalogPermissions\Model\Indexer\Category::INDEXER_ID)->invalidate();
        $this->indexerRegistry->get(\Magento\CatalogPermissions\Model\Indexer\Product::INDEXER_ID)->invalidate();
    }
    return $import;
}
```

## Solution

<!-- Is this solution tested? Has it been approved by another developer or SME? Are there any risks with us recomending this?-->

Write custom import modules that use the core Commerce importer as a base and do not import data that affects **[!UICONTROL Category Permissions]**. 

## Related reading

[Configure cron jobs](https://experienceleague.adobe.com/docs/commerce-operations/configuration-guide/cli/configure-cron-jobs.html) in the Adobe Commerce Operations Configuration Guide.
