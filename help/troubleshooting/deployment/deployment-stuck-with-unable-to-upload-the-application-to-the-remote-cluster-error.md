---
title: Deployment stuck with "Unable to upload the application to the remote cluster" error
description: 'This article provides a solution for the Adobe Commerce issue, where deployment gets stuck, and the following error message can be found in the deploy log: *"Error: Unable to upload the application to the remote cluster"*.'
exl-id: 30f0ec31-db27-429c-b065-cf7770a72194
---
# Deployment stuck with "Unable to upload the application to the remote cluster" error

This article provides a solution for the Adobe Commerce issue, where deployment gets stuck, and the following error message can be found in the deploy log: *"Error: Unable to upload the application to the remote cluster"*.

## Affected products and versions

* Adobe Commerce on cloud infrastructure, all versions

## Issue

<u>Steps to reproduce</u>:

Trigger deployment manually or by performing a merge, push, or synchronization of your environment.

<u>Expected result</u>:

Deployment is completed successfully.

<u>Actual result</u>:

Deployment gets stuck, and in the deployment error log in cloud UI, the following error message is displayed: *"Error: Unable to upload the application to the remote cluster" found in deploy log after failed deployment, site may display error "503 first byte timeout"*.

## Cause

The problem is caused by the outage of available storage.

## Solution

You can consider cleaning the log directories and/or increasing disk space.

Directories that be considered for clean up:

* `var/log`
* `var/report`
* `var/debug/`
* `var`

For details on how to increase disk space if you are on the Adobe Commerce on cloud infrastructure Starter plan architecture, see [Increase disk space for Integration environment on cloud](https://support.magento.com/hc/en-us/articles/360005189554-Increase-disk-space-for-Integration-environment-on-Cloud) in our support knowledge base. The same instructions can be used for increasing the space of the Adobe Commerce on cloud infrastructure Pro plan architecture Integration environment. For Pro Production/Staging, you need to [file a ticket to Adobe Commerce Support](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket-Submit-a-support-ticket) and request increased disk space. But typically, you will not have to deal with this on the Staging/Production of the Pro plan as Adobe Commerce monitors these parameters for you and alerts and/or takes actions according to the contract.
