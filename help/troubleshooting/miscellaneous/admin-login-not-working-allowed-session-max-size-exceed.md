---
title: '[!DNL Admin] login not working - allowed session max size exceeded'
description: This article provides a fix for when you try to log in to your Admin panel and the form refreshes and you are unable to log in.
---

# [!DNL Admin] login not working - allowed session max size exceeded

This article provides a fix for when you try to log in to your Commerce Admin panel but the form just refreshes and you are unable to log in. This is because the Admin Session Size has been exceeded.


## Affected versions


* Adobe Commerce on-premises, [all supported versions](https://www.adobe.com/content/dam/cc/en/legal/terms/enterprise/pdfs/Adobe-Commerce-Software-Lifecycle-Policy.pdf)
* Adobe Commerce on cloud infrastructure, [all supported versions](https://www.adobe.com/content/dam/cc/en/legal/terms/enterprise/pdfs/Adobe-Commerce-Software-Lifecycle-Policy.pdf)

## Issue 

The Commerce admin login is not working as the allowed session max size is exceeded.


## Solution 


Check the `var/log/support_report.log` file for errors such as these:

*[2023-07-13T04:26:09.792060+00:00] report.WARNING: Session size of 260572 exceeded allowed session max size of 256000. [] []
[2023-07-13T04:26:17.056714+00:00] report.WARNING: Session size of 260570 exceeded allowed session max size of 256000. [] []*

If you see these errors, the solution would be:

<u>Adobe Commerce on-premises</u>:
1. In order to fix the issue, you need to increase the **[!UICONTROL Max Session Size in Admin]** value from the backend configuration.
1. Go to **[!UICONTROL Stores] > **[!UICONTROL Configuration]** > **[!UICONTROL Advanced]** > **[!UICONTROL System]** > **[!UICONTROL Security]** > **[!UICONTROL Max Session Size in Admin]**
1. Set the value to *500000* or higher (depending on the existing max size reported in the error - you also could set the value to 0 which will remove  the       session size limit)

<u>Adobe Commerce on cloud infrastructure</u>:
(This setting is only accessible in the admin when the deployment/operation mode is Default or Development. However, only the Production deployment mode is allowed in the Cloud environment.)

To increase this value, run this command in the terminal (SSH):

```ssh
bin/magento config:set system/security/max_session_size_admin 500000 or higher (depends on the existing max size reported in the error - you also could set the value to 0 which will remove the session size limit))
```

## Related Reading

[Session size](/docs/commerce-admin/systems/security/security-session-management.html?lang=en#admin-sessions)
[Operation mode](/docs/commerce-operations/configuration-guide/cli/set-mode.html)
[Secure connections](/docs/commerce-cloud-service/user-guide/develop/secure-connections.html)
