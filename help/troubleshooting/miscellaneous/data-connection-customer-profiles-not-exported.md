---
title: Customer profiles not appearing in Experience Platform
description: This article provides troubleshooting steps if your customer profile data is not appearing in the Experience Platform when using the Data Connection extension.
feature: Personalization, Integration, Configuration
role: Admin, Developer
---
# Customer profiles not appearing in Experience Platform

This article provides troubleshooting steps if your customer profile data is not appearing in the Experience Platform when using the Data Connection extension.

## Affected products and versions

* Adobe Commerce 2.4.x with Data Connection extension installed

## Issue

You have installed and configured the [Data Connection](https://experienceleague.adobe.com/en/docs/commerce-merchant-services/data-connection/overview) extension and have enabled customer profile data to be sent to the Experience Platform, but that profile data is not appearing in the Experience Platform.

## Solution

If customer profile information is not appearing in the Experience Platform, check the following:

### Confirm that the latest version of Data Connection is installed

Ensure you have installed the latest version of the `experience-platform-connector` extension.

See the [[!DNL Data Connection] extension release notes](https://experienceleague.adobe.com/en/docs/commerce-merchant-services/data-connection/release-notes) for information about the latest version. 

>[!NOTE]
>
>The latest version of the [!DNL Data Connection] extension includes the `customers-connector` module, which is responsible for sending profile data to the Experience Platform. The `customers-connector` module should be version `1.2.0` or higher.

### Confirm the customers-connector module is configured

Confirm the `customers-connector` module is configured based on your installation scenario.

#### Adobe Commerce on Cloud infrastructure

1. Enable the `ENABLE_EVENTING` global variable in `.magento.env.yaml`. [Learn more](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/configure/env/stage/variables-global).

    ```bash
        stage:
            global:
                ENABLE_EVENTING: true
    ```

1. Commit and push updated files to the Cloud environment. When deployment is finished, enable sending events with the following command:

    ```bash
        bin/magento config:set adobe_io_events/eventing/enabled 1
    ```

#### Adobe Commerce on-premise installation

Execute the following commands in order to enable code generation and Adobe Commerce Events:

```bash
   bin/magento events:generate:module
   bin/magento module:enable Magento_AdobeCommerceEvents
   bin/magento setup:upgrade
   bin/magento setup:di:compile
   bin/magento config:set adobe_io_events/eventing/enabled 1
```

### Confirm you enabled profile data to be captured and sent to Experience Platform

In the Commerce Admin, make sure that the following fields are set:

In **System** -> *Services* -> **Data Connection**, verify that the Back office events and Customer profiles checkboxes are enabled. Ensure
that the **Profile Dataset ID** field is correct and is a different dataset than what you are currently using for behavioral and back office event data.

### Check if events are routing to staging or production

1. Run the following command to show the current Adobe Developer environment:

    ```bash
    Copy code
    bin/magento config:show
    adobe_io_events/integration/adobe_io_environment
    ```

1. If the environment is set to "stage", change it to "production" with the following
command:

    ```bash
    Copy code
    bin/magento config:set adobe_io_events/integration/adobe_io_environment
    production
    ```

### Query Event Data SaaS table

Connect and execute the following SQL query to verify customer profile records appear in the
`event_data_saas` table and that there are no errors:

```sql
Copy code
select * from event_data_saas;
```

### Handle event publishing errors

1. If you encounter the following error, ensure that the sandbox and production SaaS connector keys are correct:

    ```css
    Copy code
    2024-06-07 14:37:57 | 2024-06-07 14:38:03 | 1 | 0 | Event publishing
    failed: Error code: 403; reason: Forbidden { "error": { "code":
    "Forbidden", "message": "Client ID is invalid", "details": {
    "error_code": "403003" } } }
    ```

1. Go to the Commerce Services Connector page in the Admin and ensure that the sandbox/production keys specified are correctly configured. Also confirm that the Commerce account sandbox/production settings match those shown in the Commerce Services Connector. Learn [more](https://experienceleague.adobe.com/en/docs/commerce-merchant-services/user-guides/integration-services/saas#apikey).

### Check if the Service ID is in the allowlist and confirm with Adobe Commerce support

1. Verify that the Commerce Services Connector `serviceId` appears in allowlist in Adobe Commerce.
1. Contact [Adobe Commerce support](https://support.magento.com/hc/en-us) to confirm the allowlist status.

## Related reading

See the [Data Connection](https://experienceleague.adobe.com/en/docs/commerce-merchant-services/data-connection/overview) extension in the user guide.
