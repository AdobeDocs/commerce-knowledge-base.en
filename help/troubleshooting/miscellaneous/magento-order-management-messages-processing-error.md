---
title: Magento Order Management System (OMS) for Adobe Commerce processing error
description: This article provides a solution for the issue when you get a `getMode()` error in the CLI running `bin/magento oms:messages:process` in the Magento Order Management System (OMS) for Adobe Commerce.
exl-id: 83089465-f810-4a3b-bdb6-4720b44f0b49
feature: System
role: Developer
---
# Magento Order Management System (OMS) for Adobe Commerce processing error

This article provides a solution for the issue when you get a `getMode()` error in the CLI running `bin/magento oms:messages:process` in the Magento Order Management System (OMS) for Adobe Commerce.

## Affected products and versions

This error occurs when using MCOM Connector release 3.1.1 and 3.2.0. It is resolved in MCOM Connector 3.3.0. It is not specific to an MDC or MOM version.

## Issue

When running the following command in the CLI:

 `bin/magento oms:messages:process`

An error message similar to the following is outputted in the CLI:

```
<project-id>@<project-id>:~$ php bin/magento oms:messages:process

Processing messages...

PHP Fatal error:Uncaught Error: Call to a member function getMode()
on null in /app/<project-id>/vendor/magento/module-inventory-message-bus/Handler/OnAggregateStockUpdatedSubscriber.php:64

Stack trace:

  #0 [internal function]: Magento\InventoryMessageBus\Handler\OnAggregateStockUpdatedSubscriber->onUpdated(Object(Magento\InventoryMessageBus\Model\Event\OnAggregateStockUpdated))

  #1 /app/<project-id>/vendor/magento/module-service-bus/Message/SingleMessageProcessor.php(81):
  call_user_func(Array, Object(Magento\InventoryMessageBus\Model\Event\OnAggregateStockUpdated))

  #2 [internal function]: Magento\ServiceBus\Message\SingleMessageProcessor->Magento\ServiceBus\Message\\{closure}(Array)

  #3 /app/<project-id>/vendor/magento/module-service-bus/Message/SingleMessageProcessor.php(86):
  array_map(Object(Closure), Array)

  #4 /app/<project-id>/vendor/magento/module-service-bus/Message/Processor.php(110):
  Magento\ServiceBus\Message\SingleMessageProcessor->process(Object(Magento\CommonMessageBus\Message\Message))

  #5 /app/t in /app/<project-id>/vendor/magento/module-inventory-message-bus/Handler/OnAggregateStockUpdatedSubscriber.php
  on line 64
```

## Cause

Â
This occurs when the Connector attempts to process `magento.inventory.source_management` messages. The Connector attempts to process these messages as if they were a `magento.inventory.source_stock_management.update` message which does require a mode value. Because there is no mode in the `magento.inventory.source_mangement` messages, the error occurs.

## Solution

To resolve the problem run the following [!DNL SQL] statement in the CLI which deletes all records in the `mcom_api_messages` table:

 `delete from mcom_api_messages;`

## Related Reading

* OMS Docs [OMS Connector Setup Tutorial](https://commerce-docs.github.io/oms-documentation-archive/integration/connector/setup-tutorial/)
* [Best practices for modifying database tables](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/development/modifying-core-and-third-party-tables#why-adobe-recommends-avoiding-modifications) in the Commerce Implementation Playbook
