---
title: Create database dump on Adobe Commerce on cloud infrastructure
description: This article discusses the possible (and recommended) ways to create a database (DB) dump on Adobe Commerce on cloud infrastructure.
exl-id: 4a2e54ac-8d65-4e51-8337-08f9748dc6c0
---
# Create database dump on Adobe Commerce on cloud infrastructure

This article discusses the possible (and recommended) ways to create a database (DB) dump on Adobe Commerce on cloud infrastructure.

You only need to use one variant (option) to dump your DB. These options apply to any environment type (Integration, Staging, Production) and any plan (Adobe Commerce on cloud infrastructure Starter plan architecture and Adobe Commerce on cloud infrastructure Pro plan architecture).

## Prerequisite: SSH to your environment

To dump your DB on Adobe Commerce on cloud infrastructure with any variant discussed in this article, you must first [SSH to your environment](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/secure-connections.html).

>[!WARNING]
>
>Whether you choose Option 1 or Option 2 please run the command during off peak hours against a database secondary node.

## Option 1: db-dump (**ece-tools; recommended**)

You may dump your DB using the [ECE-Tools](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/dev-tools/ece-tools/update-package.html) command:

```php
vendor/bin/ece-tools db-dump
```

This is the recommended and safest option.

 See [Dump your database (ECE-Tools)](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/storage/snapshots.html#dump-your-database) in our Commerce on Cloud Infrastructure Guide.


## Option 2: mysqldump

>[!WARNING]
>
>Do not run this command against the database cluster. The cluster will not differentiate whether it is run against the database primary or against a secondary. If the cluster runs this command against the primary, the database will be unable to execute writes until the dump is completed and could impact performance and site stability.

You may dump your DB using the native MySQL `mysqldump` command.

The entire command might look as follows:

```sql
mysqldump -h <host> -u <username> -p <password> --single-transaction <db_name> | gzip > /tmp/<dump_name>.sql.gz
```

The database backup created by running the `mysqldump` command and saved in `\tmp`, should be moved from this location. It should not take up storage space in `\tmp` (which might result in problems).

To obtain your DB credentials (host, username, and password), you might call the `MAGENTO_CLOUD_RELATIONSHIPS` environment variable:

```
echo $MAGENTO_CLOUD_RELATIONSHIPS |base64 --d |json_pp
```

 **Related documentation:**

* [mysqldump &ndash; A Database Backup Program](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html) in official MySQL documentation.
* [Cloud variables](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/configure/env/stage/variables-cloud.html) (see `MAGENTO_CLOUD_RELATIONSHIPS`) in our Commerce on Cloud Infrastructure Guide.
