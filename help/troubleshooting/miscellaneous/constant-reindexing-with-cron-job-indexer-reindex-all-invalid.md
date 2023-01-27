---
title: Indexes invalidated and `indexer_reindex_all_invalid` run constantly
labels: troubleshooting,error,indexing,crons,site performance,adobe commerce,magento,cron,indexer_reindex_all_invalid,SQL,MySQL,reindex
---

# Indexes invalidated and `indexer_reindex_all_invalid` run constantly

This article provides a possible workaround for the issue when your site has performance issues caused by constant reindexing. This is caused by the [!DNL cron] job `indexer_reindex_all_invalid` continuously running and caches cleaned on [!DNL reindex].

## Affected products and versions

* Adobe Commerce (Cloud & On-Premise) 2.4.0+ (As **[!UICONTROL Category Permissions]** is a Adobe-Commerce-only feature, it will not affect Magento Open Source.)

## Issue

In [!DNL New Relic One] error logs should show `indexer_update_all_views` running many times with a time > 1 second (i.e., it is processing something).

## Cause

When the core Adobe Commerce importer is run (manually or by [!DNL cron]), then a set of plugins across multiple core modules are executed to determine what indexes should be invalidated.

The issue occurs when the **[!UICONTROL Category Permissions]** module is enabled in the [!DNL Commerce Admin]. If this is true then the module’s plugin always invalidates the Product & Category indexes (and linked indexes) when an import is executed. If the standard import types are examined, then they all affect **[!UICONTROL Category Permissions]**. Invalidation is expected.

In addition, when a site has B2B modules enabled if **[!UICONTROL Shared Catalog]** is activated, it turns on and locks **[!UICONTROL Category Permissions]**. Turning off **[!UICONTROL Shared Catalog]** will unlock **[!UICONTROL Category Permissions]**, but not switch it off.

<u>Checking [!DNL cron] logs in your [!DNL MySQL] database</u>:

If you login into your [!DNL MySQL] database, they can check your `cron` log for the **[!DNL reindex all indexes]** process.
This **should** appear many times, but the important factor is that the process does one of two possible things.

The process can only do one of these two things:

1. Nothing: Would take 0 to 1 second (one second or less) - the process checks to see if it needs to do anything, and then stops if it does not need to do anything.
1. [!DNL Reindex] everything: Will always take time - usually minutes.

Normally you would want to see lots of occurrences of the process, but with an execution time of &lt1 second.
A merchant can use this [!DNL MySQL] query to do this:

```sql
SELECT TIMESTAMPDIFF(SECOND, executed_at, finished_at) AS period FROM cron_schedule WHERE job_code = 'indexer_reindex_all_invalid' HAVING period > 1
```

You can see how long a period is recorded by running:

```sql
SELECT executed_at FROM cron_schedule WHERE job_code = 'indexer_reindex_all_invalid' AND executed_at IS NOT NULL ORDER BY executed_at ASC LIMIT 1;
```

If this doesn’t give you a long enough period to make a proper assessment, then you can increase the time a successful `cron` process is kept in the log following this [[!DNL Cron] (scheduled tasks)](https://experienceleague.adobe.com/docs/commerce-admin/systems/tools/cron.html) guide and increasing the **[!DNL Success History Lifetime]** value (the default is only 60 minutes).


## Solution

Extend `Magento\CatalogPermissions\Model\Indexer\Plugin\Import` so that the `afterImportSource` method excludes the custom importer.

```
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

[Configure [!DNL cron] jobs](https://experienceleague.adobe.com/docs/commerce-operations/configuration-guide/cli/configure-cron-jobs.html) in the Adobe Commerce Operations Configuration Guide.
