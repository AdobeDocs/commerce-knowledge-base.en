---
title: 'Managed alerts on Adobe Commerce: MariaDB alerts'
description: 'This article provides troubleshooting steps when you receive MariaDB alerts for Adobe Commerce in New Relic. The MariaDB alerts monitor high query load as well as excessive Data Manipulation Language (DML) queries. Both can lead to a degraded user experience or even downtime. You can receive four kinds of alerts:'
exl-id: 707e20e0-faba-4bcd-884c-b54568787442
feature: Cache, Observability, Support, Tools and External Services
role: Admin
---
# Managed alerts on Adobe Commerce: MariaDB alerts

This article provides troubleshooting steps when you receive MariaDB alerts for Adobe Commerce in New Relic. The MariaDB alerts monitor high query load as well as excessive Data Manipulation Language (DML) queries. Both can lead to a degraded user experience or even downtime. You can receive four kinds of alerts:

* DML Queries Warning
* DML Queries Critical

## **Affected products and versions**

Adobe Commerce on cloud infrastructure Pro plan architecture

## Issue

You will receive a managed alert in New Relic if you have signed up to [Managed alerts for Adobe Commerce](/help/support-tools/managed-alerts-for-adobe-commerce/managed-alerts-for-magento-commerce.md) and one or more of the alert thresholds have been surpassed. These alerts were developed by Adobe to give customers a standard set using insights from Support and Engineering.

 **Do!**

* Abort any deployment scheduled until this alert is cleared.
* Put your site into maintenance mode immediately if your site is or becomes completely unresponsive. For steps refer to [Installation Guide > Enable or disable maintenance mode](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/tutorials/maintenance-mode) in our developer documentation. Make sure to add your IP to the exempt IP address list to ensure that you are still able to access your site for troubleshooting. For steps, refer to [Maintain the list of exempt IP addresses](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/tutorials/maintenance-mode#instgde-cli-maint-exempt).
* End any scripts such as imports that may be the cause of the alert if site performance is impacted.

 **Don't!**

* Run indexers or additional crons which may cause additional stress on MariaDB.
* Do any major administrative tasks (i.e., Commerce Admin, data imports / exports).
* Clear your cache.

## Solution

**DML Queries (queries that modify the database using UPDATE, INSERT, and DELETE)**

If you receive a DML Queries Critical alert start at step one. If you receive a DML Queries Warning alert start at step two.

1. Check if an Adobe Commerce support ticket exists. For steps, refer to our knowledge base [Track your support tickets](/help/help-center-guide/help-center/magento-help-center-user-guide.md#track-tickets). Support may have received a New Relic threshold alert, created a ticket and started working on the issue. If no ticket exists, create one. The ticket should have the following information:
1. Contact Reason: select "New Relic MariaDB alert received".
1. Description of the alert.
1. [New Relic Incident link](https://docs.newrelic.com/docs/alerts-applied-intelligence/new-relic-alerts/alert-incidents/view-violation-event-details-incidents). This is included in your [Managed alerts for Adobe Commerce](/help/support-tools/managed-alerts-for-adobe-commerce/managed-alerts-for-magento-commerce.md).
1. To identify the source of the issue, try to identify the DML queries:
1. Review your database operations by using steps from New Relic [APM UI Pages > Monitoring > Databases page](https://docs.newrelic.com/docs/apm/apm-ui-pages/monitoring/databases-page-view-operations-throughput-response-time) .
1. Sort by CALL COUNT, then OPERATION. Review INSERT, DELETE, and UPDATE operations.
1. Look for high AVG.
1. Click through to find database operation callers. This will identify transactions using that query by time.
1. Seek out either code optimizations, or operational optimizations:
1. Code optimizations: Look to optimize queries with bulk inserts / updates, minimizing index usage, or throttling code.
1. Operational optimizations: Offload resource intensive data modifications to lower traffic times.
1. Additional optimizations: Ensure that you are on the latest version of ECE-Tools. For steps, refer to [Cloud for Adobe Commerce > Update ece-tools version](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/dev-tools/ece-tools/update-package) in our developer documentation.

## Related Reading

* To research other common MariaDB issues, refer to [Most common database issues for Adobe Commerce on cloud infrastructure](https://experienceleague.adobe.com/docs/commerce-operations/implementation-playbook/best-practices/maintenance/resolve-database-performance-issues.html).
* To research database best practices, refer to [Database best practices for Adobe Commerce on cloud infrastructure](https://experienceleague.adobe.com/docs/commerce-operations/implementation-playbook/best-practices/planning/database-on-cloud.html).
