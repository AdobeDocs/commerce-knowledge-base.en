---
title: '[!DNL MySQL] disk space is low on Adobe Commerce on cloud infrastructure'
description: This article provides solutions for when you are experiencing very low space or no space for [!DNL MySQL] on Adobe Commerce on cloud infrastructure. Symptoms could include site outages, customers unable to add products to the cart, being unable to connect to the database, access the database remotely, not being able to SSH into node. Symptoms also include Galera, environment sync, PHP, database, and deployment errors as listed below. Click [Solution](https://support.magento.com/hc/en-us/articles/360058472572#solution) to jump directly to the solution section.
exl-id: 788c709e-59f5-4062-ab25-5ce6508f29f9
feature: Catalog Management, Categories, Cloud, Paas, Services
role: Developer
---
# [!DNL MySQL] disk space is low on Adobe Commerce on cloud infrastructure

This article provides solutions for when you are experiencing very low space or no space for [!DNL MySQL] on Adobe Commerce on cloud infrastructure. Symptoms include site outages, customers unable to add products to the cart, being unable to connect to the database, access the database remotely, not being able to SSH into node. Symptoms also include Galera, environment sync, PHP, database, and deployment errors as listed below. Click [Solution](https://support.magento.com/hc/en-us/articles/360058472572#solution) to jump directly to the solution section.

## Affected products and versions

Adobe Commerce on cloud infrastructure 2.3.0-2.3.6-p1, 2.4.0-2.4.2

## Issue

The database gets too big. The symptoms might include losing the database connection, database upload error, and a variety of other issues.

Errors you may encounter:

Galera:

* *SQLSTATE\[08S01\]: Communication link failure: 1047 WSREP has not yet prepared node for application use*   *Import errors:*
* *SQLSTATE\[HY000\]: General error: 1180 Got error 5 "Input/output error"*
* *SQLSTATE\[08S01\]: Communication link failure: 1047 WSREP has not yet prepared node for application use*

Environment sync errors:

* *SQLSTATE: General error: 1180 Got error 5 "Input/output error" during COMMIT*

PHP errors:

* *php: PDO::\_\_construct(): [!DNL MySQL] server has gone away.*
* *php errors: PDO::\_\_construct(): Error while reading greeting packet. PID=NNNN.*
* *ERROR 2013 (HY000): Lost connection to [!DNL MySQL] server at 'reading initial communication packet', system error: 0 "Internal error/check (Not system error)".*

Database errors:

* *Error\_code: 1114*
* *InnoDB: Error (Out of disk space) writing word node to FTS auxiliary index table.*
* *SQLSTATE\[HY000\]: General error: 2006 [!DNL MySQL] server has gone away*
* *\[ERROR\] Slave SQL: Error 'The table `<table\_name>` is full' on query.*
* *Unit mysql.service entered failed state.*
* *error: 'Can't connect to local [!DNL MySQL] server through socket '/var/run/mysqld/mysqld.sock' (111 "Connection refused")'*
* *1205 Lock wait timeout exceeded; try restarting transaction, query was: INSERT INTO \`cron\_schedule\` (\`job\_code\`, \`status\`, \`created\_at\`, \`scheduled\_at\`) VALUES (?, ?, `YYYY-02-07 HH:MM:SS`, `YYYY-MM-DD HH:MM:SS`)*

Deployment errors:

* *E: Command '\['sudo', '-u', `<environment name>`, 'bash', '-c', '/etc/platform/`<environment name>`/post\_deploy.sh'\]' returned non-zero exit status 255*
* *E: Command '\['ssh', u`<node IP address>`, 'sudo /usr/bin/sv -w 30 restart site-`<environment name>`g-nginx'\]' returned non-zero*
* *Upgrading schema.. SQLSTATE\[HY000\]: General error: 1114 The table `<table\_name>` is full*
* *SQLSTATE\[HY000\]: General error: 3 Error writing file ./`<environment name>`/\#*
* *W: `<filename>` (Errcode: 28 "No space left on device")*  *Indexing errors (along with orphaned temporary .ibd files in /tmp):*
* *Catalog Rule indexer throws an exception. The temporary tables don't get cleaned up in the aftermath and then fill the disk on the current [!DNL MySQL] master node*

<u>Steps to reproduce</u>:

 One of the ways you can check if the `/data/mysql` (or wherever [!DNL MySQL] data storage is configured) is full is by running the following command in the CLI:

```bash
df -h
```

Less than 10% of free memory on [!DNL MySQL] disk is a primary indicator of an outage.

## Cause

The `/data/mysql` mount might become full due to a range of issues, such as not having enough inodes, available storage space, and bad queries that generate temporary tables.

## Solution

There is an immediate step that you might take to bring [!DNL MySQL] back on track (or prevent it from getting stuck): free up some space by flushing big tables.

But a long-term solution would be allocating more space and following [Database best practices](https://experienceleague.adobe.com/docs/commerce-operations/implementation-playbook/best-practices/planning/database-on-cloud.html), including enabling the [Order/Invoice/Shipment archive](https://experienceleague.adobe.com/en/docs/commerce-admin/stores-sales/order-management/orders/order-archive) functionality.

Following are details on both quick and long-term solutions.

### Check and free up inodes

Ensure that there are enough available inodes. To do this, run the following command:

```bash
df -i
```

The output would look similar to the following:

```bash
Filesystem Inodes   Used   Free Use% Mounted on
/dev/nvme2n1 655360    1695  653665    1% /data/mysql
```

Check that Use % is <70%. Inodes are correlated with files. If you remove files from the partition, you will free inodes.

### Check and free up storage space

Check available storage space. For this, execute:

```bash
df -k
```

The output would be similar to following:

```bash
Size Used Avail Use% Mounted on·
       50G 49G 95M 100% /data/mysql
```

If the Use % is >70%, you need to take action to free/add some space.

### Check for large `ibtmp1` files

Check for large `ibtmp1` file on `/data/mysql` of each node: this file is the tablespace for temporary tables. If there are bad queries that generate temp tables, they are contained in the `ibtmp1` file. This file is only removed when the database is restarted. If it is taking up all available space, the database must be restarted. If there are bad queries, it will be recreated again.

### Flush large tables

>[!WARNING]
>
>We strongly recommend creating a database backup before performing any manipulations and avoiding them during high site load periods. See [Dump your database](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/storage/snapshots) in our developer documentation.

Check if there are large tables and consider if any of them can be flushed. Do this on the primary (source) node.

For example, tables with reports can usually be flushed. For details on how to find large tables, see the [Find Large [!DNL MySQL] tables](/help/how-to/general/find-large-mysql-tables.md) article.

If there are no huge report tables, consider flushing `_index` tables, just to return the Adobe Commerce application back on track. `index_price` tables would be the best candidates. For example, `catalog_category_product_index_storeX` tables, where X can have values from "1" to the maximum store count. Please mind that you would need to reindex to restore data in these tables, and in the case of big catalogs, this reindex might take a lot of time.

Once you flush them, wait for wsrep sync completion. You can now create backups and take more significant steps to add more space, like allocating/buying more space and enabling [Order/Invoice/Shipment archive](https://experienceleague.adobe.com/en/docs/commerce-admin/stores-sales/order-management/orders/order-archive) functionality.

### Check binary logging settings

Check your [!DNL MySQL] server binary logging settings: `log_bin` and `log_bin_index`. If the settings are enabled, the log files might become huge. [Create a support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket) requesting to purge large binary log files. Also, request to check that binary logging is being configured correctly so that logs are purged periodically and don't take too much space.

If you don't have access to [!DNL MySQL] server settings, request support to check it.

### Reclaim unused allocated disk space

1. SSH into node one and log in to MySQL:

    ```sh
    mysql -h127.0.0.1 -p`php -r "echo (include('app/etc/env.php'))['db']['connection']['default']['password'];"` -u`whoami` `whoami`
    ```

    For detailed steps, refer to [Connect and run queries against the Adobe Commerce database](https://experienceleague.adobe.com/en/docs/commerce-learn/tutorials/backend-development/remote-db-connection-execute-queries).

1. Check for unused space:
 
    ```sql
    SELECT table_name, round((data_length+index_length)/1048576,2) AS size_MB, round((data_free)/1048576,2) AS Allocated_but_unused FROM information_schema.tables WHERE data_free > 1048576*10 ORDER BY data_free DESC;
    ```
  

    Example output:

    | table_name           | size_MB | Allocated_but_unused |
    |----------------------|----------|--------------------------|
    | sales_order_grid  | 28145.20  | 14943.00                 |

    
    Check in the output to see if there is memory that has been allocated but is unused. This occurs when data has been deleted from within a table however the memory is still allocated to that table.


1. Place your site into maintenance mode, and stop cron jobs so that there are no interactions taking place on the database. For steps, refer to [Enable or disable maintenance mode](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/tutorials/maintenance-mode) and [Disable cron jobs](https://experienceleague.adobe.com/en/docs/commerce-on-cloud/user-guide/configure/app/properties/crons-property#disable-cron-jobs).
1. Reclaim that space by recreating the table using the following command (example using the table listed above with the most unused space):

    ```sql
    ALTER TABLE sales_order_grid Engine = "INNODB";
    ```

 1. Run the following query to check for unallocated space for each table that shows a high value within the column **[!UICONTROL Allocated_but_unused]**.

     ```sql
     SELECT table_name, round((data_length+index_length)/1048576,2) as size_MB, round((data_free)/1048576,2) as Allocated_but_unused FROM information_schema.tables WHERE 1 AND data_free > 1048576*10 ORDER BY 
     data_free DESC;
     ```

 
1. Now [Disable maintenance mode](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/tutorials/maintenance-mode#enable-or-disable-maintenance-mode-1) and [Enable cron jobs](https://experienceleague.adobe.com/en/docs/commerce-on-cloud/user-guide/configure/app/properties/crons-property#disable-cron-jobs).


### Allocate/buy more space

Allocate more disk space for [!DNL MySQL] if you have some unused. See the [Check disk space limit](/help/how-to/general/check-disk-space-limit-for-magento-commerce-cloud.md) article to learn how to check if you have free disk space.

* For the Starter plan, all environments, and Pro plan Integration environments, you can allocate the disk space if you have some unused. For details, see the [Allocate more space for [!DNL MySQL]](/help/how-to/general/allocate-more-space-for-mysql-in-magento-commerce-cloud.md).
* For Pro plan Staging and Production environments, [contact support](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket) to allocate more disk space if you have some unused.

If you have reached your space limit and still experience low space issues, consider buying more disk space, contact your Adobe Account Team for details.

## Related reading

[Best practices for modifying database tables](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/development/modifying-core-and-third-party-tables#why-adobe-recommends-avoiding-modifications) in the Commerce Implementation Playbook
