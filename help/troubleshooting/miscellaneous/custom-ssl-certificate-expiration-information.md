---
title: Custom SSL certificate expiration information
description: This article provides a solution for when a custom SSL certificate was updated with an Adobe provided SSL certificate.
exl-id: cc968bae-f742-449b-b291-bc121ec45935
feature: Support
role: Developer
---
# Custom SSL certificate expiration information

This article provides a solution for when a custom SSL certificate was updated with an Adobe provided SSL certificate.

## Affected products and versions

Adobe Commerce on cloud infrastructure, [all supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf)

## Issue

Adobe Commerce automatically updates SSL certificates 30 days prior to expiration. This automation does not check if the certificate being replaced is an internal SSL or a custom third-party SSL and will replace it with a valid internal SSL upon detection of expiration. This can cause confusion for site owners and operators that expect to have the custom certificate on the site, as well as the potential for other functionality issues including, but not limited to, a site outage.

<u>Steps to reproduce</u>

1. Custom SSL certificate installed for the website.
1. Automation detects the custom SSL certificate is 30 days away from expiring.
1. Adobe Commerce automatically replaces the custom certificate with our internal certificate.

<u>Expected results</u>

Adobe Commerce skips custom certificates when running its automated SSL certificate update.

<u>Actual results</u>

Adobe Commerce updates any certificate when it is 30 days from expiration.

## Solution

When a merchant elects to use their own custom SSL certificate, it must be updated more than 30 days prior to the certificate expiration to ensure it will not be replaced by an internal Adobe Commerce SSL certificate.

If you are in a situation where your custom SSL was replaced by our internal SSL and you want to replace it with your updated custom SSL certificate, please [submit a support request](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket) with the location you uploaded your new certificate files. Please include the start date of the new SSL. Once we have this information, we can move forward with installing the new SSL certificate.

## Related reading

* [SSL (TLS) certificates for Magento Commerce Cloud: FAQ](/help/how-to/general/ssl-tls-certificates-for-magento-commerce-cloud-faq.md) in our support knowledge base.
* [Command-line tools reference: magento-cloud certiificate:add](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/dev-tools/cloud-cli/cloud-cli-reference#certificateadd) in our developer documentation.
* [Launch checklist](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/launch/checklist)in our developer documentation.
* [Access Site-Wide Analysis Tool](https://experienceleague.adobe.com/en/docs/commerce-operations/tools/site-wide-analysis-tool/access#step-2-access-site-wide-analysis-tool) in our user guide.
