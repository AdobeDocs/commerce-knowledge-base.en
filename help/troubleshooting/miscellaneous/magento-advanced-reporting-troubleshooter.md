---
title: Advanced Reporting troubleshooter for Adobe Commerce
description: Advanced Reporting issues on Adobe Commerce can be solved using this troubleshooter tool. This includes Advanced Reporting not showing any data and 404 errors. Click on each question to reveal the answer in each step of the troubleshooter.
exl-id: 7ef9870c-b6b6-4144-a5a7-81aa20a1606c
feature: Cache, Support
role: Developer
---
# Advanced Reporting troubleshooter for Adobe Commerce

Advanced Reporting issues on Adobe Commerce can be solved using this troubleshooter tool. This includes Advanced Reporting not showing any data and 404 errors. Click on each question to reveal the answer in each step of the troubleshooter.

## Step 1 - Confirm site meets Advanced Reporting Requirements {#step-1}

+++**Does your website meet Advanced Reporting Requirements?**

You have a 404 Error page when using Advanced Reporting. Does your website meet [Advanced Reporting Requirements](https://docs.magento.com/user-guide/reports/advanced-reporting.html#requirements)?

a. YES – Proceed to [Step 2](#step-2).  
b. NO – Complete the Advanced Reporting requirements for your site by following the steps in [Advanced Reporting Requirements](https://docs.magento.com/user-guide/reports/advanced-reporting.html#requirements). Then, proceed to [Step 2](#step-2).

+++

## Step 2 - Are there orders in multiple base currencies? {#step-2}

+++**Are multiple base currencies used?**

Are multiple base currencies used (in orders and configuration)? Run this SQL command to obtain the current configuration: `SELECT value FROM core_config_data WHERE path = 'currency/options/base';` .

a. YES – You cannot use Advanced Reporting, as we only support one currency.  
b. NO – Output shows only one currency. Example: `USD`. Have multiple base currencies ever been used (in orders)? Run this SQL command to obtain historical orders data:  
`SELECT DISTINCT base_currency_code FROM sales_order;`. 
**NOTE: This command requires a full table scan, so for tables with high numbers of records, this could have a performance impact whilst the query is executing** to obtain historical orders data.
If multiple base currencies have ever been used you cannot use Advanced Reporting, as we only support one currency. If the output shows only one currency proceed to [Step 3](#step-3).

+++

## Step 3 - Check if split database in use {#step-3}

+++**Are you using split database solution?**

Are you using [split database solution](https://devdocs.magento.com/guides/v2.3/config-guide/multi-master/multi-master.html)?

a. YES – Use the patch **MDVA-26831** in [Advanced Reporting 404 error on split database solution](/help/troubleshooting/known-issues-patches-attached/advanced-reporting-404-error-on-split-database-solution.md) and clear cache. Wait for 24 hours for the job to run again and try again.  
b. NO – Proceed to [Step 4](#step-4).

+++

## Step 4 - Confirm Advanced Reporting enabled {#step-4}

+++**Is Advanced Reporting enabled?**

Check **Admin** > **Stores** > **Settings** > **Configuration** > **General** > **Advanced**. For detailed steps, review [Advanced Reporting: Enable Advanced Reporting](https://docs.magento.com/user-guide/reports/advanced-reporting.html#step-1-enable-advanced-reporting).

a. YES – Proceed to [Step 5](#step-5).  
b. NO – [Enable Advanced Reporting](https://docs.magento.com/user-guide/reports/advanced-reporting.html#step-1-enable-advanced-reporting) and save, and wait 24 hours for Adobe Commerce and Advanced Reporting to synchronize. Check if your data now loads. If it does you have solved the issue. If it does not proceed to [Step 5](#step-5).

+++

## Step 5 - Check for token {#step-5}

+++**Is there a token?**

Check that there is a token by running the following query: `SELECT * FROM core_config_data WHERE path LIKE 'analytics/general/token' \G` Is there a token?

a. YES – Proceed to [Step 7](#step-7).  
b. NO – If token value is NULL or there is no record in the database, proceed to [Step 6](#step-6).

+++

## Step 6 - Use the row {#step-6}

+++**Does the query return the row?**

Check counter value in flag table by running this query: ``SELECT * FROM `flag` where `flag_code` = 'analytics_link_subscription_update_reverse_counter'\G;`` Does the query return the row?

a. YES – Take the following steps: 1. Run the query below:  
``DELETE from `flag` where `flag_code` = 'analytics_link_subscription_update_reverse_counter';``  
2\. [Disable and Enable Advanced Reporting module](https://docs.magento.com/user-guide/reports/advanced-reporting.html#step-1-enable-advanced-reporting) in settings and [reauthorize the token](https://docs.magento.com/user-guide/reports/advanced-reporting.html#verify-that-the-integration-is-active).  
3\. Wait 24 hours for Adobe Commerce and Advanced Reporting to synchronize. If you still can't see data in Advanced Reporting, [submit a support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket).  
b. NO – If the query does not return anything, take the following steps: 1. [Disable and Enable Advanced Reporting module](https://docs.magento.com/user-guide/reports/advanced-reporting.html#step-1-enable-advanced-reporting) in settings and [reauthorize the token](https://docs.magento.com/user-guide/reports/advanced-reporting.html#verify-that-the-integration-is-active).  
2\. Wait 24 hours for Adobe Commerce and Advanced Reporting to synchronize. If you still can't see data in Advanced Reporting, [submit a support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket).

+++

## Step 7 - Check for records in `cron_schedule` table {#step-7}

+++**Are there are records in the `cron_schedule` table?**

Check that job `analytics_collect_data` was executed by running this query: `SELECT * FROM cron_schedule WHERE job_code LIKE 'analytics_collect_data' \G`

a. YES – If there are records and the **status** column says _missed_, use the patch in this KB article [Update Advanced Reporting to run on its own cron group](/help/troubleshooting/known-issues-patches-attached/update-advanced-reporting-to-run-on-its-own-cron-group.md).  
b. YES – If there are records and the **status** column says _success_, proceed to [Step 9](#step-9).  
c. YES – If there are records and the **status** column says _error_, proceed to [Step 8.](#step-8)  
d. NO – If there are no records, proceed to [Step 8](#step-8).

+++

## Step 8 - Check for job in `support_report.log` {#step-8}

+++**Was the job logged in `support_report.log`?**

Run the command: `zgrep analytics_collect_data var/log/support_report.log var/log/support_report.log.1.gz | tail`

a. YES – If the output from the query indicates a successful job, for example `Cron Job analytics_collect_data is successfully finished` proceed to [Step 9](#step-9).  
b. NO – If there are no records in the log, [submit a support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket).  
c. YES – If there are records but there is an error, proceed to [Step 10](#step-10).

+++

## Step 9 - Check for `data.tgz` file {#step-9}

+++**Does the file `data.tgz` exist in the system and are there are records in access logs?**

To check that the file `data.tgz` exists, run command:

```
ls -ltr pub/media/analytics/<there should be a directory with hash name>/
```

To check that there are records in access.logs, run command:

```
zgrep -i analytics /var/log/platform/[cluster_id|cluster_id_stg]/access.log* | grep MagentoBI
```

a. YES – If the file `data.tgz` is present and there are records in the access logs, but you still have a 404 error, you need to [submit a support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket).  
b. NO – Proceed to [Step 10](#step-10).

+++

## Step 10 - Check the error message {#step-10}

+++**Is there an error message thrown by the cron job?**

Example: In the core_config_data table you see the error ``The “/app/var/tmp/analytics/tmp/.nfsb3b6041dd44588a0000850c0” file can’t be deleted. Warning!unlink(/app/var/tmp/analytics/tmp/.nfsb3b6041dd44588a0000850c0?lang=en): No such file or directory``
a. YES – Use the ACSD-50165 patch in [The file can’t be deleted. Warning!unlink: No such file or directory error from the Admin](/help/troubleshooting/miscellaneous/file-cannot-be-deleated-no-file-or-directory.md), wait 24 hours for the job to run again and then try again.  
b. NO – Proceed to [Step 11](#step-11).

+++

## Step 11 - Verify if there is Page Builder error {#step-11}

+++**Is there an error caused by Page Builder?**

Example: `report.ERROR: Cron Job analytics_collect_data has an error: substr_count() expects parameter 1 to be string, null given. Statistics: {"sum":0,"count":1,"realmem":0,"emalloc":0,"realmem_start":224919552,"emalloc_start":216398384} [] []`

a. YES – Use the MDVA-19391 patch in [Common Advanced Reporting cron job errors on Adobe Commerce](/help/troubleshooting/known-issues-patches-attached/advanced-reporting-cron-job-errors-magento-commerce.md), wait 24 hours for the job to run again and try again.  
b. NO – [submit a support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket).

+++

[Back to Step 1](#step-1)
