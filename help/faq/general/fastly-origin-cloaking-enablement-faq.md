---
title: Fastly origin cloaking enablement FAQ
description: This FAQ discusses common questions about Fastly origin cloaking enablement in Adobe Commerce (that has been fully implemented as of 2021).
exl-id: d608abe7-7d64-44ce-bea1-34b201c29113
---
# Fastly origin cloaking enablement FAQ

This FAQ discusses common questions about [!DNL Fastly] origin cloaking enablement in Adobe Commerce (that has been fully implemented as of 2021).

## What is Fastly origin cloaking?

Origin cloaking is a security feature that allows Adobe Commerce on cloud infrastructure to block any non-Fastly traffic (to prevent DDoS attacks, going to the cloud infrastructure (origin).

## What are origin cloaking’s benefits?

Origin cloaking is designed to prevent traffic from bypassing the Fastly Web Application Firewall (WAF) and routing it through the strictly defined flow of **Fastly** > **Load Balancer** > **Instances**. With this implementation, all the traffic is guaranteed to go through the Fastly WAF as well as the internal WAF built into the load balancer.

## Why is this origin cloaking enablement happening?

This feature was originally created to benefit Adobe Commerce on cloud infrastructure.

## Do I need to request origin cloaking enablement for my project?

No. This feature should have already been implemented on all cloud projects, and any projects that have been provisioned since 2021 would have had this enabled by default. However, you may request that origin cloaking be disabled for your project by submitting a support request.

## Does origin cloaking change the outgoing IP address?

No, it does not.

## Does origin cloaking impact REST API?

Fastly does not cache API calls, so the client should be fine with the change. Origin cloaking only blocks requests that go straight to the origin, such as:

```php
mywebsite.com.c.abcdefghijkl.ent.magento.cloud
```

In this example, the client will still be able to hit the API if they change the URL to ``mywebsite.com``:

```php
mywebsite.com/rest/default/V1/integration/admin/token?username=XXXX&password=XXXXX;
mywebsite.com/rest/default/V1/orders/
mywebsite.com/rest/default/V1/products/
mywebsite.com/rest/default/V1/inventory/source-items
```

## Will this change impact deployment and downtime?

No, this change will **NOT** impact deployment and downtime.

## If the project has multiple staging environments, will origin cloaking be applied to all staging environments?

Yes, if the project has multiple staging environments, the change will be applied to all staging environments.
