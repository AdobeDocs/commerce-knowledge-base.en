---
title: .magento.env.yaml changes not shown in env.php after deploy
description: This article provides a solution for the issue where changes in .magento.env.yaml file are not reflected in app/etc/env.php after deployment.
exl-id: 39ea7295-ba5a-40cc-bc68-a5e0b965c1a7
feature: Deploy
role: Developer
---
# .magento.env.yaml changes not shown in env.php after deploy

>[!NOTE]
>
>If you have this problem upgrade to ece-tools 2002.1.5 to fix it. 2002.1.5 has functionality to reset the opcache on each deployment so there is never a need to change the setting `opcache.enable_cli=1`. If you don't want to upgrade, then you would have to do the workaround steps as described below in the solution.

This article provides a solution for the issue where changes in `.magento.env.yaml` file are not reflected in `app/etc/env.php` after deployment.

## Affected products and versions

* Adobe Commerce on cloud infrastructure (all [supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf)).

## Issue

Changes made in the `.magento.env.yaml` file do not affect the `app/etc/env.php` generated.

<u>Steps to reproduce:</u>

Change any value in `.magento.env.yaml` and push to the server, where it should define the configuration (and deployment settings) for the currently checked-out environment. For steps, see [Environment Variables > Deploy Variables](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/configure/env/stage/variables-deploy) in our developer documentation.

<u>Expected result:</u>

Changes made in the `.magento.env.yaml` file affect the `app/etc/env.php` generated.

<u>Actual result:</u>

The changes have no effect on the `app/etc/env.php` variables after deployment.

## Cause

The issue could be caused by the incorrect value of the `opcache.enable_cli` parameter in the `php.ini` file.

## Solution

1. Check that the system is configured according to [Adobe Commerce Performance Best Practices > Software recommendations](https://experienceleague.adobe.com/en/docs/commerce-operations/performance-best-practices/software).
1. Check if `opcache.enable_cli` directive in `php.ini` is set to `0` by executing: `php -i | grep opcache.enable_cli`
1. If the output looks like `opcache.enable_cli=1` , edit the `php.ini` file in the project root directory and change `opcache.enable_cli=1` to `opcache.enable_cli=0`
1. Redeploy the project.

## Related reading

* [Cloud for Adobe Commerce > Build and deploy](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/configure/env/configure-env-yaml).
