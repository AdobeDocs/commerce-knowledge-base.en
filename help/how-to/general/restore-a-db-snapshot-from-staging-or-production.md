---
title: Restore a DB snapshot from Staging or Production
labels: Cloud,Magento Commerce Cloud,commit,how to,DB,snapshot,database,dump,Adobe Commerce,cloud infrastructure
description: "This article shows how to restore a DB snapshot from Staging or Production on Adobe Commerce on cloud infrastructure."
---

# Restore a DB snapshot from Staging or Production

This article shows how to restore a DB snapshot from Staging or Production on Adobe Commerce on cloud infrastructure.

## Affected products and versions

* Adobe Commerce on cloud infrastructure, [all supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf)

Choose the most appropriate for your case:

* [Method 1: Transfer the database dump to your local machine and import it](#meth2).
* [Method 2: Import the database dump directly from the server](#meth3).

## Method 1: Transfer the database dump to your local machine and import it {#meth2}

The steps are:

1. Using sFTP, navigate to the location where the database snapshot has been placed, usually on the first server/node of your cluster (For example: `/mnt/recovery-<recovery_id>`).
1. Copy the database dump file (For example: `<cluster ID>|<cluster ID_stg>.sql.gz` to your local computer).
1. Make sure you have set up the SSH tunnel to connect to the database remotely: [SSH and sFTP: SSH tunneling](https://devdocs.magento.com/cloud/env/environments-ssh.html#env-start-tunn) in our developer documentation.
1. Connect to the database.

    ```sql
    mysql -h <db-host> -P <db-port> -p -u <db-user> <db-name>
    ```

1. Drop the database; at the MariaDB `[<cluster ID>]>` prompt, enter:

    ```sql
    drop database <cluster ID>;
    ```

1. Enter the following command to import the snapshot:

    ```bash
    zcat <cluster ID>sql.gz | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' | mysql -h 127.0.0.1 -P <db-port> -p -u   <db-user> <db-name>
    ```

## Method 2: Import the database dump directly from the server {#meth3}

The steps are:

1. Navigate to the location where the database snapshot has been placed, usually on the first server/node of your cluster (For example: `/mnt/recovery-<recovery_id>`).
1. To drop and re-create the cloud database, first connect to the database:

    ```sql
    mysql -h 127.0.0.1 -P <db-port> -p -u <db-user> <db-name>
    ```

1. Drop the database; at the MariaDB `[<cluster "ID>]>` prompt, enter:

    ```sql
    drop database <cluster ID>;
    ```

1. Enter the following command to import the snapshot:

    ```bash
    zcat <cluster ID>sql.gz | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' | mysql -h 127.0.0.1 -p -u <db-user> <db-name>
    ```

## Related reading

In our developer documentation:

* [Import code: Import the database](https://devdocs.magento.com/cloud/setup/first-time-setup-import-import.html#cloud-import-db)
* [Snapshots and backup management: Dump your database](https://devdocs.magento.com/cloud/project/project-webint-snap.html#db-dump)
