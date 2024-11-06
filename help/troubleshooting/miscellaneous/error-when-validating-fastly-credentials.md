---
title: Error when validating the Fastly credentials
description: This article provides a solution for the issue where a user gets an error when validating the Fastly credentials.
exl-id: 02104731-6666-47a6-abc6-215812f09915
feature: Configuration
role: Developer
---
# Error when validating the Fastly credentials

This article provides a solution for the issue where a user gets an error when validating the Fastly credentials.

## Issue

User gets an error when validating the Fastly credentials.

## Affected products and versions

* Adobe Commerce (all deployment methods): All versions
* Extension or technology (Fastly, New Relic, etc.) version Fastly

## Solution

1. Make sure you have the correct Fastly service ID and API token and try to validate again. For detailed instruction, refer to [Test the Fastly credentials](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/cdn/setup-fastly/fastly-configuration#test-the-fastly-credentials) in our developer documentation.
1. If the verification of the credentials fails, run the following curl command to confirm the status of the service:

    ```curl
    curl -H "Fastly-Key: <API key>" https://api.fastly.com/service/<service ID>/version/active
    ```

1. If the above command returns an error similar to: *{"msg":"Token $TOKEN expired at 2021-09-28T02:03:37Z"}*, submit a support ticket to request a new API token.

    To learn how to submit a support ticket, refer to [Adobe Commerce Help Center User Guide > SUPPORT TICKETS](/help/help-center-guide/help-center/magento-help-center-user-guide.md#support-tickets) in our support knowledge base.

    >[!NOTE]
    >
    >Never share any passwords or valid/active API tokens directly in the ticket as we will have to revoke the current token and generate a new one for security reasons.

1. If the command doesn't return the error, make sure that you are running the newest version of the [!DNL Fastly] extension. If you are on an older version prior to 1.2.203, you must first click on **[!UICONTROL Save Config]** before you can test the credentials.

## Related readings in our developer documentation:

* [Cloud for Adobe Commerce > Fastly > Fastly service account and credentials](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/cdn/fastly#fastly-service-account-and-credentials)

* [Cloud for Adobe Commerce > Set up Fastly > Test the Fastly credentials](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/cdn/setup-fastly/fastly-configuration#test-the-fastly-credentials)
