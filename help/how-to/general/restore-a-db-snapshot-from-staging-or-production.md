---
title: Restore a DB snapshot from Staging or Production
description: This article shows how to restore a DB snapshot from Staging or Production on Adobe Commerce on cloud infrastructure.
exl-id: 1026a1c9-0ca0-4823-8c07-ec4ff532606a
---
# Restore a DB snapshot from [!DNL Staging] or [!DNL Production]

This article shows how to restore a DB [!DNL snapshot] from [!DNL Staging] or [!DNL Production] on Adobe Commerce on Cloud Pro infrastructure.


>[!NOTE]
>
>These methods will restore the **full snapshot**. 
>If you need to restore the snapshot **partially**—for example, only restoring the catalog tables while leaving the order tables intact—you must consult with your developer or DBA.


## Affected products and versions

* Adobe Commerce on cloud infrastructure, [all supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf)

Choose the most appropriate for your case:

* [Method 1: Transfer the database [!DNL dump] to your local machine and import it](#meth2).
* [Method 2: Import the database [!DNL dump] directly from the server](#meth3).

## Method 1: Transfer the database [!DNL dump] to your local machine and import it {#meth2}


>[!NOTE]
>
> The format of the snapshot on **Azure projects** will be different and contains other databases that **cannot be imported**.  
> Before importing the snapshot, you must take additional steps to **extract the appropriate database** before proceeding with the dump import.

The steps are:

1. Using [!DNL SFTP], navigate to the location where the database [!DNL snapshot] has been placed, usually on the first server/node of your [!DNL cluster] (For example: `/mnt/recovery-<recovery_id>`).  
   > **Azure-based projects:**  
   > If your project is Azure-based (i.e., your project URL looks like `https://us-a1.magento.cloud/projects/<cluster_id>`), the snapshot will be placed in:  
   > * `/mnt/shared/<cluster ID>/all-databases.sql.gz`  
   > * `/mnt/shared/<cluster ID_stg>/all-databases.sql.gz`

   **Azure-specific extraction steps**

   **For Production:**

   ```bash
   cd /mnt/shared/<cluster ID>/
   gunzip all-databases.sql.gz 
   head -n 17 all-databases.sql > <cluster ID>.sql 
   sed -n '/^-- Current Database: `<cluster ID>`/,/^-- Current Database: `/p' all-databases.sql >> <cluster ID>.sql gzip <cluster ID>.sql
   zcat <cluster ID>.sql.gz | \
   sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' | \
   mysql -h 127.0.0.1 \
   -u $DB_USER \
   --password=$MYSQL_PWD $DB_NAME \
   --init-command="SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT ;SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS ;SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION ;SET NAMES utf8 ;SET @OLD_TIME_ZONE=@@TIME_ZONE ;SET TIME_ZONE='+00:00' ;SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 ;SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 ;SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' ;SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0;"
   ```

   **For Staging:**

   ```bash
   cd /mnt/shared/<cluster ID_stg>/
   gunzip all-databases.sql.gz 
   head -n 17 all-databases.sql > <cluster ID_stg>.sql
   sed -n '/^-- Current Database: `<cluster ID_stg>`/,/^-- Current Database: `/p' all-databases.sql >> <cluster ID_stg>.sql 
   gzip <cluster ID_stg>.sql  
   zcat <cluster ID_stg>.sql.gz | \
   sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' | \
   mysql -h 127.0.0.1 \
   -u $DB_USER \
   --password=$MYSQL_PWD $DB_NAME \
   --init-command="SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT ;SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS ;SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION ;SET NAMES utf8 ;SET @OLD_TIME_ZONE=@@TIME_ZONE ;SET TIME_ZONE='+00:00' ;SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 ;SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 ;SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' ;SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0;"
   ```

1. Copy the database [!DNL dump file] (For example: `<cluster ID>.sql.gz` for [!DNL Production] or `<cluster ID_stg>.sql.gz` for [!DNL Staging]) to your local computer.
1. Make sure you have set up the [!DNL SSH tunnel] to connect to the database remotely: [[!DNL SSH] and [!DNL sFTP]: [!DNL SSH tunneling]](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/secure-connections#env-start-tunn) in our developer documentation.
1. Connect to the database.

    ```bash
    mysql -h <db-host> -P <db-port> -p -u <db-user> <db-name>
    ```

1. [!DNL Drop] the database; at the [!DNL MariaDB] prompt, enter:

   (For [!DNL Production])

    ```bash
    drop database <cluster ID>;
    ```

   (For [!DNL Staging])

    ```bash
    drop database <cluster ID_stg>;
    ```

1. Enter the following command to import the [!DNL snapshot]:

   (For [!DNL Production])

    ```bash
    zcat <cluster ID>.sql.gz | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' | mysql -h 127.0.0.1 -P <db-port> -p -u   <db-user> <db-name>
    ```

   (For [!DNL Staging])

    ```bash
    zcat <cluster ID_stg>.sql.gz | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' | mysql -h 127.0.0.1 -P <db-port> -p -u   <db-user> <db-name>
    ```

## Method 2: Import the database [!DNL dump] directly from the server {#meth3}

The steps are:

1. Navigate to the location where the database [!DNL snapshot] has been placed, usually on the first server/node of your [!DNL cluster] (For example: `/mnt/recovery-<recovery_id>`).
1. To [!DNL drop] and re-create the cloud database, first connect to the database:

    ```bash
    mysql -h 127.0.0.1 -P <db-port> -p -u <db-user> <db-name>
    ```

1. [!DNL Drop] the database; at the [!DNL MariaDB] prompt, enter:

   (For [!DNL Production])

    ```bash
    drop database <cluster ID>;
    ```

   (For [!DNL Staging])

    ```bash
    drop database <cluster ID_stg>;
    ```

1. After dropping the database, recreate the database:

    ```bash
    create database [database_name];
    ```

1. Enter the following command to import the [!DNL snapshot]:

   (For importing the database backup from [!DNL Production])

    ```bash
    zcat <cluster ID>.sql.gz | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' | mysql -h 127.0.0.1 -p -u <db-user> <db-name>
    ```

   (For importing the database backup from [!DNL Staging])

    ```bash
    zcat <cluster ID_stg>.sql.gz | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' | mysql -h 127.0.0.1 -p -u <db-user> <db-name>
    ```
    
   (For importing a database backup from any other environment)

    ```bash
    zcat <database-backup-name>.sql.gz | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' | mysql -h 127.0.0.1 -p -u <db-user> <db-name>
    ```

   (For importing a database backup from any other environment)

    ```bash
    zcat <database-backup-name>.sql.gz | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' | mysql -h 127.0.0.1 -p -u <db-user> <db-name>
    ```

## Related reading

In our developer documentation:

* [Import code: Import the database](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/deploy/staging-production)
* [[!DNL Snapshots] and [!DNL backup] management: [!DNL Dump] your database](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/storage/snapshots)
* [Backup (snapshot) on Cloud: FAQ](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/faq/backup-snapshot-on-cloud-faq)
