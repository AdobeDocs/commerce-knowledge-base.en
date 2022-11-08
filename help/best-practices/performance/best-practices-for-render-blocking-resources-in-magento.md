---
title: Best practices for render-blocking resources in Adobe Commerce
description: This article provides guidance on preventing resources blocking page rendering in Adobe Commerce, which can lead to a significant increase in page rendering time and cause performance degradation.
exl-id: 4e1009eb-69b2-47b2-b356-a7aa0718e1d5
---
# Best practices for render-blocking resources in Adobe Commerce

This article provides guidance on preventing resources blocking page rendering in Adobe Commerce, which can lead to a significant increase in page rendering time and cause performance degradation.

## Affected products and versions

* Adobe Commerce on-premises, all [supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf)
* Adobe Commerce on cloud infrastructure, all [supported versions](https://magento.com/sites/default/files/magento-software-lifecycle-policy.pdf)

## Best practices

Consider delivering critical JS/CSS features inline and deferring all non-critical JS/CSS styles. For guidance, refer to web.dev [Eliminate render-blocking resources](https://web.dev/render-blocking-resources/).

If assistance is required or if there are questions or concerns, [submit a support ticket](/help/help-center-guide/help-center/magento-help-center-user-guide.md#submit-ticket).

## Related reading

* See [Optimizing Resource Files](https://docs.magento.com/user-guide/system/file-optimization.html) in our user guide.
* See [Optimize CSS and JS files Adobe Commerce](/help/best-practices/configuration/optimize-css-and-js-files-in-magento-commerce.md) in our support knowledge base.
* See [Frontend Developer Guide > Cascading style sheets (CSS) > CSS merging, minification and performance](https://devdocs.magento.com/guides/v2.3/frontend-dev-guide/css-topics/css-overview.html#css-merging-minification-and-performance) in our developer documentation.
