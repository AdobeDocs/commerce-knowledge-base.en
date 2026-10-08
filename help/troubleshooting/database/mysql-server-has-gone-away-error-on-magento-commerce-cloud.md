---
title: MySQL server has gone away​ error on Adobe Commerce on cloud
description: This article talks about the solution for the issue where you receive an " *SQL server has gone away* " error message in the `cron.log` file. A range of symptoms including image file importing issues or deployment failure may be experienced.
exl-id: 14cb9a6d-6d25-4044-8f52-d65648c03431
feature: Cloud, Paas, Services, Variables
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 5a951749-fac9-5bc7-9a98-ebe4ff066437
    internal-label: Cloud
  - id: 00451af3-7b97-5414-9992-3a6c269e413f
    internal-label: Paas
  - id: da76473c-f99b-5ad0-9b14-896aed473f8a
    internal-label: Services
  - id: 8d0b446f-5b16-5a10-b272-01143504a11c
    internal-label: System
subfeature_v2:
  - id: 2191e157-828a-5358-ad69-ebcaa8402915
    internal-label: Variables
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# MySQL server has gone away​ error on Adobe Commerce on cloud

This article talks about the solution for the issue where you receive an " *SQL server has gone away* " error message in the `cron.log` file. A range of symptoms including image file importing issues or deployment failure may be experienced.

## Affected products and versions

* Adobe Commerce on cloud infrastructure, all [supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf).

## Issue

You receive an " *SQL server has gone away* " error message in the `cron.log` file.

 <u>Steps to reproduce</u>

Import files and trigger a deployment.

 <u>Expected result</u>

Successful deployment.

 <u>Actual result</u>

Error message in `cron.log` :" *SQLSTATE\[HY000\] \[2006\] MySQL server has gone away at/app/AAAAAAAAA/vendor/magento/zendframework1/library/Zend/Db/Adapter/Pdo/Abstract.php:144"*

## Cause

The `default_socket_timeout` value is set too low. This is caused by the setting `default_socket_timeout` . If php doesn't receive anything from the MySQL database within this period, it assumes it is disconnected and throws the error.

## Solution

1. Check the current timeout period for `default_socket_timeout` by running in the CLI: `php -i |grep default_socket_timeout`.
1. Check the current timeout period for `default_socket_timeout` by running in the CLI: `php -i |grep default_socket_timeout`
1. Depending on the timeout setting increase, the `default_socket_timeout` variable to the expected longest possible run time in the `/etc/platform/<project_name>/php.ini` file. It is suggested that you set between 10-15 mins.
1. Commit it to GIT and redeploy.

## Related reading

* [Database best practices for Adobe Commerce on cloud infrastructure](https://experienceleague.adobe.com/docs/commerce-operations/implementation-playbook/best-practices/planning/database-on-cloud.html)
* [Most common database issues in Adobe Commerce on cloud infrastructure](https://experienceleague.adobe.com/docs/commerce-operations/implementation-playbook/best-practices/maintenance/resolve-database-performance-issues.html)
