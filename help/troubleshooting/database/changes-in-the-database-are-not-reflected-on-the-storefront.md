---
title: Changes in the database are not reflected on the storefront
description: This article provides solutions to avoid delays or interruptions in entity updates being applied. This includes how to avoid change log tables from getting oversized and how to set up MySQL table triggers.
exl-id: ac52c808-299f-4d08-902f-f87db1fa7ca6
feature: Catalogs, Categories, Services, Storefront
role: Developer
---
# Changes in the database are not reflected on the storefront

This article provides solutions to avoid delays or interruptions in entity updates being applied. This includes how to avoid change log tables from getting oversized and how to set up MySQL table triggers.

Affected products and versions:

* Adobe Commerce on cloud infrastructure 2.2.x, 2.3.x
* Adobe Commerce on-premises 2.2.x, 2.3.x

## Issue

Changes you make in the database are not reflected on the storefront, or there is a significant delay in the application of entity updates. The entities that might be affected include products, categories, prices, inventory, catalog rules, sales rules and target rules.

## Cause

If your indexers are [configured to update by schedule](https://devdocs.magento.com/guides/v2.3/config-guide/cli/config-cli-subcommands-index.html#configure-indexers), the issue might be caused by one or more tables with change logs being too large or MySQL triggers being not set up.

### Oversized change log tables

The change log tables grow that big if the `indexer_update_all_views` cron job is not completed successfully multiple times.

Change log tables are the database tables where the changes to entities are tracked. A record is stored in a change log table as long as the change is not applied, which is performed by the `indexer_update_all_views` cron job. There are multiple change log tables in a Adobe Commerce database, they are named according to the following pattern: INDEXER\_TABLE\_NAME + ‘\_cl’,  for example `catalog_category_product_cl`, `catalog_product_category_cl`. You can find more details on how changes are tracked in database in the [Indexing overview > Mview](https://devdocs.magento.com/guides/v2.3/extension-dev-guide/indexing.html#m2devgde-mview) article in our developer documentation.

### MySQL database triggers not set up

You would suspect database triggers not being set up, if after adding or changing an entity (product, category, target rule, and so on) - no records are added to the corresponding change log table.

## Solution

>[!WARNING]
>
>We strongly recommend creating a database backup before performing any manipulations, and avoiding them during high site load periods.

### Avoid change log tables being oversized

Ensure that the `indexer_update_all_views` cron job is always successfully completed.

You can use the following SQL query to get all failed instances of the `indexer_update_all_views` cron job:

```sql
select * from cron_schedule where job_code = "indexer_update_all_views" and status
  <> "success" and status <> "pending";
```

Or you can check its status in the logs by searching for the `indexer_update_all_views` entries:

* `<install_directory>/var/log/cron.log` - for versions 2.3.1+ and 2.2.8+
* `<install_directory>/var/log/system.log` - for earlier versions

### Re-set MySQL table triggers

To set up the missing MySQL table triggers, you need to re-set the indexer mode:

1. Switch to 'On Save'.
1. Switch back to 'On Schedule'.

Use the following command to perform this operation.

>[!WARNING]
>
>Before switching indexer modes, we recommend putting your website in [maintenance](https://experienceleague.adobe.com/docs/commerce-operations/configuration-guide/setup/application-modes.html#maintenance-mode) mode and [disable cron jobs](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/configure/app/properties/crons-property.html#disable-cron-jobs) to avoid database locks.

```bash
php bin/magento indexer:set-mode {realtime|schedule} [indexerName]
```

>[!INFO]
>
>The indexers-related database triggers are added when the indexer mode is set to schedule and removed when the indexer mode is set to realtime. If the triggers are missing from your database while the indexers are set to schedule, change the indexers to realtime and then change them back to schedule. This resets the triggers.

## Related reading

<ul><li title="MySQL tables are too large"><a href="/help/troubleshooting/database/mysql-tables-are-too-large.md">MySQL tables are too large</a> in our support knowledge base.</li>
<li title="MySQL tables are too large"><a href="https://devdocs.magento.com/guides/v2.3/extension-dev-guide/indexing.html#m2devgde-mview">Indexer overview > Mview</a> in our developer documentation.</li></ul>
