---
title: Checklist for setting up a new [!DNL domain]
description: This is a checklist of how to set up a new [!DNL domain] in Adobe Commerce on cloud infrastructure.
exl-id: bfe0582d-2c6d-4814-908f-dfd8c898bef7
feature: Cache
---
# Checklist for setting up a new [!DNL domain]

This checklist explains how to set up a new [!DNL domain] in Adobe Commerce on cloud infrastructure. It applies whether you're adding a new domain or replacing the current one. It also applies after getting a new Staging environment (see Step 4).

## Affected products and versions

Adobe Commerce on cloud infrastructure, [all supported versions](https://www.adobe.com/content/dam/cc/en/legal/terms/enterprise/pdfs/Adobe-Commerce-Software-Lifecycle-Policy.pdf)

## How to set up a new domain

>[!NOTE]
>
>Before proceeding with domain setup, ensure that: 
>
>All Base URLs are configured to use HTTPS under **[!UICONTROL Stores]** > **[!UICONTROL Settings]** > **[!UICONTROL Configuration]** > **[!UICONTROL General]** > **[!UICONTROL Web]**, scoped to the correct website or store view.
> Force TLS is enabled to redirect all HTTP traffic to HTTPS across your Adobe Commerce site on cloud infrastructure.

### Step 1 - Is this for the [!DNL Integration, Staging], or [!DNL Production environment]?

* **[!DNL Integration]**: [!DNL Custom domains] are not supported. You must use this method instead: [Set up multiple websites or stores: Configure local installation](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/configure-store/multiple-sites.html#add-new-domains) in our user guide.
* **[!DNL Staging]**: Go to **Step 2**.
* **[!DNL Production]**: Go to **Step 3**.

### Step 2 - [!DNL Staging environment]: are you on [!DNL Pro] or [!DNL Starter]?

* **[!DNL Pro]**: **Submit a request** to add the domain to [!DNL Fastly, Nginx], and configure the [!DNL SSL certificate] (as well as the [!DNL Sendgrid domain], if necessary). Once that has been configured, [update the [!DNL DNS] configuration with [!DNL development settings]](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/cdn/setup-fastly/fastly-configuration.html#update-dns-configuration-with-development-settings).

>[!NOTE]
>
>For PRO architecture, adding a new domain requires submitting a support request to Adobe Commerce. While some customers may be able to manually configure Fastly via the Admin Console, this only applies in limited cases—such as when the domain isn’t tied to another Fastly service or project. However, Nginx configuration is always required, and this step must be handled by Adobe. Because of this, the recommended and most reliable approach is to submit a support ticket and let Adobe manage the entire domain setup process.


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
>1. You are migrating the domain from on-premises to the cloud environment, which has been configured in your own [!DNL Fastly] service. In this case, submit a request and request delegation of the domain.
>1. You are migrating the domain from Starter to Pro. In this case, submit a request for further assistance.

* **[!DNL Starter]**: Add the [!DNL domain] to your project in the **[!DNL Domains]** tab, then **submit a request** to provide the **[!DNL ACME Challenge Key]** for the [!DNL SSL certificate].

### Step 4 - Is the [!DNL domain] live?

* **YES**: [Update the [!DNL DNS] configuration with [!UICONTROL production] settings](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/launch/checklist.html#update-dns-configuration-with-production-settings).
* **NO**: [Update the [!DNL DNS] configuration with [!UICONTROL development] settings](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/cdn/setup-fastly/fastly-configuration.html#update-dns-configuration-with-development-settings).

### Step 5 - Are domain redirects configured in `magento-vars.php`?

After the domain has been configured, you need to [modify the variables](https://experienceleague.adobe.com/en/docs/commerce-on-cloud/user-guide/configure-store/multiple-sites#modify-variables) in the `magento-vars.php` file to direct the domain to the appropriate website/store URL.

### Step 6 - Is the [!DNL domain] configuration verified?

If you have added new stores, store groups, and websites in **[!UICONTROL Stores]** > **[!UICONTROL Settings]** > **[!UICONTROL All Stores]** for the new domain(s), check whether the following sections appear in your `app/etc/config.php` file, for example:

```php
'scopes' => [
    'websites' => [
        'admin' => [
            'website_id' => '0',
            'code' => 'admin',
            'name' => 'Admin',
            'sort_order' => '0',
            'default_group_id' => '0',
            'is_default' => '0',
        ],
        'base' => [
            'website_id' => '1',
            'code' => 'base',
            'name' => 'Main Website',
            'sort_order' => '0',
            'default_group_id' => '1',
            'is_default' => '1',
        ],
        'site2' => [
            'website_id' => '2',
            'code' => 'site2',
            'name' => 'Second Website',
            'sort_order' => '0',
            'default_group_id' => '2',
            'is_default' => '0',
        ],
    ],
    'groups' => [
        0 => [
            'group_id' => '0',
            'website_id' => '0',
            'name' => 'Default',
            'root_category_id' => '0',
            'default_store_id' => '0',
            'code' => 'default',
        ],
        1 => [
            'group_id' => '1',
            'website_id' => '1',
            'name' => 'Main Website Store',
            'root_category_id' => '2',
            'default_store_id' => '1',
            'code' => 'main_website_store',
        ],
        2 => [
            'group_id' => '2',
            'website_id' => '2',
            'name' => 'Second Website Store',
            'root_category_id' => '2',
            'default_store_id' => '2',
            'code' => 'site2store',
        ],
    ],
    'stores' => [
        'admin' => [
            'store_id' => '0',
            'code' => 'admin',
            'website_id' => '0',
            'group_id' => '0',
            'name' => 'Admin',
            'sort_order' => '0',
            'is_active' => '1',
        ],
        'default' => [
            'store_id' => '1',
            'code' => 'default',
            'website_id' => '1',
            'group_id' => '1',
            'name' => 'Default Store View',
            'sort_order' => '0',
            'is_active' => '1',
        ],
        'site2sv' => [
            'store_id' => '2',
            'code' => 'site2sv',
            'website_id' => '2',
            'group_id' => '2',
            'name' => 'Second Website Store view',
            'sort_order' => '0',
            'is_active' => '1',
        ],
    ],
]
```

This means that you have set up [SCD on Build](https://experienceleague.adobe.com/en/docs/commerce-on-cloud/user-guide/develop/deploy/static-content#setting-the-scd-on-build) by running the `config:dump` command in the `ece-tools` package in the past.

If you find that the new store/website you've created isn't showing in the `app/etc/config.php` file, make sure to run the command again to sync the `config.php` file with the changes to your database, then commit the `config.php` file and redeploy. This is to facilitate static content deployment for the new store/website(s) to the appropriate file paths.

## Related reading

* [Set up multiple websites or stores: Add New [!DNL Domains]](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/configure-store/multiple-sites.html#add-new-domains) in our user guide.
* [Site not accessible due to origin cloaking](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26856)
