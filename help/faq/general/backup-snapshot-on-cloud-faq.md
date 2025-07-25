---
title: 'Backup (snapshot) on Cloud: FAQ'
description: This article covers the essentials of backing up your environments with snapshots on Adobe Commerce on cloud infrastructure.
exl-id: 0077db74-3e7e-4c98-b215-7f6c089f49e8
feature: Cloud, Iaas
---
# Backup (snapshot) on Cloud: FAQ

This article covers the backing up your environments with snapshots on Adobe Commerce on cloud infrastructure.

## Affected products and versions

* Adobe Commerce on cloud infrastructure 2.4.x
* Architecture plans:  Starter, Pro Legacy, Pro

## Environment snapshot, Pro plan

### Staging and Production environments

* Manual snapshots are not available for Staging and Production environments on Pro plan.
* Automatic snapshots are created **regardless of the live state** of your site (snapshots are also created for sites that have not been launched yet). Automatic backups are not publicly accessible because they are stored in a separate system.
You can [submit an Adobe Commerce Support ticket](/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide.html#submit-ticket) to request a special backup or to restore from a specific backup providing the date, time, and timezone in the ticket. Once the Infrastructure team has provided the snapshot, to determine the timestamp when it was originally taken, run the following command from the location where the snapshot has been placed:

  `cat /mnt/recovery/vol-<volume_id>/snap.time`

  Example output:

  <strong>2025-01-13 08:42:17.123000+00:00</strong>


* Support does not generate any manual snapshots on demand. Also, note that support does not perform the rollback or restoration of the database for you - they retrieve the snapshot, but you must restore the database yourself.
* Automatic snapshots are created **regardless of the live state** of your site (snapshots are also created for sites that have not been launched yet). Automatic backups are stored in a separate system and are not accessible to the public.
You can [submit an Adobe Commerce Support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md) to request a special backup or to restore from a specific backup providing the date, time, and timezone in the ticket. Support does not generate any manual snapshots on demand.
Also, note that support does not perform the rollback or restoration of the database for you - they retrieve the snapshot, but you must restore the database yourself.
* The backups are created using the **encrypted Amazon Web Services Elastic Block Store (AWS EBS) snapshots**.
* Environment snapshots include your full system (file system and the database).
* Retention time for automatic snapshots **is different** and follows [the schedule](https://experienceleague.adobe.com/en/docs/commerce-on-cloud/user-guide/architecture/pro-architecture#backup-and-disaster-recovery).

>[!NOTE]
>
>The Cloud Console always shows [!UICONTROL No backup] in Staging and Production environments. You can only take backups from the integration environment. Select **[!UICONTROL Backup]** on the ellipsis drop down menu.
>
>![cloud_console_backup.png](assets/cloud_console_backup.png)

### Integration (Development) environment

* Your [Integration environment](/help/announcements/adobe-commerce-announcements/integration-environment-enhancement-request-pro-and-starter.md) is **not being backed up automatically**, but you may create snapshots **manually**.
* You can create manual snapshots for Integration environments on non-live stores.
* You may have **multiple snapshots** that have been triggered manually.
* A manually triggered snapshot is stored for **7 days**.

 **Related articles in our developer documentation:**

* [Backup and disaster recovery](https://experienceleague.adobe.com/en/docs/commerce-on-cloud/user-guide/architecture/pro-architecture#backup-and-disaster-recovery)
* [Create a snapshot](https://experienceleague.adobe.com/en/docs/commerce-on-cloud/user-guide/develop/storage/snapshots)

## Environment snapshot, Starter plan

* All types of environments (Integration, Staging, Production) **are not being backed up automatically**, but you may create snapshots manually.
* You may create manual snapshots **regardless of the live state** of your site (snapshots also created for sites that have not been launched yet).
* A manually triggered snapshot is stored for **7 days**.

## Restore an environment snapshot

To restore an existing snapshot (on the supported environment: Integration, Staging, Production on Starter plan or Integration on Pro plan), follow the steps in [Backup management: Restore a manual backup](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/storage/snapshots#restore-a-manual-backup) in our Commerce on Cloud Infrastructure Guide.

## Database (DB) backup

DB backup is a part of a Cloud snapshot:

A snapshot is a complete backup of an environment that includes all persistent data from all running services (for example, **your MySQL database**, Redis, and so on) and any files stored on the mounted volumes.

>[!NOTE]
>
>The mounted volumes only include/refer to the [writable mounts](https://experienceleague.adobe.com/en/docs/commerce-on-cloud/user-guide/configure/app/properties/properties#mounts) and will not include all of your `/app` directory. As for the other files, they are created/generated by [the build and deployment process](https://experienceleague.adobe.com/en/docs/commerce-on-cloud/user-guide/architecture/pro-develop-deploy-workflow#deployment-workflow), and you will also have to check out the remaining files from your Git repository.

[Snapshots and backup management](https://experienceleague.adobe.com/en/docs/commerce-on-cloud/user-guide/develop/storage/snapshots) in our developer documentation.

Only submit a [support request](/help/help-center-guide/help-center/magento-help-center-user-guide.md) for a DB snapshot from Pro Production and Staging if you need the DB from a specific point in time. If you need a current backup of your DB only (on any environment), see the knowledge base article: [Generate database dumps on Cloud](/help/how-to/general/create-database-dump-on-cloud.md).
