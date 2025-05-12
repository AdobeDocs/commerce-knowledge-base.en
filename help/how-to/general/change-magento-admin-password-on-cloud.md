---
title: Change Admin password on Adobe Commerce on cloud infrastructure
description: '![login_panel_s.png](assets/login_panel_s.png)'
exl-id: 1b6e867e-d314-4e7b-be95-d699e6749896
feature: Admin Workspace, Cloud
---
# Change Admin password on Adobe Commerce on cloud infrastructure

## Method 1: Forgot Your Password (reset via email)

![login_panel_s.png](assets/login_panel_s.png)

Read the steps in the [Reset your password section of Admin Sign In](https://experienceleague.adobe.com/docs/commerce-admin/start/admin/admin-signin.html#admin-sign-in) in our user guide.

Below are the critical usage notes.

### Enable outgoing emails

Before using the **Forgot your password** form, ensure that you [enable outgoing emails](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/project/outgoing-emails.html) using the [Cloud Console](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/project/overview.html). This applies only to integration environments and sandbox projects. If outgoing emails are truly disabled on Pro Production or Staging - meaning that the email wasn't picked up by SendGrid - you can verify this by checking [Enable emails in the Cloud Console](https://experienceleague.adobe.com/en/docs/commerce-on-cloud/user-guide/project/outgoing-emails#enable-emails-in-the-cli). If the issue persists, you can submit an [Adobe Commerce Support ticket](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide).

### Check your Junk Email folder

If you cannot find the message with a Reset Password link, check your *Junk Email* folder. The name of the email is *Password Reset Confirmation for Admin Username*.

## Method 2: Add a New Admin User

If you cannot restore or reset the password for the existing user, you can create a new Admin user and set a password for this user. To do so, take the following steps:

1. Use [SSH to log in to the remote environment](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/secure-connections.html).
1. Run the following command: `bin/magento admin:user:create   --admin-user=%user_name% --admin-password=%your_password% --admin-email=%your_email% --admin-firstname=%admin_user_first_name% --admin-lastname=%admin_user_last_name%`
