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

    * Create a new user on accounts.magento.com.
    * Why a new user? Magento BI needs a user added to the project to continuously fetch new data to be transferred to the account's MBI data warehouse. This user will serve as that connection. Adding this user to the project will come in Step 4.
    * The reason for having a dedicated MBI user is to prevent the added user from inadvertently being deactivated or deleted and stopping the MBI connection.

1. Add the newly created user to the project's primary environment as a *Contributor*.

    ![Add user as a Contributor](/help/troubleshooting/miscellaneous/assets/contributor_user_mbi.png)

1. Get your MBI SSH keys.

    * Go to the **[!UICONTROL Connect your database]** page of the MBI set up user interface and scroll down to **[!UICONTROL Encryption settings]**.
    * For the field, **[!UICONTROL Encryption Type] choose **[!UICONTROL SSH Tunnel].
    * From the dropdown, you can copy and paste the provided Magento BI Essentials Public Key.

    ![Encryption settings](/help/troubleshooting/miscellaneous/assets/encryption_type_mbi.png)

1. Add your new Magento BI Essentials Public key to the MBI user created in Step 5.

    * Go to https://accounts.magento.cloud/. Sign in with your account log in information for the new MBI user created. Then go to the **[!UICONTROL Account Settings]** tab.
    * Scroll down the page and expand the drop down for SSH keys. Then click **[!UICONTROL Add a public key]**.

    ![Add a public key](/help/troubleshooting/miscellaneous/assets/add_public_key_mbi.png)

    * Add the Magento MBI Essentials SSH Public Key from above.

    ![Add SSH Public Key](/help/troubleshooting/miscellaneous/assets/add_ssh_key_mbi.png)

1. Provide Magento Business Intelligence Essentials MySQL credentials.

    * Update your `.magento/services.yaml`

    ```
    mysql:
     type: mysql:10.0
     disk: 2048
     configuration:
         schemas:
             - main
         endpoints:
             mysql:
                 default_schema: main
                 privileges:
                     main: admin
             mbi:
                 default_schema: main
                 privileges:
                     main: ro
    ```

1. 












