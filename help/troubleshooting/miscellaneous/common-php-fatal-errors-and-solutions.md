---
title: Common PHP Fatal Errors and solutions
description: This article lists some common PHP Fatal Error quick examples that you could find when looking through your Adobe Commerce logs and the solutions for problems they indicate.
exl-id: 3e42d38f-97bc-4d38-8e36-23b1453f81d9
feature: Support
role: Developer
---
# Common PHP Fatal Errors and solutions

This article lists some common PHP Fatal Error quick examples that you could find when looking through your Adobe Commerce logs and the solutions for problems they indicate.

## Example

 *'PHP Fatal error:  Maximum execution time of 60 seconds exceeded in....'*

## Solution

You can update the maximum execution time by setting a custom `max_execution_time` value in your `php.ini` file and redeploying.

For example:

`max_execution_time = 120`

Consult the [Customize php.ini settings](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/configure/app/php-settings) article.

## Example

 *'PHP Fatal error: Allowed memory size of 792723456 bytes exhausted'* (That's just an example byte size.)

## Solution

Customize your `php.ini` settings. Consult this [Customize php.ini settings](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/configure/app/php-settings) article.

## Example

 *'PHP Warning: Unknown: failed to open stream: No such file or directory'*

## Solution

Make sure you do not remove the Windows-style endings in the `php.ini` file. On Windows, line-endings are terminated with a combination of a carriage return (ASCII 0x0d or \r) and a newline(\n), also referred to as CR/LF.

## Example

 *'PHP Fatal error: Uncaught PDOException: SQLSTATE\[HY000\] \[1040\] Too many connections in'*

## Solution

The MySQL environment has run out of disk space. Provide more disk space for the MySQL environment.

## Example

 *'PHP Fatal error: Uncaught TypeError: Return value of Magento'*

## Solution

Check the `<root>/tmp` directory because it is probably full. If it is full, provide more space in the directory. This could involve simply moving files to another directory or deleting them.

## Related reading

In our developer documentation:

* [PHP settings errors](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/overview)
* [Required PHP settings](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/prerequisites/php-settings)
* [Redis verification](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/cache/redis/redis-session#verify-redis-connection)
* [Configure Redis](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/cache/redis/config-redis)
* [PHP memory limit error](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/overview)
* [Solutions to common problems - Memory limit](https://developer.adobe.com/commerce/testing/guide/unit/command-line/#solutions-to-common-problems)
