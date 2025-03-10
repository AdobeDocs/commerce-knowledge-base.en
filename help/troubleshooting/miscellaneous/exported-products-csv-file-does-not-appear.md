---
title: Exported products .csv file does not appear
description: This article provides a fix for the issue where you try to export the desired entity type to a .csv file in the Commerce Admin, but the file does not appear.
exl-id: 8e3bb65c-ea75-4af4-ad4b-4d94ab219bbb
feature: Cache, Data Import/Export, Products, Variables
role: Developer
---
# Exported products .csv file does not appear

This article provides a solution for the issue where exporting the desired entity type to a .csv file in the Commerce Admin results in the file not appearing.

## Affected products and versions

* Adobe Commerce on cloud infrastructure, all [supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf).

## Issue

 <u>Steps to reproduce</u>

Prerequisites: The **Add Secret Key to URLs** option is set to *Yes*. The option is configured in the Commerce Admin under **Stores** > **Configuration** > **Advanced** > **Admin** > **Security**.

1. In the Admin, navigate to **System** > **Data Transfer** > **Export**.

    ![magento_export_products_2.3.4.png](assets/magento_export_products_2.3.4.png)

1. Select
    * **Entity Type**: The entity you wish to export
    * **Export File Format**: *CSV*
    * **Field Enclosure**: leave unchecked.
1. Click **Continue**.
1. The following message is displayed: *"Message is added to queue, wait to get your file soon"*.

 <u>Expected result</u>

The .csv file containing the exported desired entity type is displayed in the grid within a couple of minutes.

 <u>Actual result</u>

The .csv file containing the exported desired entity type is not displayed in the grid in 10 minutes or more.

## Cause

A known issue with the Export functionality in the Adobe Commerce application part version 2.3.2.

## Solution

There are two possible solutions for the issue:

* Disable the Add Secret Key to URL option.
* Run the `bin/magento queue:consumers:start exportProcessor` command manually, and optionally configure it to be run by cron.

See details for both options in the following paragraphs.

### Disable the Add Secret Key to URL option

1. In the Admin, navigate to **Stores** > **Configuration** > **Advanced** > **Admin** > **Security**.
1. Set the **Add Secret Key to URLs** option to *No.*
1. Click **Save Config**.
1. Clean cache under **System** > **Tools** > **Cache Management** or by running    ```bash    bin/magento cache:clean``` or in the Admin.

### Run the export command manually and optionally add it as cron job

To get the export file, run the `bin/magento queue:consumers:start exportProcessor` command. After running this, the file should be displayed in the grid.


To add the process as a cron job optionally, you must add the `CRON_CONSUMERS` variable to the `.magento.env.yaml` file.

#### Add process as a cron job (optional)

1. Make sure your cron is setup and configured. See [Set up cron jobs](/docs/commerce-cloud-service/user-guide/configure/app/properties/crons-property.html) for details.
1. Run the following command to return a list of message queue consumers:     `./bin/magento queue:consumers:list`
1. Add the following to your `.magento.env.yaml` file in the root application directory and include the consumers you would like to add. For example, here is the consumer required for export processing:

   ```yaml
   stage:
       deploy:
           CRON_CONSUMERS_RUNNER:
               cron_run: true
               max_messages: 1000
               consumers:
                   - exportProcessor
   ```

   Then push this updated file and redeploy your environment. Also reference [Add custom cron jobs to your project](/docs/commerce-cloud-service/user-guide/configure/app/properties/crons-property.html#add-custom-cron-jobs-to-your-project) in our developer documentation.

>[!NOTE]
>
>If you cannot find the `.magento.env.yaml` file for your environment, and you think it was deleted, you need to create a new `.magento.env.yaml`. It might be empty initially, you can add info there as required. Reference the following articles: [Configure environment variables for deployment](/docs/commerce-cloud-service/user-guide/configure/env/configure-env-yaml.html) and [Environment variables](/docs/commerce-cloud-service/user-guide/configure/env/stage/variables-intro.html) in our developer documentation.

>[!TIP]
>
>[YAML files](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/configure/env/configure-env-yaml.html) are case sensitive and do not allow tabs. Be careful to use consistent indentation throughout the .magento.env.yaml file or your configuration may not work as expected. The examples in the documentation and in the sample file use two-space indentation. Use the ece-tools validate command to check your configuration.

>[!NOTE]
>
>On Adobe Commerce on cloud infrastructure Pro projects, the [auto-crons feature](/docs/commerce-cloud-service/user-guide/configure/app/properties/crons-property.html?lang=en#crontab) must be enabled on your Adobe Commerce on cloud infrastructure before you can add custom cron jobs to Staging and Production environments using `.magento.app.yaml`. If this feature is not enabled, [create a support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket), to have the job added for you.
