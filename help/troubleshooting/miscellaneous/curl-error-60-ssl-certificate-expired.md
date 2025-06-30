---
title: 'cURL error 60: SSL certificate expired'
description: 'This article shows how to check when the last time a branch was deployed after receiving a cURL error 60: SSL certificate expired in the Master or Integration branches on Adobe Commerce on cloud infrastructure.'
exl-id: 74f1db7e-ee2b-4e27-8fcc-fe462a9e72c3
feature: Configuration
role: Developer
---
# cURL error 60: SSL certificate expired

This article shows how to check when the last time a branch was deployed after receiving a `cURL error 60`: [!DNL SSL certificate] expired in the [!DNL Master] or [!DNL Integration] branches on Adobe Commerce on cloud infrastructure.

## Affected products and versions

* Adobe Commerce on cloud infrastructure, [all supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf)

## Cause

The [!DNL SSL certificates] in those branches are only valid for 30 days, and the branch may have not been re-deployed in over 30 days.

The error will look similar to this:

```cURL
cURL error 60: SSL certificate problem: certificate has expired
```

>[!NOTE]
>
>These certificates are not signed by well-known external Certificate Authorities (CAs) like [!DNL Let's Encrypt] or [!DNL DigiCert]. They are managed by the Adobe platform for the purposes of testing and development, and may not be trusted by default in browsers or curl unless you explicitly trust the root issuing the certificate.

## Solution

Check when the last time the branch was deployed. If over the 30-day threshold, then re-deploy the branch.

Two methods to check for when the last deployment was performed:

* [Method 1: Use [!DNL magento-cloud] CLI](#meth2).
* [Method 2: Open the [!DNL Project URL]](#meth3).

If the deployment has been completed successfully, the [!DNL SSL certificate] will be automatically renewed.

If the deployment fails and you need assistance resolving it, [submit a support ticket](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/help-center-guide/magento-help-center-user-guide.html#submit-ticket).

### Method 1: Use [!DNL magento-cloud] CLI {#meth2}

Run this command: `magento-cloud activity:list --type=environment.push`

### Method 2: Open the [!DNL Project URL] {#meth3}

Go to, for example: `https://demo.magento.cloud/#/projects/<project>/environments/<environment>`, and check when the last deployment was performed.

## Related reading

In our developer documentation:

* [Cloud Manager API: SSLCertificates](https://developer.adobe.com/experience-cloud/cloud-manager/reference/api/#tag/SSLCertificates)
* [Set up Fastly: Provision SSL/TLS certificates](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/cdn/setup-fastly/fastly-configuration#provision-ssltls-certificates)

In our support knowledge base:

* [Custom SSL certificate expiration information](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/custom-ssl-certificate-expiration-information.html)
* [SSL (TLS) certificates for Adobe Commerce on cloud infrastructure](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/how-to/ssl-tls-certificates-for-magento-commerce-cloud-faq.html)
