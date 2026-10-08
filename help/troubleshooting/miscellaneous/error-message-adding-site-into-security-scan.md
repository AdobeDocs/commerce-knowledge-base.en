---
title: Error message when adding sites into Security Scan
description: This article provides possible solutions for the issue when a user is not able to add sites into the [Commerce Security Scan](https://account.magento.com/scanner/dashboard/).
exl-id: 8d000ca4-b977-432d-bb26-6ea320067a40
feature: Cache, Compliance, Console, Security
role: Developer
product_v2:
  - id: eadea719-cf89-469b-a6fd-a236a7138047
    internal-label: Commerce
feature_v2:
  - id: b5f00040-57a0-4a6d-a39e-383b1936c2c9
    internal-label: Compliance
  - id: ba9e5be9-7de1-4f71-a5d2-baead0e425ee
    internal-label: Security
  - id: e7dae43f-215c-4cdf-90d3-c5a461a6e669
    internal-label: Admin tools and workspace
  - id: 125c1f49-aefd-5f34-a252-288937f95f6b
    internal-label: Marketing Tools
subfeature_v2:
  - id: b673188e-f9fa-492a-b470-c8f949bf7827
    internal-label: Cache
  - id: c4af0798-d497-5e6b-8380-19812c26d00a
    internal-label: Console
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Error message when adding sites into Security Scan

This article provides possible solutions for the issue when a user is not able to add sites into the [Commerce Security Scan](https://account.magento.com/scanner/dashboard/).

## Affected products and versions

* Adobe Commerce (all deployment methods and versions)
* Magento Open Source

## Issue

User is not able to add sites into the [Commerce Security Scan](https://account.magento.com/scanner/dashboard/). The following error message appears when trying to add a site: *Unable to submit site for scanning.*

## Solution

1. Make sure that the following IP addresses are not blocked on ports 80 and 443:
   * 52.87.98.44
   * 34.196.167.176
   * 3.218.25.102
 
1. The confirmation code is time-sensitive. If more than 30 minutes have passed after the **Add site** link was clicked, the code has probably expired.
1. Don't forget to clean cache and make sure the validation code appears in the home page source body. The confirmation code should be injected according to the HTML markup specs: HTML comment can be injected in the page body (we suggest putting it in the footer section); the META tag should be in the head section only.
1. Before clicking **Verify Confirmation code**, open the browser's developer console, click the **Network** tab and check the response from magento.com. It should be HTTP 200 (OK) and the response body should contain a JSON object.
1. If the response code is HTTP 200 and the response body is a JSON object and the `verified` property value is `false`, it means the code is not found on the page. The `details` property value should contain the explanation. For example, if the store uses a self-signed SSL certificate, there will probably be a connection error.

If you still cannot add sites, complete the following steps:

1. Place another HTML comment on the page:

    ```HTML
    <!-- MAGEID:Your magento.com ID, EMAIL:your email address -->
    ```

1. Submit a support ticket and provide the following information:
    * Adobe Commerce store URL
    * MAGEID + Magento.com account email
    * First name + Last name
    * Company name
    * Comma separated notification email list

## Related reading

* [Security Scan](https://experienceleague.adobe.com/en/docs/commerce-admin/systems/security/security-scan) in our user guide.
