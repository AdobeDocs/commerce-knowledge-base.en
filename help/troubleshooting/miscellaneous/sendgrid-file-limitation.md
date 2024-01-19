---
title: "[!DNL SendGrid] file limitation on Adobe Commerce Cloud"
description: This article provides a workaround to the  [!DNL SendGrid] limitation in Adobe Commerce on cloud infrastructure.
feature: Deploy, Email
role: Developer, Admin
---
# [!DNL SendGrid limitation] on Adobe Commerce Cloud

This article provides some workarounds to the [!DNL SendGrid limitation] on Adobe Commerce Cloud.

## Affected products and versions

<!---
 1. Does this impact all support versions of Adobe Commerce on cloud infrastructure?
 2. Is SendGrid installed by default?-->

* Adobe Commerce on cloud infrastructure, all supported versions

## Issue

You attempt to send large attachments in emails and see these log errors:

<!--what are the numbers starting with "i-" are they i-nodes and should they be removed? Should any other information in these error messages be considered sensitive and removed? -->

In `/var/log/mail.log`

```shell
Month Date Time i-<id> postfix/sendmail[21408]: fatal: no-reply@leviat.com(8080): message file too big
Month Date Time i-<id> postfix/sendmail[26434]: fatal: no-reply@leviat.com(8080): message file too big
```

In `in /var/log/exception.log`

<!---
1) Is the number after /app/ a project ID?  
2) Is it is ok to shorten the error message -->

```shell
  [Year Date Time] report.ERROR: Laminas\Mail\Transport\Exception\RuntimeException: Unable to send mail: Unknown error in /app/<id>_stg2/vendor/laminas/laminas-mail/src/Transport/Sendmail.php:313
```

## Cause

This is a limitation of [!DNL SendGrid]. [!DNL SendGrid] has a system limitation of 30Mb size for email. It is recommended that you do not use attachments that exceeds 10Mb. See [Sending Attachments](https://docs.sendgrid.com/ui/sending-email/attachments-with-digioh) in Sendgrid documentation.

## Workaround

* Do not use attachments higher that 6Mb or 10Mb.
* Consider the use of a remote SMTP server on your Adobe Commerce instance. For steps, refer to [Configure email communications](https://experienceleague.adobe.com/docs/commerce-admin/systems/communications/email-communications.html) in our Admin Systems Guide.
* Reconfigure your server so that within your module files can be saved, and then attach the link to the files in the emails.

<!---is this recomended by company policy - using third party customerization that may not be tested?-->
* Search for 3rd-party customization in our Marketplace Store https://commercemarketplace.adobe.com, that enables emails to be sent via remote services.

## Related reading

* [[!DNL SendGrid] email service](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/project/sendgrid.html) in our Commerce on Cloud Infrastructure Guide.
