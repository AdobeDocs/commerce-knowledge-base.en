---
title: '[!DNL MySQL] tables are too large'
description: This article discusses why it is an issue when any [!DNL MySQL] table gets larger than 1 GB and how to prevent this.
exl-id: 43f74e3b-7f2e-428c-9964-56d2ce98a34d
feature: Services
role: Developer
---
# [!DNL MySQL] tables are too large

This article discusses why it is an issue when any [!DNL MySQL] table gets larger than 1 GB and how to prevent this.

## Affected products and versions:

* Adobe Commerce on cloud infrastructure  2.x.x
* Adobe Commerce on-premises 2.x.x

## Issue

The [!DNL MySQL] tables size does not directly affect the site performance. However, if a table is large, it means that there are frequent insert operations on this table, with possible extra data or outdated data. [!DNL MySQL] is designed for databases, where the ratio between read/write operations is 80%/20%.  For the large tables, 1 GB and more, [!DNL MySQL] indices, which are designed to speed up performance on read operations, could degrade performance on write operations.

## Solution

Consider the following options to avoid a decrease in performance:

* Create CRON job, that will clean up large tables. See [Find large [!DNL MySQL] tables](/help/how-to/general/find-large-mysql-tables.md) in our support knowledge base for recommendations on how to identify large tables.
* For tables larger than 1 GB, use a [!DNL MySQL] engine optimized for logs writing. For example, the Archive engine.
* Update functionality to avoid storing logs in DB.

## Related reading

* [Oversized change log tables causing delays in entities updates](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/database/changes-in-the-database-are-not-reflected-on-the-storefront) in our support knowledge base
* [Best practices for modifying database tables](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/development/modifying-core-and-third-party-tables#why-adobe-recommends-avoiding-modifications) in the Commerce Implementation Playbook
