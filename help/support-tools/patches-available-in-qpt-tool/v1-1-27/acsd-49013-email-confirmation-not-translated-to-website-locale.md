---
title: "ACSD-49013: email confirmation not translated to website locale"
description: Apply the ACSD-49013 patch to fix the Adobe Commerce issue where email confirmation is not translated to the website locale when creating customers using bulk API.
---
# ACSD-49013: email confirmation not translated to website locale

The ACSD-49013 patch fixes the issue where email confirmation is not translated to the website locale when creating customers using bulk API. This patch is available when the [[!DNL Quality Patches Tool (QPT)]](/help/announcements/adobe-commerce-announcements/magento-quality-patches-released-new-tool-to-self-serve-quality-patches.md) 1.1.27 is installed. The patch ID is ACSD-49013. Please note that the issue is scheduled to be fixed in Adobe Commerce 2.4.7.

## Affected products and versions

**The patch is created for Adobe Commerce version:**

* Adobe Commerce (all deployment methods) 2.4.4

**Compatible with Adobe Commerce versions:**

* Adobe Commerce (all deployment methods) 2.4.3 - 2.4.6

>[!NOTE]
>
>The patch might become applicable to other versions with new [!DNL Quality Patches Tool] releases. To check if the patch is compatible with your Adobe Commerce version, update the `magento/quality-patches` package to the latest version and check the compatibility on the [QPT landing page](https://experienceleague.adobe.com/tools/commerce-quality-patches/index.html). Use the patch ID as a search keyword to locate the patch.

## Issue

Email confirmation is not translated to the website locale when creating customers using bulk API.

<u>Steps to reproduce</u>:

1. Install a different locale like `de_DE`.
1. Configure *RabbitMQ*.
1. Execute `bin/magento setup:upgrade` to install the queues in RabbitMQ and set up the language pack.
1. Create an additional website in [!UICONTROL Admin] > **[!UICONTROL Stores]** > **[!UICONTROL All Stores]**.
1. Set the locale of this new website to `de_DE` in [!UICONTROL Admin] > **[!UICONTROL Stores]** > **[!UICONTROL Configuration]** > **[!UICONTROL General]** > **[!UICONTROL Locale Options]**.
1. Execute an API call to create a customer account using bulk API. Use the corresponding `website_id`. 

    `Endpoint: /rest/async/bulk/V1/customers`

    ```
    [{
        "customer": {
        "email": "test@example.com",
        "firstname": "test",
        "lastname": "test",
        "website_id": 2
        },
        "password": "Passw0rd!"
    }]
    ```

1. Execute `bin/magento queue:consumers:start async.operations.all --single-thread --max-messages=10`.
1. You can see the customer account is created correctly on the specified website.
1. Check the email received for customer registration.

<u>Expected results</u>:

Since the customer is created on a specified website, the registration email should also be sent using the locale of that website.





