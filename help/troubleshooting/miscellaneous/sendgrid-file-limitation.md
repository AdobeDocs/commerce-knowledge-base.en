---
title: "[!DNL SendGrid] file limitation for Adobe Commerce Cloud"
description: This article provides a workaround to the  [!DNL SendGrid] limitation in Adobe Commerce on cloud infrastructure.
feature: Deploy, Marketing Tools
role: Developer, Admin
---
# [!DNL SendGrid limitation] for Adobe Commerce Cloud

This article provides some workarounds to the [!DNL SendGrid limitation] on Adobe Commerce on Cloud infrastructure.

## Affected products and versions

*  Adobe Commerce on cloud infrastructure, [all supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf)


## Issue

You attempt to send large attachments in emails and see these log errors:

In `/var/log/mail.log`

```shell
Month Date Time i-xxxxxxxxxxxxxxxxx postfix/sendmail[21408]: fatal: no-reply@leviat.com(8080): message file too big
Month Date Time i-xxxxxxxxxxxxxxxxx postfix/sendmail[26434]: fatal: no-reply@leviat.com(8080): message file too big
```

In `/var/log/exception.log`

Production: 

`/app/<project-id>/vendor/laminas/laminas-mail/src/Transport/Sendmail.php:313`

Staging:

`/app/<project-id_stg>/vendor/laminas/laminas-mail/src/Transport/Sendmail.php:313`

Staging2:

`/app/<project-id_stg2>/vendor/laminas/laminas-mail/src/Transport/Sendmail.php:313`

## Cause

[!DNL SendGrid] has a system limitation of 30Mb size for email. It is recommended that you do not use attachments that exceeds 10Mb. See [Sending Attachments](https://docs.sendgrid.com/ui/sending-email/attachments-with-digioh) in SendGrid documentation for more infomation.

## Workaround

* Do not use attachments higher than 6Mb or 10Mb.
* Consider the use of a remote SMTP server on your Adobe Commerce instance. For steps, refer to [Configure email communications](https://experienceleague.adobe.com/docs/commerce-admin/systems/communications/email-communications.html) in our Admin Systems Guide.
* Reconfigure your server so that files can be saved within your module, and then attach the link to the files in the emails.

## Related reading

* [[!DNL SendGrid] email service](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/project/sendgrid.html) in our Commerce on Cloud Infrastructure Guide.
