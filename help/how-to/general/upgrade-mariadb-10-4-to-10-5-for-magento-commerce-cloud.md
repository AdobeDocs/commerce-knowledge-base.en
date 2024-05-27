---
title: Upgrade MariaDB 10.4 to 10.5 for Adobe Commerce on cloud
description: MariaDB 10.4 reaches end of support on June 18, 2024. This article explains how to upgrade MariaDB from 10.4 to 10.5 to continue using Adobe Commerce on cloud infrastructure.
feature: Best Practices, Cloud
---
# Upgrade MariaDB 10.4 to 10.5 for Adobe Commerce on cloud

MariaDB is an enterprise open-source database used with Adobe Commerce. 

MariaDB 10.4 reaches the end of support on [June 18, 2024](https://endoflife.date/mariadb). You are no longer PCI compliant when you are on an unsupported version of MariaDB. This article explains how to upgrade from MariaDB 10.4 to 10.5 to continue using Adobe Commerce on cloud infrastructure.

>[!NOTE]
>
>As MariaDB 10.4 reaches end-of-life (EOL), it will no longer be supported in current Adobe Commerce versions. It is best practice to move off any EOL version within 30 days of its EOL.

## Affected product and versions

* All Adobe Commerce on-premises and on cloud infrastructure 2.4.4 and 2.4.5 

## Solution

Adopt the new security-only patches (2.4.4-p9 or 2.4.5-p8) that are releasing on June 11, 2024, to ensure compatibility with MariaDB 10.5. Then, follow the steps below to upgrade from MariaDB 10.4 to 10.5.

### Upgrade steps for cloud deployments

1. Create a [DB backup using ECE-Tools DB backup commands](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/storage/snapshots). This backup must be done before steps 2 and 3 in case something goes wrong while updating tables/rows.
1. [Check and convert all compact tables to dynamic tables](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/maintenance/mariadb-upgrade). This step is required to avoid potential data loss during the database upgrade.
1. Check for MYISAM tables. You need to [convert all MyISAM tables to InnoD](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/planning/database-on-cloud).
1. After you have prepared the database tables and rows (the previous two steps), create a [DB backup using ECE-Tools DB backup commands](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/storage/snapshots).
1. [Open a support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket) to schedule the upgrade from MariaDB 10.4 to 10.5. In the ticket, detail the date and time when you want the DB upgraded. The support team needs 48 hours' notice, and the merchants dev team needs to be available. Once the time and date are agreed for the upgrade, do the following:
    1. Put your site into maintenance mode, and stop any DB activities, for example, crons.
    1. Create a [DB backup using ECE-Tools DB backup commands](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/storage/snapshots).
    1. Let support know that you have completed the backup via your support ticket. To get steps for viewing and tracking your tickets, refer to [Adobe Commerce Help Center User Guide: Track your Tickets](/help/help-center-guide/help-center/magento-help-center-user-guide.md#track-tickets) in our support knowledge base.
    1. The Adobe Commerce support team then begins the MariaDB upgrade process. If all the above steps have been taken, and the database is average size, the process takes about an hour. Larger DBs take longer. Once the upgrade is complete, you are informed via your ticket.
1. Disable maintenance mode. Refer to [Enable or disable maintenance mode](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/tutorials/maintenance-mode) in our developer documentation.

## Related Reading

* [DB upgrade best practices guide](https://experienceleague.adobe.com/en/docs/commerce-operations/upgrade-guide/prepare/prerequisites) for on-premises deployments
* [Upgrade MariaDB 10.0 to 10.2 for Adobe Commerce on cloud](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/how-to/upgrade-mariadb-10-0-to-10-2-for-magento-commerce-cloud) in our support knowledge base
* [Adobe Commerce lifecycle policy](https://experienceleague.adobe.com/en/docs/commerce-operations/release/planning/lifecycle-policy) in our developer documentation
