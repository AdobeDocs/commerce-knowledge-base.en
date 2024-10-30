---
title: "Deployment failed on cache flush: 'There are no commands defined in the 'cache' namespace' error"
description: This article provides a solution for the issue when deployment fails with the following error **There are no commands defined in the cache namespace**.
feature: Deploy
role: Developer
exl-id: ee2bddba-36f7-4aae-87a1-5dbeb80e654e
---

# Deployment failed on cache flush: "There are no commands defined in the 'cache' namespace" error

>[!WARNING]
>
>Backup the database first, if you are doing this in a live Production site, before performing these steps.

This article provides a solution for the issue when your deployment fails and one of the errors in the log looks like this:

```
[YEAR-DAYTIME] ERROR: [127] The command "php ./bin/magento cache:flush --ansi --no-interaction" failed.
        There are no commands defined in the "cache" namespace.
...
      W:     There are no commands defined in the "cache" namespace.
```

## Affected products and versions

Adobe Commerce on cloud infrastructure 2.4.x

## Issue

<u>Steps to reproduce</u>:

Attempt to deploy.

<u>Expected results</u>:

You deploy successfully.

<u>Actual results</u>:

You do not deploy successfully. In the logs you see a deployment error with a message similar to the following *There are no commands in the cache namespace*.

### Cause

The **core_config_data** table contains configurations for a store ID or website ID that no longer exists in the database. This occurs when you have imported a database backup from another instance/environment, and the configurations for those scopes remain in the database though the associated store(s)/website(s) have been deleted.

### Solution

If you have only had one website, then the second test for the websites does not apply, and you only need to test for stores.

To solve this issue, identify the invalid rows left from those configurations.

1. SSH to the server and run this command:

    `bin/magento`

1. The error message may indicate what rows and tables remain in the database from deleted sites. For example, the following is an error indicating that the requested store was not found:

    ```...
    In StoreRepository.php line 112:

    The store that was requested wasn't found. Verify the store and try again.
    ```

1. Run this MySql query to verify that the store cannot be found, which is indicated by the error message in step 2.

    ```sql
    select distinct scope_id from core_config_data where scope='stores' and scope_id not in (select store_id from store);
    ```

1. Run the following MySql statement to delete the invalid rows:

    ```sql
    delete from core_config_data where scope='stores' and scope_id not in (select store_id from store);
    ```

1. Run this command again:

    `bin/magento`

    If you get an error like the below which indicates that the website with id X that was requested was not found you have configurations remaining        in the database from website(s) as-well as store(s) that have been deleted.

    ```
    In WebsiteRepository.php line 110:

    The website with id X that was requested wasn't found. Verify the website and try again.
    ```

    Run this MySql query and verify that the website cannot be found:

    ```sql
    select distinct scope_id from core_config_data where scope='stores' and scope_id not in (select store_id from store);
    ```

1. Run this MySql statement to delete the invalid rows from the website configuration:

    ```sql
    delete from core_config_data where scope='websites' and scope_id not in (select website_id from store_website);
    ```

To confirm that the solution worked, run the `bin/magento` command again. You should no longer see the errors and can successfully deploy.

## Related reading

* [Adobe Commerce deployment troubleshooter](/docs/commerce-knowledge-base/kb/troubleshooting/deployment/magento-deployment-troubleshooter.html)
* [Checking deployment log if Cloud UI has "log snipped" error](/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/checking-deployment-log-if-the-cloud-ui-shows-log-snipped-error.html)
