---
title: Best practice for OPcache memory size in Adobe Commerce
description: "For Adobe Commerce on cloud infrastructure Pro plan architecture 2.3.x - 2.4.x, it is recommended to set `opcache.memory_consumption` to at least 2GB, to avoid performance degradation."
---

# Best practice for OPcache memory size in Adobe Commerce

For Adobe Commerce on cloud infrastructure Pro plan architecture 2.3.x - 2.4.x, it is recommended to set `opcache.memory_consumption` to at least 2GB, to avoid performance degradation.

## Affected products and versions

* Adobe Commerce on cloud infrastructure Pro plan architecture 2.3.x - 2.4.x
* PHP 7.0 - PHP 8.0 and later

## Best practice

Allocate at least 2GB of memory for the [OPcache PHP module](https://www.php.net/manual/en/book.opcache.php).

The OPcache module is configured in the `php.ini` file. To allocate 2048MB of memory, set `opcache.memory_consumption =  2048` . For more details see [Performance Best Practices - PHP Settings](https://devdocs.magento.com/guides/v2.3/performance-best-practices/software.html#php-settings) and [Configure PHP options](https://devdocs.magento.com/cloud/project/project-conf-files_magento-app.html#customize-phpini-settings) in our developer documentation.

## Related reading

Best practices for improving Adobe Commerce on cloud infrastructure site performance in our support knowledge base:

* [Database best practices for Adobe Commerce on cloud infrastructure](/help/best-practices/database/database-best-practices-for-magento-commerce-cloud.md)
* [Most common database issues in Adobe Commerce on cloud infrastructure](/help/best-practices/database/most-common-database-issues-in-magento-commerce-cloud.md)
* [Indexers "Update On Schedule" optimizes Adobe Commerce performance](/help/best-practices/performance/indexers-update-on-schedule-optimizes-magento-performance.md)
