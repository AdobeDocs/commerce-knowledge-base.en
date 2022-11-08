---
title: Manual order export to MOM fails. The Export Order button returns HTTP 404 error
description: This article discusses how to fix an issue, where trying to export an order to Magento Order Management (MOM) by clicking the **Export Order** button on the order view in the Commerce Admin returns a " *404 Page Not Found* " error.
exl-id: 75741473-7c9a-4418-a56f-de75ac246d27
---
# Manual order export to MOM fails. The Export Order button returns HTTP 404 error

This article discusses how to fix an issue, where trying to export an order to Magento Order Management (MOM) by clicking the **Export Order** button on the order view in the Commerce Admin returns a " *404 Page Not Found* " error.

## Affected products and versions

* Adobe Commerce 2.2.x, 2.3.x
* MOM Connector 2.3.0, 2.4.0, 3.2.0, 3.3.0

## Issue

<u>Steps to reproduce:</u>:

1. In the Commerce Admin, click **Sales > Orders**.
1. Click the **Create New Order** button.
1. Select a user, add an item(s), select payment and shipping methods, and then click the **Submit Order** button.
1. Click the **Export Order** button and then **OK**.

<u>Expected result</u>:

The order is sent to MOM.

<u>Actual result</u>:

A " *404 Error: Page Not Found* " page is displayed.

## Solution

* Upgrade the MOM Connector to 3.4.0 for Adobe Commerce 2.3.x, or MOM Connector 2.5 for Adobe Commerce 2.2.x.
* If upgrading the MOM Connector is not an option, you can export the order to Magento Order Management using the CLI command:

```bash
$bin/magento oms:orders:sync
```

## Related reading

 [Magento Order Management technical documentation](https://omsdocs.magento.com/en/)
