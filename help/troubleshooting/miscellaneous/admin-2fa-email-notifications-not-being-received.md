---
title: Admin 2FA email notifications not being received
description: This article provides troubleshooting when you aren't receiving the email with the setup completion instructions after you have set up Two-Factor Authentication (2FA) in order to enhance Admin access security in Adobe Commerce on cloud infrastructure.
exl-id: 7ab6b2b4-6aca-4323-a45b-2b4e52955160
feature: Admin Workspace, Communications
role: Developer
---
# Admin 2FA email notifications not being received


## Affected products and versions

* Adobe Commerce on cloud infrastructure, all versions

## Issue

You have set up Two-Factor Authentication in order to enhance Admin access security, but aren't receiving the email with the instructions on completing the setup.

## Cause

If you have not configured the Sender email properly, or your domain has not been white-labeled in SendGrid, then the email would likely have ended up in the Spam folder.

## Troubleshooting

### Step 1: Check your Spam folder

1. If the email didn't appear in your Spam folder, run this Mysql query to verify the email addresses have been configured:

    ```sql
    select * from core_config_data where path like '%trans_email%';
    ```

    * If it doesn't return any results, it means that the Sender address has not been configured.
Since you you don't have access to the admin, you will have to insert the configuration into the database. Plug in the appropriate email address and run the MySQL statement:
    
    ```
    insert into core_config_data (scope,scope_id,path,value) values ('default',0,'trans_email/ident_general/email', your-email@here.com)
    ```

    * If it returns a result, proceed to **Step 2**.

1. If the email appeared in your Spam folder, click on the link in the email. If the link has since expired, try logging in again to repeat the process.
1. Once you have gained access, go to **Stores** > **Configuration** > **General** > **Store Email Addresses** and configure the email addresses.

### Step 2: If/once the email addresses have been properly configured, SSH into the environment and run this command:

```php
php -r "mail(<your email address>,<subject>,<content>,'To: <sender email>');"
```

Check your Spam folder for the email. 

If the email appeared in your Spam folder, your domain's email authentication might not be fully configured for outbound delivery via SendGrid.

If you are using the SendGrid service managed by Adobe:

[Submit a support ticket](https://experienceleague.adobe.com/home?support-tab=home#support) requesting that your sending domain be authenticated (sometimes called *white-labeled*) with SendGrid.
This process involves adding DNS records (DKIM and SPF) to authorize SendGrid to send emails on behalf of your domain, which increases the likelihood that your emails will be delivered to the inbox instead of the spam folder.

If you are using your own SendGrid account:

You are responsible for managing your domain authentication settings directly within your SendGrid account dashboard. Refer to [How to Set Up Domain Authentication](https://www.twilio.com/docs/sendgrid/ui/account-and-settings/how-to-set-up-domain-authentication) in SendGrid documentation for details.

>[!NOTE]
>
>Some customers might choose to use a separately provisioned SendGrid service for full control over email deliverability and compliance (e.g., HIPAA requirements). Ensure you are following the correct troubleshooting steps based on the type of SendGrid service (Adobe-managed vs. self-managed) you are using.


## Related reading

* [SendGrid](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/project/sendgrid) in our developer documentation.
