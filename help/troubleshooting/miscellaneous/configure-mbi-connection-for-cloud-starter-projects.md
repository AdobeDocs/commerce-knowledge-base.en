---
title: Configuring MBI Connection for existing cloud starter projects
description: This article provides a solution for when you want to configure MBI Connection for existing cloud starter projects.
feature: Observability
role: Developer
---
# Configuring MBI Connection for existing cloud starter projects

This article provides a solution for when you want to configure MBI Connection for existing cloud starter projects.

## Affected products and versions

Adobe Commerce on cloud starter (all versions)

## Issue

You want to configure MBI connection for existing cloud starter projects.

>[!NOTE]
>
>Adobe no longer supports new Cloud Starter subscriptions, but if you have an existing Starter project, you will need to follow the steps given below to configure your connection.

## Solution

To activate Magento BI for Cloud Starter projects, create a Magento BI account, create an SSH key, and finally connect to your Adobe Commerce database. 

Follow these steps:

1. Create your Magento BI Account:

    * Log into the account.
    * Go to **[!UICONTROL My Account]** > **[!UICONTROL My MBI Instances].
    * Click the **[!UICONTROL Create Instance]**. If you do not see this button, contact your Customer Success Manager or Customer Technical Advisor.
    * Select your Cloud Starter subscription. If you only have a Cloud Starter subscription, this will automatically be selected.
    * Click **[!UICONTROL Continue]**.
    * Input your information to create your account.

    ![Create MBI account](/help/troubleshooting/miscellaneous/assets/create_mbi_account.png)

    * Go to your inbox and verify the email address.

    ![Verify email address](/help/troubleshooting/miscellaneous/assets/verify_email_address_mbi.png)

    * Create a password.
    
    ![Create a password](/help/troubleshooting/miscellaneous/assets/create_password_mbi.png)

    * After creating your account, you will have the option to add users to your new account. Technical admins can now be added to carry out the following steps.

    ![Add users](/help/troubleshooting/miscellaneous/assets/add_users_mbi.png)

1. Input information about your store to set your preferences.

    ![Add store information](/help/troubleshooting/miscellaneous/assets/add_store_info_mbi.png)

    There is some information you will need to gather before you can connect your database for the third step in the onboarding flow. You will be filling in the Connect your database page in step 9.

1. Create a dedicated MBI user.






