---
title: Display Adobe Commerce error report number instead of Fastly 503 error
description: 'By default, Fastly hides all Adobe Commerce errors behind the **503 Service Unavailable** error. To display the Adobe Commerce error log report number (to be able to find it in logs and see the error details), open the website omitting Fastly using these steps:'
exl-id: c0a4a9f8-a674-4cef-8088-e844594e6076
feature: Cache, Cloud
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: 5a951749-fac9-5bc7-9a98-ebe4ff066437
    internal-label: Cloud
  - id: e7dae43f-215c-4cdf-90d3-c5a461a6e669
    internal-label: Admin tools and workspace
subfeature_v2:
  - id: b673188e-f9fa-492a-b470-c8f949bf7827
    internal-label: Cache
---
# Display Adobe Commerce error report number instead of Fastly 503 error

By default, Fastly hides all Adobe Commerce errors behind the **503 Service Unavailable** error. To display the Adobe Commerce error log report number (to be able to find it in logs and see the error details), open the website omitting Fastly using these steps:

1. Add your application's domain and IP address to your hosts file on your local machine.
1. Clear the browser cache and cookies (or switch to incognito mode).
1. Open your store's website again to see the Adobe Commerce error.

Once you see the authentic Adobe Commerce error and the error report number, you may get details in the error report file by following these steps:

1. SSH to the affected environment. Refer to [SSH to an environment](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/secure-connections) in our developer documentation.
1. Locate the `./var/report/{error_number}` file.

## Add application domain and IP address to your hosts file: detailed steps

1. Check the server IP of your store by executing the `nslookup` command in the command line on your local machine:
    * Pro architecture users (Staging and Production environments):

    ```
    nslookup {your_project_id}.ent.magento.cloud
    ```
    
    * Starter architecture users (all environments); Pro architecture users (Integration environment):
    
    ```
    nslookup gw.{your_region}.magentosite.cloud
    ```

1. Add your store domain and application server IP to the hosts file on your local machine using the following format:

```
{server_IP} {store_domain}
```
