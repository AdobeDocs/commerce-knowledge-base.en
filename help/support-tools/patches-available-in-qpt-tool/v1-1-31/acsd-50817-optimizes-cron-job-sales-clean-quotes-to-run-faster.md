---
title: "ACSD-50817: Optimizes CRON job sales_clean_quotes to run faster"
description: Apply the ACSD-50817 patch to fix the Adobe Commerce issue where the CRON job `sales_clean_quotes` has been optimized to run faster by adding a composite index on the *store_id* and *updated_at* columns in the quote table.
---
# ACSD-50817: Optimizes CRON job `sales_clean_quotes` to run faster

The ACSD-50817 patch fixes the issue where the **CRON** job `sales_clean_quotes` has been optimized to run faster by adding a composite index on the *store_id* and *updated_at* columns in the quote table. This patch is available when the [!DNL Quality Patches Tool (QPT)] 1.1.31 is installed. The patch ID is ACSD-50817. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.7.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.5-p1

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.3.7 - 2.4.6

>[!NOTE]
>