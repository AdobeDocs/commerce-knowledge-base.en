---
title: Database errors related to max_allowed_packet on Adobe Commerce
description: This article provides a solution for database connection errors in the `var/log/exception.log` that may occur when importing a large number of products or performing another task that forces the server to handle bigger packets than set in `max_allowed_packet` that is larger than the default, 16MB.
exl-id: e8932b72-91a3-43ea-800e-a6c7a5a17656
feature: Best Practices, Observability, Services
role: Developer
---
# Database errors related to max_allowed_packet on Adobe Commerce

This article provides a solution for database connection errors in the `var/log/exception.log` that may occur when importing a large number of products or performing another task that forces the server to handle bigger packets than set in `max_allowed_packet` that is larger than the default, 16MB.

## Affected products and versions

* Adobe Commerce on-premises, all [supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf)

## Issue

When a [!DNL MySQL] client or the [mysqld](https://dev.mysql.com/doc/refman/8.0/en/mysqld.html) server receives a packet bigger than [max\_allowed\_packet](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_max_allowed_packet) bytes, it issues an [ER\_NET\_PACKET\_TOO\_LARGE](https://dev.mysql.com/doc/mysql-errors/8.0/en/server-error-reference.html#error_er_net_packet_too_large) error (which can be seen in the `exception.log`) and closes the connection. With some clients, you may also get a *Lost connection to [!DNL MySQL] server during query* error if the communication packet is too large.

<u>Steps to reproduce</u>

A variety of tasks can produce this issue. This can include trying to import a large number of products into Adobe Commerce or transactional queries sending back too much data. The result is database connection errors in `var/log/exception.log` and other problems, like products not being successfully imported.

## Cause

The default value of 16MB for the [!DNL MySQL] `max_allowed_packets` setting is not large enough for your needs.

## Solution

1. Identify queries where the individual rows exceed the current `max_allowed_packet` limit. Such queries need to be rewritten to reduce the amount of data being returned. This can be done by having a smaller number of columns in the `SELECT` statement or choosing a smaller data type for various columns as part of the table design. If you have a New Relic account, use the [New Relic APM Errors page](https://docs.newrelic.com/docs/apm/apm-ui-pages/error-analytics/errors-page-explore-events-behind-errors) and the [New Relic APM Databases page](https://docs.newrelic.com/docs/apm/apm-ui-pages/monitoring/databases-page-view-operations-throughput-response-time), and [New Relic Logs](https://docs.newrelic.com/docs/logs/log-management/get-started/get-started-log-management) to search for the relevant queries.
1. For quick remediation, you can temporarily request the `max_allowed_packet` size to be increased when you [submit a ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket), but this is at the discretion of the Customer Engineering team, as too large of a value can cause replication failures by causing network congestion.
1. As a best practice, you should run the following command in your CLI for some of your large database tables:

   ```
   show table status like [table name to match]
   ```

   Evaluate the queries running on these tables to determine if you are exceeding the recommended `max_allowed_packet` size of 16MB. Follow the same process in step one to reduce the data being returned by such queries.

## Related reading

* [On-premises installation overview](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/overview) in our developer documentation.
* [Database upload loses connection to [!DNL MySQL]](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/database/database-upload-loses-connection-to-mysql) in our support knowledge base.
* [Database best practices for Adobe Commerce on cloud infrastructure](https://experienceleague.adobe.com/docs/commerce-operations/implementation-playbook/best-practices/planning/database-on-cloud.html) in our support knowledge base.
* [Best practices to resolve database performance issues](https://experienceleague.adobe.com/docs/commerce-operations/implementation-playbook/best-practices/maintenance/resolve-database-performance-issues.html) in our support knowledge base.
* [Best practices for modifying database tables](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/development/modifying-core-and-third-party-tables#why-adobe-recommends-avoiding-modifications) in the Commerce Implementation Playbook
