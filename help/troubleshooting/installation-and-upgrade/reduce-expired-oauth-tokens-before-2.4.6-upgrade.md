---
title: "Reduce expired `oauth_tokens` before 2.4.6 upgrade"
description: This article provides a solution to the issue where you see a large amount of `oauth_tokens` in your `oauth_token` table which can cause a long delay in upgrading to version 2.4.6. It's recommended to reduce the `oauth_token` table using CleanExpiredTokens.php.
feature: Variables, Upgrade
role: Developer
---

# "Reduce expired `oauth_tokens` before 2.4.6 upgrade"

This article provides a solution to the issue where you see a large amount of `oauth_tokens` in your `oauth_token` table which can cause a long delay in upgrading to version 2.4.6. It's recommended to reduce the `oauth_token` table using the [`CleanExpiredTokens.php`](https://github.com/magento/magento2/blob/2.4.5-p2/app/code/Magento/Integration/Cron/CleanExpiredTokens.php) [!DNL cron] job to delete the expired tokens.

## Affected products and versions

* Adobe Commerce 2.4.0 - 2.4.6, all deployment methods

## Issue

If there are a large amount of `oauth_tokens` in your `oauth_token` table, that can cause a long delay in upgrading to version 2.4.6.

The upgrade process includes encrypting those tokens for an extra layer of security, and it's only done 100 records at a time. This could take several hours if there is a large number of tokens.

Reducing a large amount of `oauth_tokens` in your `oauth_token` table can prevent a long delay in upgrading to version 2.4.6.

## Solution

Before starting an upgrade, first ensure that the [`CleanExpiredTokens.php`](https://github.com/magento/magento2/blob/2.4.5-p2/app/code/Magento/Integration/Cron/CleanExpiredTokens.php) [!DNL cron] job is running. It reduces the size of the `oauth_token` table by deleting the expired `oauth_tokens` tokens, and should already be enabled by default. 

To manually trigger the [`CleanExpiredTokens.php`](https://github.com/magento/magento2/blob/2.4.5-p2/app/code/Magento/Integration/Cron/CleanExpiredTokens.php) [!DNL cron] job, run:
```bin/magento cron:run --group default```

## Related reading

* [Services > [!DNL OAuth]](https://experienceleague.adobe.com/docs/commerce-admin/config/services/oauth.html) in the Commerce Configuration Reference guide. 
* [Authentication Guide](https://developer.adobe.com/developer-console/docs/guides/authentication/) on the Adobe Developer guide.
