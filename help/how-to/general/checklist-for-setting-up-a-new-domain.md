---
title: Checklist for setting up a new [!DNL domain]
description: This is a checklist of how to set up a new [!DNL domain] in Adobe Commerce on cloud infrastructure.
exl-id: bfe0582d-2c6d-4814-908f-dfd8c898bef7
feature: Cache
---
# Checklist for setting up a new [!DNL domain]

This is a checklist of how to set up a new [!DNL domain] in Adobe Commerce on cloud infrastructure. It applies regardless of whether you are trying to simply add a new domain or replace the current domain with a new one.

## Affected products and versions

Adobe Commerce on cloud infrastructure, [all supported versions](https://www.adobe.com/content/dam/cc/en/legal/terms/enterprise/pdfs/Adobe-Commerce-Software-Lifecycle-Policy.pdf)

## How to set up a new domain

### Step 1 - Is this for the [!DNL Integration, Staging], or [!DNL Production environment]?

* **[!DNL Integration]**: [!DNL Custom domains] are not supported. You must use this method instead: [Set up multiple websites or stores: Configure local installation](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/configure-store/multiple-sites.html#add-new-domains) in our user guide.
* **[!DNL Staging]**: Go to **Step 2**.
* **[!DNL Production]**: Go to **Step 3**.

### Step 2 - [!DNL Staging environment]: are you on [!DNL Pro] or [!DNL Starter]?

* **[!DNL Pro]**: **Submit a request** to add the domain to [!DNL Fastly, Nginx], and configure the [!DNL SSL certificate] (as well as the [!DNL Sendgrid domain], if necessary). Once that has been configured, [update the [!DNL DNS] configuration with [!DNL development settings]](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/cdn/setup-fastly/fastly-configuration.html#update-dns-configuration-with-development-settings).

>[!NOTE]
>
>You can add the new [!DNL domain] to [!DNL Fastly] yourself by updating the configuration in the [!DNL Admin] in **[!UICONTROL Stores]** > **[!UICONTROL Configuration]** > **[!UICONTROL Advanced]** > **[!UICONTROL System]** > **[!UICONTROL Full Page Cache]** > **[!DNL Fastly Configuration]** > **[!UICONTROL Domains]** as in [[!DNL Manage domains]](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/cdn/setup-fastly/fastly-custom-cache-configuration.html#manage-domains) in our user guide.
>
>If you are unable to add the domain, it could be due to one of these reasons:
>
>1. You are migrating the domain to the Cloud environment, which has been configured in your own Fastly service - submit a request and request delegation of the domain
>1. You are migrating the domain from Starter to Pro - submit a request for further assistance.

* **[!DNL Starter]**: [!DNL Custom domains] are not supported on the Staging environment.

### Step 3 - [!DNL Production environment]: are you on [!DNL Pro] or [!DNL Starter]?

* **[!DNL Pro]**: **Submit a request** to add the domain to [!DNL Fastly, Nginx], and configure the [!DNL SSL certificate] (as the [!DNL Sendgrid domain], if necessary). Once that has been configured, continue to **Step 4**.

>[!NOTE]
>
>You can add the new [!DNL domain] to [!DNL Fastly] yourself by updating the configuration in the [!DNL Admin] in **[!UICONTROL Stores]** > **[!UICONTROL Configuration]** > **[!UICONTROL Advanced]** > **[!UICONTROL System]** > **[!UICONTROL Full Page Cache]** > **[!DNL Fastly Configuration]** > **[!UICONTROL Domains]** [[!DNL Manage domains]](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/cdn/setup-fastly/fastly-custom-cache-configuration.html#manage-domains) in our user guide.
>
>
>If you are unable to add the domain, it could be due to one of these reasons:
>
>1. You are migrating the domain from On-Premises to the Cloud environment, which has been configured in your own Fastly service - submit a request and request delegation of the domain
>1. You are migrating the domain from Starter to Pro - submit a request for further assistance.

* **[!DNL Starter]**: Add the [!DNL domain] to your project in the **[!DNL Domains]** tab, then **submit a request** to provide the **[!DNL ACME Challenge Key]** for the [!DNL SSL certificate].

### Step 4 - Is the [!DNL domain] live?

* **YES**: [Update the [!DNL DNS] configuration with [!UICONTROL production] settings](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/launch/checklist.html#update-dns-configuration-with-production-settings).
* **NO**: [Update the [!DNL DNS] configuration with [!UICONTROL development] settings](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/cdn/setup-fastly/fastly-configuration.html#update-dns-configuration-with-development-settings).

## Related reading

* [Set up multiple websites or stores: Add New [!DNL Domains]](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/configure-store/multiple-sites.html#add-new-domains) in our user guide.
