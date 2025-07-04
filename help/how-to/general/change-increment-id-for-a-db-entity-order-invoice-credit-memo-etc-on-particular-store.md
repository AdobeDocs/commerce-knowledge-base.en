---
title: Change increment ID for a DB entity (order, invoice, credit memo, etc.) on particular store
description: This article discusses how to change the increment ID for an Adobe Commerce database (DB) entity (order, invoice, credit memo, etc.) on a particular Adobe Commerce store using the `ALTER TABLE` SQL statement.
exl-id: 3704dd97-3639-44dc-9b8b-cf09f0c04e6c
feature: Invoices
---
# Change increment ID for a DB entity (order, invoice, credit memo, etc.) on particular store

This article discusses how to change the increment ID for an Adobe Commerce database (DB) entity (order, invoice, credit memo, etc.) on a particular Adobe Commerce store using the `ALTER TABLE` SQL statement.

>[!NOTE]
>
>This article only describes how to change the starting numeric value of the increment ID for orders, invoices, credit memos, etc.
>
>It does not cover how to modify the increment ID format or add custom prefixes/suffixes (for example, changing 10000001 to ORDER-10000001, MYSTORE-10000001, 2A10000001, etc.)
>
>To customize the format, you will need a custom extension or development work.

## Affected versions

* Adobe Commerce on-premises: 2.x.x
* Adobe Commerce on cloud infrastructure: 2.x.x
* MySQL: any [supported version](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/system-requirements)

## When would you need to change increment ID (cases)

You might need to change the increment ID for new DB entities in these cases:

* After a hard backup restore on a Live site
* Some order records have been lost, but their IDs are already being used by payment gateways (like PayPal) for your current Merchant account. Such being the case, the payment gateways stop processing new orders that have the same ID's, returning the "Duplicate invoice id" error

>[!NOTE]
>
>You may also fix the payment gateway issue for PayPal by allowing multiple payments per invoice ID in PayPal's Payment Receiving Preferences. See [PayPal gateway rejected request - duplicate invoice issue](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-26838) in our support knowledge base.

## Prerequisite steps

1. Find stores and entities for which the new increment ID should be changed.
1. [Connect](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/prerequisites/database-server/mysql-remote) to your MySQL DB. For Adobe Commerce on cloud infrastructure, at first, you need to [SSH to your environment](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/secure-connections.html).
1. Check the current auto\_increment value for the entity sequence table using the following query:

```sql
SHOW TABLE STATUS FROM `{database_name}` WHERE `name` LIKE 'sequence_{entity_type}_{store_id}';
```

### Example

If you are checking an auto-increment for an order on the store with *ID=1*, the table name would be:

```sql
'sequence_order_1'
```

If the value of the `auto_increment` column is *1234*, the next order placed at the store with *ID=1* will have the *ID \#100001234*.

### Related documentation

* [Set up a remote MySQL database connection](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/prerequisites/database-server/mysql-remote) in our developer documentation.

## Update entity to change increment ID

Update the entity using the following query:

```sql
ALTER TABLE sequence_{entity_type}_{store_id} AUTO_INCREMENT = {new_increment_value};
```

>[!WARNING]
>
>Important: The new increment value must be greater than the current one, not less!

### Example

After executing the following query:

```sql
ALTER TABLE sequence_order_1 AUTO_INCREMENT = 2000;
```

the next order placed at the store with *ID=1* will have the *ID \#100002000*.

## Additional recommended steps on Production environment (Cloud)

Before executing the `ALTER TABLE` query on the Production environment of Adobe Commerce on cloud infrastructure, we strongly recommend performing these steps:

* Test the entire procedure of changing the increment ID on your Staging environment
* [Create](/help/how-to/general/create-database-dump-on-cloud.md) a DB backup to restore your Production DB in case of failure

## Related documentation

* [Create database dump on Cloud](/help/how-to/general/create-database-dump-on-cloud.md) in our support knowledge base
* [SSH to your environment](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/develop/secure-connections.html) in our developer documentation
* [Best practices for modifying database tables](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/development/modifying-core-and-third-party-tables#why-adobe-recommends-avoiding-modifications) in the Commerce Implementation Playbook
