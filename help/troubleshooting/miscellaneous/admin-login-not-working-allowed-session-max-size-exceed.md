---
title: '[!UICONTROL Admin] login not working - allowed session max size exceeded'
description: Solve the issue when you try to log in to your [!UICONTROL Admin] panel and the form refreshes and you're unable to log in.
exl-id: 12789df0-6130-4e60-a92a-68ed329bd7fd
---
# [!UICONTROL Admin] login not working - allowed session max size exceeded

This article provides a fix for when you try to log in to your [!UICONTROL Admin] panel, but the form just refreshes and you're unable to log in, or you're performing some actions in the [!UICONTROL Admin] panel and get logged out automatically.
This is caused by the [!UICONTROL Admin] [!UICONTROL Session Size] has been exceeded.

## Affected versions

* Adobe Commerce on-premises, [all supported versions](https://www.adobe.com/content/dam/cc/en/legal/terms/enterprise/pdfs/Adobe-Commerce-Software-Lifecycle-Policy.pdf)
* Adobe Commerce on cloud infrastructure, [all supported versions](https://www.adobe.com/content/dam/cc/en/legal/terms/enterprise/pdfs/Adobe-Commerce-Software-Lifecycle-Policy.pdf)

## Issue

You experience one of the following symptoms on the [!UICONTROL Admin]:

1. It's impossible to log in to the [!UICONTROL Admin], because the form keeps reloading.
1. You're getting logged out automatically when attempting to perform an action.

## Cause

The allowed session max size is exceeded.

## Solution

Check the `var/log/support_report.log` file for errors such as these:

*[2023-07-13T04:26:09.792060+00:00] report.WARNING: Session size of 260572 exceeded allowed session max size of 256000. [] []
[2023-07-13T04:26:17.056714+00:00] report.WARNING: Session size of 260570 exceeded allowed session max size of 256000. [] []*

If you see these errors, the solution would be:

<u>Adobe Commerce on-premises</u>:
1. Increase the **[!UICONTROL Max Session Size in Admin]** value from the backend configuration. To do so go to **[!UICONTROL Stores]** > **[!UICONTROL Settings]** > **[!UICONTROL Configuration]** > **[!UICONTROL Advanced]** > **[!UICONTROL System]** > **[!UICONTROL Security]** > **[!UICONTROL Max Session Size in Admin]**.
1. Set the value to *500000* or higher. Depending on the existing max size reported in the error - you also could set the value to *0* which will remove  the session size limit.

<u>Adobe Commerce on cloud infrastructure</u>:

(This setting is only accessible in the [!UICONTROL Admin] when the deployment/operation mode is *default* or *developer*. However, only the Production deployment mode is allowed in the cloud environment.)

To increase this value, run this command in the terminal (SSH):

```ssh
bin/magento config:set system/security/max_session_size_admin 500000
```

You can set to higher than *500000* depending on the existing max size reported in the error and you can also set the value to *0* to remove the session size limit.

## Related Reading

* [Session size](https://experienceleague.adobe.com/en/docs/commerce-admin/systems/security/security-session-management#admin-sessions) in Admin Systems Guide
* [Operation mode](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/cli/set-mode) in the Configuration Guide
* [Secure connections](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/secure-connections) in the Commerce on Cloud Infrastructure Guide
