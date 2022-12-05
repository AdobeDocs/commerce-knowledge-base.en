---
title: Adobe Commerce database numeric value out of range, `INT` to `BIGINT`
description: This article provides solutions for when you are unable to save a product update, like a price change, or deleting, and duplicating a product.
exl-id: e2a00371-9032-4e81-b60e-5456ba35be94
---
# Adobe Commerce database numeric value out of range, `INT` to `BIGINT`

>[!WARNING]
>
>Before implementing the solution in this article (`INT` to `BIGINT` schema update) merchants must always check that the field they are going to change DOES NOT have any foreign-key relationships to another table. If the field does have foreign-key relationships to another table, there will issues because the related field is still `INT`. They can use the following query to verify this. This query lists the foreign-key relationships available in the database for the given table field: 
>```mysql
>SELECT 
>   TABLE_NAME,COLUMN_NAME,CONSTRAINT_NAME,REFERENCED_TABLE_NAME,REFERENCED_COLUMN_NAME
>FROM
>  INFORMATION_SCHEMA.KEY_COLUMN_USAGE
>WHERE
>   REFERENCED_TABLE_SCHEMA = '<database_name>' AND
>   REFERENCED_TABLE_NAME = '<table_name>' AND
>   REFERENCED_COLUMN_NAME = '<table_field>';
>```

## Affected products and versions

* Adobe Commerce (all deployment methods) all [supported versions](https://www.adobe.com/content/dam/cc/en/legal/terms/enterprise/pdfs/Adobe-Commerce-Software-Lifecycle-Policy.pdf)

This article provides solutions for when you are unable to save a product update, like a price change, or deleting, and duplicating a product. 
You may see the error message *The stock item was unable to be saved. Please try again.* You might fail to deploy after a product update. You may also see the following MySQL error message when you run `php bin/magento setup:upgrade` (on Adobe Commerce on cloud infrastruture this error shows in the deployment logs):

```mysql
SQLSTATE[22003]: Numeric value out of range: 167 Out of range value for column 'value_id' at row 1, query was: INSERT INTO `catalog_product_entity_decimal` (`attribute_id`,`store_id`,`row_id`,`value`) VALUES (?, ?, ?, ?) ON DUPLICATE KEY UPDATE `attribute_id` = VALUES(`attribute_id`), `store_id` = VALUES(`store_id`), `row_id` = VALUES(`row_id`), `value` = VALUES(`value`)
```

The solutions described in the article are:
* Update the `[ AUTO_INCREMENT ]` to the next value from the table or
* `INT` to `BIGINT` schema update

Which solution you use depends on what has caused the issue. Refer to the steps below to isolate the cause.

## Steps to check the cause


Check the highest value of the primary key by running the following command in the terminal: `SELECT MAX(value_id) FROM catalog_product_entity_int;`

If the `max(value_id)` is lower than the `max int(11) [ 4294967296 ]`, and the `[ AUTO_INCREMENT ]` has a value greater than or equal to the `max int(11) [ 4294967296 ]`, then consider [updating the `[ AUTO_INCREMENT ]` to the next value from the table](#update-the-auto-increment-to-the-next-value-from-the-table). Otherwise, consider a [`INT` to `BIGINT` schema update](#int_to_bigint_schema_update).

## Update the `AUTO_INCREMENT` to the next value from the table {#update-the-auto-increment-to-the-next-value-from-the-table}

>[!WARNING]
>
>Perform a database backup before alterating tables. Also consider putting the site into [maintenance mode](https://experienceleague.adobe.com/docs/commerce-operations/configuration-guide/setup/application-modes.html#maintenance-mode).

If the value shown is lower than `max int(11) [ 4294967296 ]` as shown in the below example terminal output, than a table `[ AUTO_INCREMENT ]` has changed to a number bigger or equal to the `max [ int(11) ]` value. 

```mariadb
MariaDB [xxx]> SELECT MAX(value_id) FROM catalog_product_entity_int;
+---------------------+
| MAX(source_item_id) |
+---------------------+
|          4283174130 |
+---------------------+
```

To check if this has occured run the following command in the terminal:

```
MariaDB [xxx]> show create table catalog_product_entity_int;

...
) ENGINE=InnoDB AUTO_INCREMENT=4294967297 DEFAULT CHARSET=utf8 COMMENT='Catalog Product Integer Attribute Backend Table';
```

As you can see in the above example output the table `[ AUTO_INCREMENT ]` has changed to a bigger number than the `max int(11) [ 4294967296 ]`. The solution is to update the `[ AUTO_INCREMENT]` to the next value from the table:

```
ALTER TABLE catalog_product_entity_int AUTO_INCREMENT = 4283174131;
```

## `INT` to `BIGINT` schema update {#int_to_bigint_schema_update}

However, if when running the following query `SELECT MAX(value_id) FROM catalog_product_entity_int;` the value shown is higher than `max int(11) [ 4294967296 ]`  consider doing a `INT` to `BIGINT` schema update. The datatype `BIGINT` has a larger range of values.

To do so:

1. Create a custom module inside the *app/code/* directory.
1. In the custom module create a *db_schema.xml*. In *db_schema.xml* you will set the datatype to `BIGINT`. 
1. Add the following content and then execute `bin/magento setup:upgrade` to apply the above changes to the corresponding table.

```
<?xml version="1.0"?>
<schema xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:Setup/Declaration/Schema/etc/schema.xsd">
    <table name="catalog_product_entity_int">
        <column xsi:type="bigint" name="value_id" unsigned="false" nullable="false" identity="true"
                comment="Value ID"/>
    </table>
</schema>
```


## Related reading

* [General MySQL guidelines](https://experienceleague.adobe.com/docs/commerce-operations/installation-guide/prerequisites/database-server/mysql.html) in the Commerce Installation Guide.
* [Database upload loses connection to MySQL](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/troubleshooting/database/database-upload-loses-connection-to-mysql.html) in our support knowledge base. 
* [Database best practices for Adobe Commerce on cloud infrastructure](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/best-practices/database/database-best-practices-for-magento-commerce-cloud.html) in our support knowledge base.
* [Most common database issues in Adobe Commerce on cloud infrastructure](https://experienceleague.adobe.com/docs/commerce-knowledge-base/kb/best-practices/database/most-common-database-issues-in-magento-commerce-cloud.html) in our support knowledge base.
