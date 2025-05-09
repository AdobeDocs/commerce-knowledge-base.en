---
title: SSL (TLS) certificates for Adobe Commerce on cloud infrastructure
description: This article provides quick answers to questions about getting SSL (TLS) certificates for your Adobe Commerce site on our cloud infrastructure.
exl-id: 5a682d07-e4d7-4e81-a2ad-3232f2d8d9c1
feature: Cloud, Console
---
# SSL (TLS) certificates for Adobe Commerce on cloud infrastructure

This article provides quick answers to questions about getting SSL (TLS) certificates for your Adobe Commerce site on our cloud infrastructure.

## What SSL/TLS certificate does Adobe provide?

Adobe provides a Domain-Validated [Let's Encrypt SSL/TLS certificate](https://letsencrypt.org/) to serve secure HTTPS traffic from [!DNL Fastly]. Adobe provides one certificate for each Adobe Commerce on cloud infrastructure Pro plan architecture, Staging, and Adobe Commerce on cloud infrastructure Starter plan architecture environment to secure all domains in that environment.

## What does a certificate cover?

For the Pro plan architecture, both Staging and Production dedicated environments will have a SSL certificate created. Each dedicated environment outside of the Platform-as-a-Service (PaaS) Integration environments will have this certificate for the URLs that are assigned to that environment.

For the Starter plan architecture and PaaS Integration environments, there will be a default technical domain that is provisioned with the environment and secured by a separate certificate.

## How to add a new domain for the existing certificate?

To add the domain to the service in [!DNL Fastly]:

1. Point your domain in DNS to prod.magentocloud.map.fastly.net and wait up to 6 hours.
1. [Submit a support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket) requesting to add this domain in the Nginx configuration (if you haven't done it earlier).

## How to request a certificate?

Case 1

If you have not launched a website yet, you may have received ACME Challenge CNAME from your Customer Technical Advisor (CTA). You only need an ACME challenge if you cannot immediately point your DNS to your production URL and need to get the SSL certificates created in advance.

Case 2

If your site is already live and/or you can point the URLs that will be used for your live site right away, you do not need to request an ACME CNAME. Once you add the URLs as necessary to your Adobe Commerce on cloud infrastructure site and point your DNS at [!DNL Fastly], HTTP validation will work and either create your SSL certificate for the first time or update your certificate with additional URLs.

## Can I use my own SSL/TLS certificate?

You can provide your own SSL/TLS certificate instead of using the [Let's Encrypt certificate](https://letsencrypt.org/) provided by Adobe. 

However, this process requires additional work to set up and maintain. You will first need to generate a Certificate Signing Request (CSR) for the website's domain name (or common name) and provide it to your SSL vendor to provide an SSL certificate. 

Once you have the SSL certificate, submit an [Adobe Commerce Support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket) or work with your CTA to add custom-hosted certificates to your cloud environments. 

* If the domains are no longer in use, they will be automatically purged from our system, and no further action is required. 
* If you already own a certificate, upload it using an SFTP (SSH File Transfer Protocol) client to a web-inaccessible file location on your server and [submit a support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket) letting them know the file path.

>[!WARNING]
>
>It is important that you do not upload the certificate files directly to the ticket. Otherwise, the certificates will be considered compromised, and Adobe will need to request a new certificate.
>The files should be uploaded via SFTP to the server to a folder of your choice, e.g., `var/ssl`, `/tmp/ssl`, etc. - do not use any other methods like committing the files to your repository (which should only be done for immutable files that do not contain sensitive data.)

## The name of your certificate

The name of the SSL certificate only matters for the primary URL, and it is the primary hostname named by the first URL and must match to be validated and created. If you have a few URLs, they will be added as subject alternate name entries to the certificate. If you have several URLs pointing to one Adobe Commerce on cloud infrastructure site, you will only have one common name URL certification that will then have appended subject alternative names to secure your site with SSL.

## What domain will be displayed in the Common Name field of the certificate?

The domain displayed on the certificate is just the first domain added to the TLS certificate, it populates the **Common Name** (**CN**) field, and browsers display this name first. The **Subject Alternative Name** (**SAN**) field contains all of the DNS names for the TLS certificate. There is no way to change or request the Common Name displayed.

## Can I use wildcard TLS certificates?

Wildcard TLS certificates can only be used with your custom certificate and not with Adobe Commerce Let's Encrypt certificates. As part of our TLS optimization, Adobe is ending support for wildcard TLS certificates. We are identifying and contacting merchants that use a wildcard certificate with Adobe's Let's Encrypt certificates and are configured in the [!DNL Fastly] console for Adobe Commerce. We are asking that these wildcard certificates be replaced with exact domains to ensure TLS coverage. To replace a wildcard TLS certificate, please visit the [domain section](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/cdn/setup-fastly/fastly-custom-cache-configuration#manage-domains) of the [!DNL Fastly] plugin. From here, exact domains can be added, and the wildcard can be removed. Please note that DNS will need to point to [!DNL Fastly] for these new domains to route through the CDN. Once the domains are added and DNS is updated, a matching [Let's Encrypt](https://letsencrypt.org/) certificate will be provisioned. If you don't remove a domain that is pointing to [!DNL Fastly] using a wildcard, Adobe will delete the shared certificate. This may result in a site outage if you do not have the URL FQDN configured and the same URL FQDN set up in your DNS. You should therefore confirm that the URLs configured also have a one-to-one match in their DNS pointing to [!DNL Fastly].

## What should I do if my domain is no longer pointing to Adobe Commerce?

If your domain is no longer pointing to Adobe Commerce, please remove it from the [!DNL Fastly]/Adobe Commerce system. See [!DNL Fastly] [Deleting a domain](https://docs.fastly.com/en/guides/working-with-domains#deleting-a-domain) to learn more. While it is not necessary to point your domain to Adobe Commerce, confirm if a top-level domain TLS certificate is required. If a top-level domain is required, please update your DNS to point to Adobe Commerce. If it is already pointing to Adobe Commerce, update your CAA record to include [lets-encrypt](https://letsencrypt.org/). If you perform these steps, you will see the LE Cert updated with the necessary secondary URL's that the cert covers.​

## Related reading

 [Provision SSL/TLS certificates](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/cdn/setup-fastly/fastly-configuration#provision-ssltls-certificates) in our developer documentation
