---
title: High throughput AJAX requests cause poor performance
description: This article provides a solution for performance issues with Adobe Commerce on-premises or Adobe Commerce on cloud infrastructure sites due to some high throughput requests causing significant server load and traffic.
exl-id: 68dfca8a-826c-4476-acaf-a139052b5dcc
feature: Cache
role: Developer
---
# High throughput AJAX requests cause poor performance

This article provides a solution for performance issues with Adobe Commerce on-premises or Adobe Commerce on cloud infrastructure sites due to some high throughput requests causing significant server load and traffic.

## Affected products and versions

* Adobe Commerce on cloud infrastructure 2.2.x, 2.3.x
* Adobe Commerce on-premises 2.2.x, 2.3.x

>[!NOTE]
>
>The issue was fixed in version 2.3.4 of both Adobe Commerce on cloud infrastructure and Adobe Commerce on-premises.

### Issue

The site experiences a slow performance due to high throughput requests, like critical AJAX requests.

### Cause

High throughput AJAX requests include those related to customers' private content.

### Solution

There are three solutions:

* [Upgrade to version 2.3.4](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/develop/upgrade/commerce-version).
* Ensure lighter requests (cache requests or move to customers' private content).
* Reduce the number of requests.

<u>Ensure lighter requests (cache requests or move to customers' private content)</u>

If there are third-party AJAX requests that are triggered on each page, attempt to cache these requests or move them to customers' private content. The merchant can do this by making sure that custom AJAX requests are called using the GET HTTP methods. It will make these requests cacheable by Fastly. If there are custom AJAX requests that should not be cached, they should be refactored according to private-content functionality. For steps, refer [Private Content](https://developer.adobe.com/commerce/php/development/cache/page/private-content/) in our developer documentation.

 <u>Reduce the number of requests</u>

* Disable the persistent shopping cart, as it can increase the number of `customer/section/load` requests. Follow the steps in [Persistent shopping cart paths](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/paths/config-reference-general) in our developer documentation to see if persistent shopping cart is enabled.
* If you need to reload or invalidate content in `sections.xml` follow the steps in [Private content: Invalidate private content](https://developer.adobe.com/commerce/php/development/cache/page/private-content/#invalidate-private-content) in our developer documentation. Please make sure that you are not using the `customerData.reload()` method directly in your customizations.
* Check other POST AJAX requests on the same page. Open Google Chrome developer tool in Google Chrome browser. Click on the **Network** tab and then the **XHR** tab, and there will be the list of all AJAX requests from the particular page. Then click on each request, and in the field Request Method should be the GET requests. Note: Google Chrome is used as an example, and it is possible to do this in other browsers as well.
* Check Google Tag Manager (GTM) functionality which is a specific AJAX request. The user can remove this AJAX and refactor their customization with private functionality to reduce the total number of requests to the server.
* Check if the Adobe Commerce Banner is enabled but not used. You might need to [Disable Adobe Commerce Banner output to improve site performance](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26909).

### Related Reading

For more information on private customer content, review [Private content](https://developer.adobe.com/commerce/php/development/cache/page/private-content/) in our developer documentation.
