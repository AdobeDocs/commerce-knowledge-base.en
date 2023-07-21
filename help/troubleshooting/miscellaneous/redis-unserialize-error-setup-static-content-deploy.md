---
title: Redis unserialize error `setup:static-content:deploy`
description: This article provides a fix for the Redis unserialize error when running `magento setup:static-content:deploy`.
exl-id: 4bc88933-3bf9-4742-b864-b82d3c1b07a9
feature: "Cache, Deploy"
---
# Redis unserialize error `setup:static-content:deploy`

This article provides a fix for the Redis unserialize error when running `magento setup:static-content:deploy`.

Running `magento setup:static-content:deploy` causes the Redis error:

```
[Exception]
Notice: unserialize(): Error at offset 0 of 1 bytes in
/var/www/domain.com/vendor/magento/module-config/App/Config/Type/System.php on line 214
```

The problem is caused by parallel interfering processes on the Redis connection.

To resolve, run `setup:static-content:deploy` in a single-thread mode by setting the following environment variable:

```
STATIC_CONTENT_THREADS =1
```

or, run the `setup:static-content:deploy` command followed by the `-j 1` (or `--jobs=1` ) argument.

Note that disabling the multithreading slows down the process of deploying static assets.

## Affected versions

* Adobe Commerce on-premises: 2.1.2 and later
* Adobe Commerce on cloud infrastructure 2.1.2 and later
* Redis, any version

## Issue

Running the `setup:static-content:deploy` command causes the Redis error:

```php
)
[2017-06-02 19:57:59] Command:php ./bin/magento setup:static-content:deploy --jobs=3  en_US

[Exception]

Notice: unserialize(): Error at offset 0 of 1 bytes in /app/<domain>/vendor/magento/module-config/App/Config/Type/System.php
on line 214

.....

[CredisException]
read error on connection

[RedisException]
read error on connection

.....

[Exception]

Notice: unserialize(): Error at offset 0 of 1 bytes in /app/<domain>/vendor/magento/module-config/App/Config/Type/System.php
on line 214

.....

[RuntimeException]
Command php ./bin/magento setup:static-content:deploy --jobs=3  en_US  returned code 3
```

## Cause

The issue is caused by parallel interfering processes on the Redis connection.

Here, a process in `App/Config/Type/System.php` was expecting a response for `system_defaultweb`, but received a response for `system_cache_exists` that was made by a different process. See the detailed explanation in [Jason Woods' post](https://github.com/magento/magento2/issues/9287#issuecomment-302362283).

## Solution

Disable parallelism and run `setup:static-content:deploy` in a single-thread mode by setting the following environment variable:

```
STATIC_CONTENT_THREADS =1
```

Also you may run the `setup:static-content:deploy` command followed by the `-j 1` (or `--jobs=1`) argument.

>[!NOTE]
>
>In the single-thread mode, the static content deployment process may take four times longer.

## More information

In our developer documentation:

* [Configure Redis](https://experienceleague.adobe.com/docs/commerce-operations/configuration-guide/cache/redis/config-redis.html)
* [Command-line upgrade](https://experienceleague.adobe.com/docs/commerce-operations/upgrade-guide/implementation/perform-upgrade.html)
