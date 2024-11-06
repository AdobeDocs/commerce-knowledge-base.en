---
title: Do I need Fastly for a Headless Adobe Commerce site?
description: Do I need Fastly for a Headless Adobe Commerce site?
exl-id: d7e07160-6a61-4c03-8f8c-4f879d86ea44
feature: Cache, GraphQL, Compliance
---
# Do I need Fastly for a Headless Adobe Commerce site?

>[!NOTE]
>
>All customers must use Fastly for their production and staging environments. Fastly is a Content Delivery Network (CDN) that provides full page caching, image optimization, and security services (DDoS and WAF) as part of your Adobe Commerce on cloud infrastructure projects. These are core components of the Adobe Commerce solution, providing increased performance and security. These features are part of Adobe's PCI Compliance. You must set up these Fastly services on your Starter Master, Staging, Pro Staging and Production environments. If you are using Adobe Commerce in a headless deployment, all API traffic from the public internet must pass through Fastly and we highly recommend that you use Fastly to cache GraphQL responses. See [GraphQL Developer Guide > Caching with Fastly](https://developer.adobe.com/commerce/webapi/graphql/usage/caching/#caching-with-fastly) in our developer documentation.

## **Question**

I am developing a headless implementation of Adobe Commerce. Do I still need to use Fastly as a CDN service for it?

## **Answer**

No, you don't. In this situation, you may skip using Fastly &ndash; at least, in the beginning of development.

The only situation you may not want to enable is for a headless deployment.
See [Cloud for Adobe Commerce > Fastly](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/cdn/fastly) in our developer documentation.

Still, most probably, you will need Fastly for using its SSL certificate.

All Adobe Commerce on cloud infrastructure customers get a shared SSL certificate from Fastly as a part of the cloud subscription plan. Adding own SSL certificate to Fastly is a separate and rather expensive paid option. Thus, we strongly recommend to enable Fastly and, at least, test it on Staging and Production environments before going live &ndash; even for your headless Adobe Commerce website.

## More information

* [Headless Websites: What's the Big Deal with Decoupled Architecture?](https://pantheon.io/blog/headless-websites-whats-big-deal-decoupled-architecture) by [Josh Koenig](https://pantheon.io/team/josh-koenig).
* [Fastly](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/cdn/fastly) in our developer documentation.
