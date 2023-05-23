---
title: Cron stops due to misconfigured or missing OpCache settings 
description: This article provides a solution for when crons stop working due to misconfigured or missing OpCache settings Adobe Commerce.
---

# Cron stopped due to misconfigured or missing OpCache settings Adobe Commerce

This article provides a solution for when cron stops working due to missing or misconfigured OpCache settings.

## Affected products and versions

Adobe Commerce on cloud infrastructure, [all supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf).

## Issue

The cron stopped working.

## Cause

The OpCache module was updated to a newer version which introduced a GraphQL plugin that rewrites the `env.php` in runtime and could override the cron setting, which may have caused the issue. The OpCache configuration needs to be updated in order to avoid any issues with the `env.php file`, and that was solved in [version 2002.1.13](/docs/commerce-cloud-service/user-guide/release-notes/ece-tools-package.html?lang=en#v2002.1.13) of the ECE Tools package.

## Solution

Option 1: Run the following in the command-line tool:

```bash
bin/magento cron:run
```

A message might display that the cron is disabled.

Option 2: Open the `app/etc/env.php` file - if you see the below, then the cron was disabled manually, was not re-enabled due to a failed deployment, or the issue was related to the OpCache settings.

```php
  'cron' =>
  array (
    'enabled' => 0,
  ),
```

1. If the cron is disabled, run this command to re-enable the cron: `vendor/bin/ece-tools cron:enable`
1. Make sure that you are on the latest version of ECE Tools. If you are not, upgrade (or skip to item 3). To check your existing version, run this command:
`composer show magento/ece-tools`
1. If you are already on the latest version of ECE Tools, check for the presence of the `op-exclude.txt` file. To do so, run this command:
`ls op-exclude.txt`
If this file is not present, please add https://github.com/magento/magento-cloud/blob/master/op-exclude.txt to your repo then commit the change and redeploy.
1. Without having to upgrade ECE Tools, you can also just add/modify https://github.com/magento/magento-cloud/blob/master/op-exclude.txt in your repo, then commit the change and redeploy.

## Related reading

* [Cron readiness check issues](/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/cron-readiness-check-issues.html?lang=en)
* [Crons property](/docs/commerce-cloud-service/user-guide/configure/app/properties/crons-property.html)
* [Cron job is stuck in “running” status](/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/cron-job-is-stuck-in-running-status.html)
