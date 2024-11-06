---
title: Backup issues
description: This article lists the possible solutions for the backup creation issues.
exl-id: 1a6204ad-bd5a-46dc-8a8e-39655a174e09
feature: Storage, Data Import/Export
role: Developer
---
# Backup issues

This article lists the possible solutions for the backup creation issues.

## Affected products and versions

* Adobe Commerce on-premises 2.3.x
* Magento Open Source 2.3.x

## Backup disabled {#backup-disabled}

If the Adobe Commerce backup functionality does not start or displays the following message, you need to enable the feature prior to backing up.

```bash
Backup functionality is disabled.
Backup functionality is currently disabled. Please use other means for backups.
```

Enter the following CLI command:

```bash
bin/magento config:set system/backup/functionality_enabled 1
```

For additional information on backups, see [Back up and roll back the file system, media, and database.](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/tutorials/backup)

## Insufficient disk space {#insufficient-disk-space-trouble-backup-space-}

If the backup failed because of insufficient disk space, you should typically free up disk space by moving some files to another storage device or drive. However, there might be other ways to resolve the issue. See one of the following resources for tips:

* [8 Tips to Solve Linux & Unix Systems Hard Disk Problems Like Disk Full Or Can't Write to the Disk](https://www.cyberciti.biz/datacenter/linux-unix-bsd-osx-cannot-write-to-hard-disk)
* [serverfault: df says disk is full, but it is not](https://serverfault.com/questions/315181/df-says-disk-is-full-but-it-is-not)
* [unix.stackexchange.com: Tracking down where disk space has gone on Linux?](https://unix.stackexchange.com/questions/125429/tracking-down-where-disk-space-has-gone-on-linux)

## Operating system error {#operating-system-error-trouble-backup-os-}

Unfortunately, we can not recommend anything specific because of the variety of errors you might encounter. We can suggest, however, you:

* Contact your system administrator.
* Search public forums like [Stack Exchange](https://unix.stackexchange.com) or [Stack Overflow](https://stackoverflow.com)
* Open a [GitHub issue](https://github.com/magento/magento2/issues) and we'll try to help.

## Backup fails {#backup-fails-trouble-backup-all-}

If the backup fails or if all backup tests fail, it's possible the [Adobe Commerce file system owner](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/prerequisites/file-system/overview) doesn't have sufficient privileges and ownership of the Adobe Commerce file system. For example, another user might own the files or the files might be read-only.

Pay particular attention to file system permissions and ownership of the `<magento_root>/var` directory and subdirectories. For more information, see [Set file system permissions and ownership](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/prerequisites/file-system/configure-permissions).
