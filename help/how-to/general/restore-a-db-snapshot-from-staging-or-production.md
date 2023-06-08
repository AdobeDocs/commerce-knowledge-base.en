---
title: Restore a DB snapshot from Staging or Production
description: This article shows how to restore a DB snapshot from Staging or Production on Adobe Commerce on cloud infrastructure.
exl-id: 1026a1c9-0ca0-4823-8c07-ec4ff532606a
---
# Restore a DB snapshot from [!DNL Staging] or [!DNL Production]

This article shows how to restore a DB [!DNL snapshot] from [!DNL Staging] or [!DNL Production] on Adobe Commerce on Cloud Pro infrastructure.

## Affected products and versions

* Adobe Commerce on cloud infrastructure, [all supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf)

Choose the most appropriate for your case:

* [Method 1: Transfer the database [!DNL dump] to your local machine and import it](#meth2).
* [Method 2: Import the database [!DNL dump] directly from the server](#meth3).

## Method 1: Transfer the database [!DNL dump] to your local machine and import it {#meth2}

The steps are:

1. Using [!DNL sFTP], navigate to the location where the database [!DNL snapshot] has been placed, usually on the first server/node of your [!DNL cluster] (For example: `/mnt/recovery-<recovery_id>`).
1. Copy the database [!DNL dump file] (For example: `<cluster ID>.sql.gz` for [!DNL Production] or `<cluster ID_stg>.sql.gz` for [!DNL Staging]) to your local computer.
1. Make sure you have set up the [!DNL SSH tunnel] to connect to the database remotely: [[!DNL SSH] and [!DNL sFTP]: [!DNL SSH tunneling]](https://devdocs.magento.com/cloud/env/environments-ssh.html#env-start-tunn) in our developer documentation.
1. Connect to the database.

    ```sql
    mysql -h <db-host> -P <db-port> -p -u <db-user> <db-name>
    ```

1. [!DNL Drop] the database; at the [!DNL MariaDB] prompt, enter:

   (For [!DNL Production])

    ```sql
    drop database <cluster ID>;
    ```

   (For [!DNL Staging])

    ```sql
    drop database <cluster ID_stg>;
    ```

1. Enter the following command to import the [!DNL snapshot]:

   (For [!DNL Production])

    ```sql
    zcat <cluster ID>.sql.gz | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' | mysql -h 127.0.0.1 -P <db-port> -p -u   <db-user> <db-name>
    ```

   (For [!DNL Staging])

    ```sql
    zcat <cluster ID_stg>.sql.gz | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' | mysql -h 127.0.0.1 -P <db-port> -p -u   <db-user> <db-name>
    ```

## Method 2: Import the database [!DNL dump] directly from the server {#meth3}

The steps are:

1. Navigate to the location where the database [!DNL snapshot] has been placed, usually on the first server/node of your [!DNL cluster] (For example: `/mnt/recovery-<recovery_id>`).
1. To [!DNL drop] and re-create the cloud database, first connect to the database:

    ```sql
    mysql -h 127.0.0.1 -P <db-port> -p -u <db-user> <db-name>
    ```

1. [!DNL Drop] the database; at the [!DNL MariaDB] prompt, enter:

   (For [!DNL Production])

    ```sql
    drop database <cluster ID>;
    ```

   (For [!DNL Staging])

    ```sql
    drop database <cluster ID_stg>;
    ```

1. Enter the following command to import the [!DNL snapshot]:

   (For [!DNL Production])

    ```sql
    zcat <cluster ID>.sql.gz | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' | mysql -h 127.0.0.1 -p -u <db-user> <db-name>
    ```

   (For [!DNL Staging])

    ```sql
    zcat <cluster ID_stg>.sql.gz | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' | mysql -h 127.0.0.1 -p -u <db-user> <db-name>
    ```

## Related reading

In our developer documentation:

* [Import code: Import the database](https://devdocs.magento.com/cloud/setup/first-time-setup-import-import.html#cloud-import-db)
* [[!DNL Snapshots] and [!DNL backup] management: [!DNL Dump] your database](https://devdocs.magento.com/cloud/project/project-webint-snap.html#db-dump)
