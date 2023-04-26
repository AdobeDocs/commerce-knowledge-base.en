---
title: Adobe Commerce Fastly troubleshooter
description: This Fastly troubleshooter for Adobe Commerce users will guide you to the solutions, based on your response about the symptoms you see. Click on the questions to see the next options or answers.
exl-id: c5c51b89-5a7d-49ba-a0ee-7abbaf78fdad
---
# Adobe Commerce Fastly troubleshooter

This Fastly troubleshooter for Adobe Commerce users will guide you to the solutions, based on your response about the symptoms you see. Click on the questions to see the next options or answers.

## Step 1

+++**Customer reports a problem involving Fastly. Is the Fastly service down?**

a. YES – Check [Fastly Service Status](https://status.fastly.com/), and [submit an Adobe Commerce support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket).  
b. NO – Proceed to [Step 2](#step-2).

+++

## Step 2

+++**Do you have any errors when you run Backend Tester?**

Run your project URL through the [Backend Tester - Fastly](https://magento-tester.global.ssl.fastly.net/magento-tester/). It shows the version of VCL configuration file, if the page is cacheable, the version of Fastly module and other useful troubleshooting information. Do you have any errors?

a. YES – You have the message _Plugin VCL version is outdated! Please re-Upload._ For the solution to this error, refer to [Fastly Error: Plugin VCL version is outdated! Please re-Upload](/help/troubleshooting/miscellaneous/fastly-error-plugin-vcl-version-is-outdated-please-re-upload.md).  
b. NO – [Step 3](#step-3).

+++

## Step 3

+++**Image optimization error?**

a. YES – [Error when enabling image optimization](/help/troubleshooting/miscellaneous/error-enabling-image-optimization-in-magento-commerce.md).  
b. NO – Check DNS by running in the CLI/terminal: `dig [your website.com] + short`. Proceed to [Step 4](#step-4).

+++

## Step 4

+++**What happens when you run `dig`?**

When you ran `dig` did it return a record pointing to prod.magentocloud.map.fastly.net or one of the following IP addresses (see [Update DNS configuration with production setting](https://devdocs.magento.com/cloud/live/site-launch-checklist.html#dns) in our developer documentation):

* 151.101.1.124
* 151.101.65.124
* 151.101.129.124
* 151.101.193.124

a. YES – The issue is not DNS related. Proceed to [Step 5](#step-5).  
b. NO – The issue is likely DNS related. The customer should [check DNS configuration](https://devdocs.magento.com/cloud/live/site-launch-checklist.html#dns "https://devdocs.magento.com/cloud/live/site-launch-checklist.html#dns") or contact their DNS provider for more information.

+++

## Step 5

+++**Do you get a "Connection Insecure" or "Not Secure" message returned when running `curl -svo /dev/null "https://website.com"` in the CLI/terminal?**

a. YES – This is likely a certificate issue. Visit the website in a browser and select the lock icon and look for a certificate expiration. Proceed to [Step 6](#step-6).  
b. NO – Visit [http://fastly-debug.com](https://www.fastly-debug.com/) and share this information in an [Adobe Commerce support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket).

+++

## Step 6

+++**Is the certificate expired?**

a. YES – You need to renew your TLS certificate with the Certificate Authority (CA).  
b. NO – You may not have a certificate at all. If you have Adobe Commerce we recommend that you purchase a TLS certificate. If you are on Adobe Commerce on cloud infrastructure you can have a Domain-Validated Let's Encrypt SSL/TLS certificate to serve secure HTTPS traffic from Fastly. See [provision SSL/TLS certificates](https://devdocs.magento.com/cloud/cdn/configure-fastly.html#provision-ssltls-certificates) in our developer documentation.

+++

[Back to Step 1](#step-1)
