---
title: Error: **Could not acquire lock for cron job: indexer_update_all_views**
labels: troubleshooting,Could not acquire lock for cron job,error,indexing,crons,site performance
---

This article provides a workaround for the issue when your site has performance issues caused by constant reindexing. This is caused by the CRON Job `indexer_reindex_all_invalid` continously running (and processing) and because on reindex, caches are cleaned.

## Affected products and versions

* Adobe Commerce on-premises x.x.x
* Adobe Commerce on cloud infrastructure x.x.x

(*Alternatively if the same versions on cloud or on-premises are affected you can say:*)

Adobe Commerce (all deployment methods) x.x.x

* Affected extension or technology (e.g. Redis, Fastly): x.x.x

## Issue

A clear description of the issue, including full error messages as text and any important screenshots.
If this is found in a log, provide details: which log, location.

Remove any specific project IDs or customer information from errors and logs! Also make sure sensitive information is not included in screen shots.

If the issue occurs in a very specific situation, provide detailed steps to reproduce, expected result and actual result in the following format:

<ins>Steps to reproduce</ins>:

Prerequisites: ... (if any).

1. First step.
1. Second step.
1. ....

<ins>Expected result</ins>:

Adobe Commerce does this.

<ins>Actual result</ins>:

In New Relic > **Logs** > **Attributes** > apmApplicationNames >[Your APM aplication name] you see the following error message about the `indexer_update_all_views`cron:
**[timestamp] report.Warning. Could not acquire lock for cron job: indexer_update_all_views [] []**

There are many other crons jobs that are pending and in an error state.

You can also see in **System** > **Tools** > **Index Management** many indexes are in an **IDLE** state.

## Cause

When the core Adobe Commerce importer is run (manually or by CRON) then a set of plugins across multiple core modules are executed to determine what indexes should be invalidated.

The issue occurs when the Category Permissions module is enabled in Commerce Admin, if this is true then the module’s plugin always invalidates the Product & Category indexes (and linked indexes) when an import is executed. If the standard import types are examined they they all affect Category Permissions and so the invalidation is expected.

In addition, when a site has the B2B modules enabled if Shared Catalog is activated it turns on and locks Category Permissions. Turning off Shared Catalog will unlock Category Permissions but not switch off.

This is the code that invalidates the indexes:
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

How to fix the issue. Use a numbered list for steps.
Finish the section with the results: error not displayed, deploy works, value changed and how to see the change, etc.

If there is a temporary workaround, specify it as a separate section below this one.

## Related reading

* [Article topic](https://docs.magento.com/user-guide/) in our user guide.
* [Article topic](https://devdocs.magento.com) in our developer documentation. You can also say to differentiate between instructions in devdocs for cloud vs on-premises users: “[Article topic](https://devdocs.magento.com) in our developer documentation for Adobe Commerce on cloud infrastructure." vs "[Article topic](https://devdocs.magento.com) in our developer documentation for Adobe Commerce on-premises."
* [Article topic](https://support.magento.com/hc/en-us) in our support knowledge base.
* Any related resources (blogs, forums, StackOverflow, etc.)
