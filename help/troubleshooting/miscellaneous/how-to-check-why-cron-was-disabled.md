---
title: How to check why [!DNL cron] was disabled
description: This article offers troubleshooting solutions for issues with cron in Adobe Commerce on cloud infrastructure products.
feature: Configuration
role: Developer
---
# How to check why [!DNL cron] was disabled

This article offers troubleshooting solutions for issues with [!DNL cron] in Adobe Commerce on cloud infrastructure products.

Affected products and versions

* Adobe Commerce on cloud infrastructure, all versions

## Issue

## The following are symptoms of [!DNL cron] issues:

You have noticed that your [!DNL cron] wasn't running. 
For example: you see the following lines in the `app/etc/env.php` file:

```  'cron' =>
  array (
    'enabled' => 0
  ),
```

An empty array would mean that the [!DNL cron] is **enabled**:

```  'cron' =>
  array (
  ),
```

## Causes

There are several reasons why the [!DNL cron] isn't currently active:

1. The [!DNL cron] was disabled due to missed [!DNL OpCache] settings.
1. The Infrastructure team disabled your [!DNL cron], because it was causing your site to perform-poorly/go-down.
1. The [!DNL cron] wasn't re-enabled because your deployment failed.

See one of the following sections for a solution to your issue.

## Solutions

### Solution for missed [!DNL OpCache] settings {#solution-missed-opcache-settings}

See [[!DNL Cron] stopped due to misconfigured or missing [!DNL OpCache] settings](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/crons-blocked-running-missing-opache-settings) in our Commerce knowledge base.

### Solution for disabled by Infrastructure team {#solution-disabled-by-infrastructure-team}

1. Check your previous support tickets in which your site was down or not responding.
1. Then check whether the Infrastructure team indicated that they had disabled it.
1. Verify that you have addressed the issues/concerns brought up by the Infrastructure team.
1. Submit a [Support request](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide#support-tickets) if you need further assistance to request to re-enable the [!DNL cron] and explain how you have addressed the issues that the Infrastructure team indicated.

### Solution for deployment failed {#solution-deployment-failed}

Check the deployment logs:

* [View and manage logs](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/test/log-locations) in our Commerce on Cloud Infrastructure Guide.
* [Checking deployment log if Cloud UI has *`log snipped`* error](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/checking-deployment-log-if-the-cloud-ui-shows-log-snipped-error) in our Commerce knowledge base. 

1. If the deployment had failed during the `setup:upgrade` step, the [!DNL cron] won't have been re-enabled.
For example: you see this line in the deployment log:

    ```The command "/bin/bash -c "set -o pipefail; php ./bin/magento setup:upgrade --keep-generated --ansi --no-interaction  | tee -a /app/$<project_id>/var/log/install_upgrade.log"" failed. Cache types config flushed successfully```

1. Otherwise, the deployment might have failed during some other stage. Check the deployment log and ensure that both lines appear (example below). If you don't see both lines similar to this in the log, it means that the [!DNL cron] was not re-enabled:

    ```  [2024-03-06T10:55:39.345564+00:00] INFO: Disable cron```<br>
...<br>
    ```  [2024-02-07T10:50:09.579005+00:00] INFO: Enable cron```

**Submit a [Support request](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide#support-tickets) if you need further assistance.**
