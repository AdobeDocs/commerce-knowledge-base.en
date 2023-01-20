---
title: Indexes invalidated and 'indexer_reindex_all_invalid' run constantly
labels: troubleshooting,Could not acquire lock for cron job,error,indexing,crons,site performance
---

# Indexes invalidated and 'indexer_reindex_all_invalid' run constantly

This article provides a possible workaround for the issue when your site has performance issues caused by constant reindexing. This is caused by the [!DNL cron] job `indexer_reindex_all_invalid` continuously running and caches are cleaned on reindex.

## Affected products and versions

* Adobe Commerce (Cloud & On-Premise.) 2.4.0+. As Category Permissions is a Adobe Commerce only feature it will not affect Magento Open Source.

## Issue

In New Relic one error logs should show `indexer_update_all_views` running many times with a time > 1s (IE it is processing something).

## Cause

When the core Adobe Commerce importer is run (manually or by CRON) then a set of plugins across multiple core modules are executed to determine what indexes should be invalidated.

The issue occurs when the **[!UICONTROL Category Permissions]** module is enabled in the Commerce Admin, if this is true then the module’s plugin always invalidates the Product & Category indexes (and linked indexes) when an import is executed. If the standard import types are examined then they all affect **[!UICONTROL Category Permissions]**. Invalidation is expected.

In addition, when a site has B2B modules enabled if **[!UICONTROL Shared Catalog]** is activated it turns on and locks **[!UICONTROL Category Permissions]**. Turning off **[!UICONTROL Shared Catalog]** will unlock **[!UICONTROL Category Permissions]** but not switch it off.

## Solution

Extend `Magento\CatalogPermissions\Model\Indexer\Plugin\Import' so that the `afterImportSource` method excludes the custom importer.

    ```php
    public function afterImportSource(\Magento\ImportExport\Model\Import $subject, $import)
    {
        if ($this->config->isEnabled() && $subject->getEntity() !== 'ENTITY_CODE') {
            $this->indexerRegistry->get(\Magento\CatalogPermissions\Model\Indexer\Category::INDEXER_ID)->invalidate();
            $this->indexerRegistry->get(\Magento\CatalogPermissions\Model\Indexer\Product::INDEXER_ID)->invalidate();
        }
        return $import;
    }
    ```

Where `ENTITY_CODE` is the value used for the entity name parameter in the `import.xml` file for the custom importer.

## Related reading

[Configure cron jobs](https://experienceleague.adobe.com/docs/commerce-operations/configuration-guide/cli/configure-cron-jobs.html) in the Adobe Commerce Operations Configuration Guide.
