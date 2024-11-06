---
title: Find large MySQL tables
description: 'To identify the large tables, connect to the database as described in the [Connect to the database](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/configure/service/mysql#connect-to-the-database) article, and run the following command, where `project_id` is your Cloud project ID:'
exl-id: dc5019bc-ab6c-4568-986f-0a294a0f3ac3
---
# Find large MySQL tables

To identify the large tables, connect to the database as described in the [Connect to the database](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/configure/service/mysql#connect-to-the-database) article, and run the following command, where `project_id` is your Cloud project ID:

```sql
SELECT TABLE_NAME AS `Table`,
  ROUND((DATA_LENGTH + INDEX_LENGTH) / 1024 / 1024) AS `Size (MB)`
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = "<project_id>"
ORDER BY (DATA_LENGTH + INDEX_LENGTH) DESC;
```

This would display the complete list of tables and their size. You can go through the list and identify which tables require attention because of the big size.

## Related reading

[Best practices for modifying database tables](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/development/modifying-core-and-third-party-tables#why-adobe-recommends-avoiding-modifications) in the Commerce Implementation Playbook
