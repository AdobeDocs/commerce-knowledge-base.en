---
title: Configuring Adobe Commerce Intelligence connection for existing Cloud Starter projects
description: This article provides a solution for when you want to configure Adobe Commerce Intelligence connection for an existing Cloud Starter project.
feature: Commerce Intelligence
role: Developer
---
# Configuring Adobe Commerce Intelligence connection for existing Cloud Starter projects

>[!NOTE]
>
>Adobe Commerce Intelligence was previously known as Magento Business Intelligence (MBI).

This article provides a solution for when you want to configure Adobe Commerce Intelligence connection for an existing Cloud Starter project.

## Affected products and versions

Adobe Commerce on cloud starter (all versions)

## Issue

You want to configure Commerce Intelligence connection for an existing Cloud Starter project.

>[!NOTE]
>
>Adobe no longer supports new Cloud Starter subscriptions, but if you have an existing Starter project, you will need to follow the steps given below to configure your connection.

## Solution

To activate Commerce Intelligence for Cloud Starter projects, create a Commerce Intelligence account, create an SSH key, and finally connect to your Adobe Commerce database. 

Follow these steps:

1. Create your Adobe Commerce Intelligence Account:

    * Go to [accounts.magento.com/customer/account/login](https://account.magento.com/customer/account/login).
    * Navigate to **[!UICONTROL My Account]** > **[!UICONTROL My MBI Instances]**.
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

1. Create a dedicated Commerce Intelligence user.

    * Create a new user on [account.adobe.com](https://account.adobe.com/).
    * Why a new user? Adobe Commerce Intelligence needs a user added to the project to continuously fetch new data to be transferred to the account's Commerce Intelligence data warehouse. This user will serve as that connection. Adding this user to the project will come in Step 4.
    * The reason for having a dedicated Commerce Intelligence user is to prevent the added user from inadvertently being deactivated or deleted and stopping the Commerce Intelligence connection.

1. Add the newly created user to the project's primary environment as a *Contributor*.

    ![Add user as a Contributor](/help/troubleshooting/miscellaneous/assets/contributor_user_mbi.png)

1. Get your Commerce Intelligence SSH keys.

    * Go to the **[!UICONTROL Connect your database]** page of the Commerce Intelligence set up user interface and scroll down to **[!UICONTROL Encryption settings]**.
    * For the field, **[!UICONTROL Encryption Type]**, choose **[!UICONTROL SSH Tunnel]**.
    * From the dropdown, you can copy and paste the provided Magento BI Essentials Public Key.

    ![Encryption settings](/help/troubleshooting/miscellaneous/assets/encryption_type_mbi.png)

1. Add your new Magento BI Essentials Public key to the Commerce Intelligence user created in Step 5.

    * Go to [accounts.magento.com/customer/account/login](https://account.magento.com/customer/account/login). Sign in with your account login information for the new Commerce Intelligence user created. Then go to the **[!UICONTROL Account Settings]** tab.
    * Scroll down the page and expand the drop-down for SSH keys. Then click **[!UICONTROL Add a public key]**.

    ![Add a public key](/help/troubleshooting/miscellaneous/assets/add_public_key_mbi.png)

    * Add the Magento MBI Essentials SSH Public Key from above.

    ![Add SSH Public Key](/help/troubleshooting/miscellaneous/assets/add_ssh_key_mbi.png)

1. Provide Business Intelligence Essentials MySQL credentials.

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

    * Update your `.magento.app.yaml`.

    ```
    relationships:
             database: "mysql:mysql"
             mbi: "mysql:mbi"
             redis: "redis:redis"
    ```

1. Get information for connecting your database to Commerce Intelligence.

    Run `echo $MAGENTO_CLOUD_RELATIONSHIPS | base64 --decode | json_pp` to get information on connecting your database.

    You should receive information similar to the output below:

    ```
    "mbi" : [
               {
                  "scheme" : "mysql",
                  "rel" : "mbi",
                  "cluster" : "vfbfui4vmfez6-master-7rqtwti",
                  "query" : {
                     "is_master" : true
                  },
                  "ip" : "169.254.169.143",
                  "path" : "main",
                  "host" : "mbi.internal",
                  "hostname" : "3m7xizydbomhnulyglx2ku4wpq.mysql.service._.magentosite.cloud",
                  "username" : "mbi",
                  "service" : "mysql",
                  "port" : 3306,
                  "password" : "[password]"
               }
            ],
    ```

1. Connect your Adobe Commerce Database.

    ![Connect your Adobe Commerce Database](/help/troubleshooting/miscellaneous/assets/connect_magento_database_mbi.png)

    *Inputs*:

    * Integration Name: [Choose a name for your integration.]
    * Host: `mbi.internal`
    * Port: 3306
    * Username: mbi
    * Password: [input password provided in Step 8's output.]
    * Database Name: main
    * Table Prefixes: [leave blank if there are no table prefixes]

1. Set your Timezone Settings.

    ![Timezone settings](/help/troubleshooting/miscellaneous/assets/timezone_settings_mbi.png)

    *Inputs*

    * Database: Timezone: UTC
    * Desired Timezone: [Choose the time zone you want your data to display in.]

1. Get information for your encryption settings.

    * The project UI provides an SSH access string. This string can be used for gathering the information needed for the Remote Address and Username in setting up your **[!UICONTROL Encryption settings]. Use the SSH Access string found by clicking the access site button on your Master branch of your Project UI and find your [!UICONTROL User Name] and [!UICONTROL Remote Address] as shown below.

    ![Access site master](/help/troubleshooting/miscellaneous/assets/access_site_mbi.png)

    ![User name and remote address](/help/troubleshooting/miscellaneous/assets/user_name_address_mbi.png)

1. Input information for your Encryption Settings.

    ![Encryption settings](/help/troubleshooting/miscellaneous/assets/encryption_type_mbi.png)

    *Inputs*

    * Encryption Type: SSH Tunnel
    * Remote Address: ssh.us-3.magento.cloud
    * Username: vfbfui4vmfez6-master-7rqtwti--mymagento
    * Port: 22

1. Click Save Integration.
1. You have now successfully connected to your Commerce Intelligence Essentials account.
1. If you are an Adobe Commerce Intelligence Pro customer, contact your Customer Success Manager or Customer Technical Advisor to coordinate the next steps.
