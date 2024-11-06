---
title: Resolving UTF-8 errors for CSV file uploads
description: This article provides a fix for when you receive the error message "CSV files must use UTF-8 encoding." This error message means that the file you're trying to upload contains illegal characters, or characters that aren't allowed. While UTF-8 encoding allows for [the majority of characters](https://www.fileformat.info/info/charset/UTF-8/list.htm), some aren't compatible with Magento BI.
exl-id: 88d8e0b8-152e-4a6d-bc44-3b285e0eb0c3
feature: Data Import/Export
role: Developer
---
# Resolving UTF-8 errors for CSV file uploads

This article provides a fix for when you receive the error message "CSV files must use UTF-8 encoding." This error message means that the file you're trying to upload contains illegal characters, or characters that aren't allowed. While UTF-8 encoding allows for [the majority of characters](https://www.fileformat.info/info/charset/UTF-8/list.htm), some aren't compatible with Magento BI.

To fix the problem, you'll need to change the encoding of the file. Re-saving the file with the proper encoding typically resolves the issue, but be aware that you may lose some information (for example, the illegal characters may be dropped) when doing this.

We recommend using [Sublime Text](https://www.sublimetext.com/2) to save and encode the file.

1. Open your file in Microsoft Excel, Google Docs, Apple Numbers, or your program of choice.
1. Click ​​ **File** > **Save as** ​​ and choose the ​​ **Comma separated values (.csv)** format to save the file.
1. Open the CSV file in Sublime Text.
1. In Sublime Text, navigate to ​​ **File** > **Save with Encoding** > **UTF-8\*​** . This will save the CSV file with UTF-8 encoding.    ![csv_file_UTF-8_sublime_3.2.2_magento_BI.png](assets/csv_file_UTF-8_sublime_3.2.2_magento_BI.png)
1. [Upload the data](https://experienceleague.adobe.com/en/docs/commerce-business-intelligence/mbi/analyze/connecting/using-file-uploader) (in our user guide) to a new table in Magento BI.
