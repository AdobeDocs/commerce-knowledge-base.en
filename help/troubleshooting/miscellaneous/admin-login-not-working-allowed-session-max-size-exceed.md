---
title: [!DNL Admin] login not working - allowed session max size exceeded
description: This article provides a fix for when you try to log in to your Admin panel and the form refreshes and you are unable to log in.
---

# [!DNL Admin] login not working - allowed session max size exceeded

This article provides a fix for when you try to log in to your Commerce Admin panel but the form just refreshes and you are unable to log in.


## Affected versions

* Adobe Commerce on-premises 2.X.X
* Adobe Commerce on cloud infrastructure 2.X.X

## Issue 

The Admin Session Size has been exceeded.

<u>Steps to reproduce:</u>

1. 
1.

## Solution 

Check the var/log/support_report.log file for errors such as these:

```[2023-07-13T04:26:09.792060+00:00] report.WARNING: Session size of 260572 exceeded allowed session max size of 256000. [] []
[2023-07-13T04:26:17.056714+00:00] report.WARNING: Session size of 260570 exceeded allowed session max size of 256000. [] []```

## Related Reading

[]() in our.

[]() in our .
