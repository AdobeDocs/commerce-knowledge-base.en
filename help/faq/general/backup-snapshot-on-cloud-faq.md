---
title: 'Backup (snapshot) on Cloud: FAQ'
description: This article covers the essentials of backing up your environments with snapshots on Adobe Commerce on cloud infrastructure.
exl-id: 0077db74-3e7e-4c98-b215-7f6c089f49e8
---
# Backup (snapshot) on Cloud: FAQ

This article covers the essentials of backing up your environments with snapshots on Adobe Commerce on cloud infrastructure.

## Affected products and versions

* Adobe Commerce on cloud infrastructure 2.2.x, 2.3.x
* Architecture plans:  Starter, Pro Legacy, Pro

## Environment snapshot, Pro plan

### Staging and Production environments

* Your Staging and Production environments are automatically backed up with snapshots **every hour**.
* Automatic snapshots are created **regardless of the live state** of your site (snapshots also created for sites that have not been launched yet). Automatic backups are not publicly accessible because they are stored in a separate system. You can [submit an Adobe Commerce Support ticket](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide.html#submit-ticket) to request a special backup or to restore from a specific backup providing the date, time, and timezone in the ticket. Also, note that support does not perform the rollback or restoration of the database for you - they retrieve the snapshot but you must restore the database yourself.
* Environment snapshots include your full system (file system and the database).
* Manual snapshots are not available for Staging and Production environments on Pro plan.
* The backups are created using the **encrypted Amazon Web Services Elastic Block Store (AWS EBS) snapshots**.
* Retention time for automatic snapshots **is different** and follows [the schedule](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/architecture/pro-architecture.html?lang=en#backup-and-disaster-recovery).


### Integration (Development) environment

* Your [Integration environment](/help/announcements/adobe-commerce-announcements/integration-environment-enhancement-request-pro-and-starter.md) is **not being backed up automatically**, but you may create snapshots **manually**.
* You can create manual snapshots for Integration environments on non-live stores.
* You may have **multiple snapshots** that have been triggered manually.
* A manually triggered snapshot is stored for **7 days**.

 **Related articles in our developer documentation:**

* [Backup and disaster recovery](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/architecture/pro-architecture.html#backup-and-disaster-recovery)
* [Create a snapshot](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/storage/snapshots.html)

## Environment snapshot, Starter plan

* All types of environments (Integration, Staging, Production) **are not being backed up automatically**, but you may create snapshots manually.
* You may create manual snapshots **regardless of the live state** of your site (snapshots also created for sites that have not been launched yet).
* A manually triggered snapshot is stored for **7 days**.

## Restore an environment snapshot

To restore an existing snapshot, follow the steps in [Snapshots and backup management: Restore a snapshot](https://devdocs.magento.com/cloud/project/project-webint-snap.html#restore-snapshot) in our developer documentation.

## Database (DB) backup

DB backup is a part of a Cloud snapshot:

>
A snapshot is a complete backup of an environment that includes all persistent data from all running services (for example, **your MySQL database**, Redis, and so on) and any files stored on the mounted volumes.

[Snapshots and backup management](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/storage/snapshots.html) in our developer documentation.

Only submit a [support request](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide.html?lang=en#submit-ticket) for a DB snapshot from Pro Production and Staging if you need the DB from a specific point in time. If you need a current backup of your DB only (on any environment), see the knowledge base article: [Generate database dumps on Cloud](/help/how-to/general/create-database-dump-on-cloud.md).
