---
title: Customer profiles not appearing in Experience Platform
description: This article provides troubleshooting steps if your customer profile data is not appearing in the Experience Platform when using the [!DNL Data Connection] extension.
feature: Personalization, Integration, Configuration
role: Admin, Developer
exl-id: 4f12b032-0bee-47da-927a-8d4c2d8b8276
---
# Customer profiles not appearing in Experience Platform

This article provides troubleshooting steps if your customer profile data is not appearing in the Experience Platform when using the Data Connection extension.

## Affected products and versions

* Adobe Commerce 2.4.x with [!DNL Data Connection] extension installed

## Issue

You have installed and configured the [[!DNL Data Connection]](https://experienceleague.adobe.com/en/docs/commerce-merchant-services/data-connection/overview) extension and have enabled customer profile data to be sent to the Experience Platform, but that profile data is not appearing in the Experience Platform.

## Solution

If customer profile information is not appearing in the Experience Platform, check the following:

### Confirm that the latest version of [!DNL Data Connection] is installed

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

#### Adobe Commerce on-premises installation

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

* In **[!UICONTROL System]** > **[!UICONTROL Services]** > **[!UICONTROL Data Connection]**, verify that the [!UICONTROL Back office events] and [!UICONTROL Customer profiles] checkboxes are enabled.
* Ensure that the *[!UICONTROL Profile Dataset ID]* field is correct and is a different dataset than what you are currently using for behavioral and back-office event data.

### Check if events are routing to staging or production

1. Run the following command to show the current Adobe Developer environment:

    ```bash
    Copy code
    bin/magento config:show
    adobe_io_events/integration/adobe_io_environment
    ```

1. If the environment is set to *[!UICONTROL Stage]*, change it to *[!UICONTROL Production]* with the following command:

    ```bash
    Copy code
    bin/magento config:set adobe_io_events/integration/adobe_io_environment
    production
    ```

### Query Event Data SaaS table

Connect and execute the following [!DNL SQL] query to verify customer profile records appear in the
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

1. Go to the *[!UICONTROL Commerce Services Connector]* page in the Admin and ensure that the [!UICONTROL sandbox/production] keys specified are correctly configured. Also, confirm that the Commerce account [!UICONTROL sandbox/production] settings match those shown in the [!UICONTROL Commerce Services Connector]. Learn [more](https://experienceleague.adobe.com/en/docs/commerce-merchant-services/user-guides/integration-services/saas#apikey).

### Check if the Service ID is in the allowlist and confirm with Adobe Commerce support

1. Verify that the [!UICONTROL Commerce Services Connector] `serviceId` appears in allowlist in Adobe Commerce.
1. Contact [Adobe Commerce support](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide) to confirm the allowlist status.

## Related reading

* [[!DNL Data Connection]](https://experienceleague.adobe.com/en/docs/commerce-merchant-services/data-connection/overview) extension in the Commerce Services user guide
* [Best practices for modifying database tables](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/development/modifying-core-and-third-party-tables#why-adobe-recommends-avoiding-modifications) in the Commerce Implementation Playbook
