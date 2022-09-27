---
description: This is an article to test ExL Markdown syntax and it's conversion to Zendesk HTML.
labels: 2.2.x,2.3.x,Magento Commerce,exception,generated,how to,install,installation,var,web setup wizard,Adobe Commerce,cloud infrastructure,on-premises,Magento Open Source
title: ExL Syntax Style Guide
---

# Basic text formatting

Test 2, update Article.

A paragraph requires no special syntax in Markdown. Add a blank line between each paragraph.
To format text as bold, you enclose it in two asterisks:

This text is **bold**.

To format text as italic, you enclose it in a single asterisk:

This text is *italic*.
To format text as both bold and italic, you enclose it in three asterisks:

This is text is both ***bold and italic***.

To ignore Markdown formatting characters, use \ before the character:

This is not \*italicized\* type.

Blockquotes
Our authoring system uses blockquotes syntax (> at the beginning of lines) to identify custom markdown extensions for tips, notes, and videos. You can create actual blockquotes by adding a > character in front of a paragraph.

This is a blockquote quotation.

>This is a blockquote quotation.

Characters to “escape”
Several characters (# { } [ ] < > * + - . !) have a special meaning in Markdown or HTML for creating headings, images, lists, and other components. When you use these characters, the rendering engine thinks you’re adding code. However, in some cases, you want to display these characters in your text. To do that, you need to “escape” the characters. The easiest escape method is to precede the character with a backslash (\). For example, if you want to start a line with a # character so that it’s not interpreted as a heading, you would type \#:

\# This is not a heading.

The backslash works only with these characters: # { } [ ] * + - . !. If you need to escape characters such as angle brackets (such as &lt;yourname&gt;), you can either enclose the text in back ticks to apply an inline code block, or use the HTML entity code instead of the character. Examples of common HTML codes:

&lt; (<)
&gt; (>)
&amp; (&)
&Hat; (^)
&mdash; (—)
&ndash; (–)

This is `inline code` within a paragraph of text.

```Use a back tick (`) for formatting```

```javascript
var visitor = Visitor.getInstance("INSERT-MARKETING-CLOUD-ORGANIZATION ID-HERE", {
     trackingServer: "INSERT-TRACKING-SERVER-HERE", // same as s.trackingServer
     trackingServerSecure: "INSERT-SECURE-TRACKING-SERVER-HERE", // same as s.trackingServerSecure

     // To enable CNAME support, add the following configuration variables
     // If you are not using CNAME, DO NOT include these variables
     marketingCloudServer: "INSERT-TRACKING-SERVER-HERE",
     marketingCloudServerSecure: "INSERT-SECURE-TRACKING-SERVER-HERE" // same as s.trackingServerSecure
});
```

Example with line numbers (```html {.line-numbers}):

```html {.line-numbers}
<!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html>
```
Definition Lists
For definition lists, we do not yet support standard Markdown syntax. Instead, use manual formatting such as this:

**Frog** - An amphibious green creature. Likes flies.

Download Files
Upload the .zip or other downloadable file to the assets directory, and then link to it. If it’s a .zip file, clicking the link will download the file. If it’s file type such as PDF or PNG that can be opened in a browser, clicking the link will open a new tab. For such files, consider zipping them or providing instructions to right-click the link and download.

Download [download-test.zip](/docs/authoring-guide-exl/assets/download-test.zip?lang=en)

# This is level 1 (article title)

## This is level 2

### This is level 3

Heading IDs

Heading IDs (also called anchor IDs) are used to create custom deep links to sections within articles. To specify a heading ID, use this format:

## Creating processing rules {#processing-rules}

Images
Use the ![]() syntax for images. The brackets [ ] include alt text, and the parentheses ( ) include the image location and optional hover text (tooltip). The exclamation mark distinguishes an image from a link.

![alt text](/docs/authoring-guide-exl/assets/logo.png "Hover text")

![Dive image alt text](/docs/authoring-guide-exl/assets/maui-dive.jpg "Hover text - Maui dive width is 300 pixels and centered"){width="300" align="center"}

Links and Cross-References
External links are straight-forward and can be rendered as a linked caption or a pure URL.

[Adobe](https://www.adobe.com)

https://www.adobe.com

<https://www.adobe.com>

Option 1: Standard relative link

Here’s what a standard relative link looks like:

See [Overview example article](collaborative-doc-instructions/overview.md)

Deep linking

To link to a heading within an article, the target heading must have an explicit heading ID (also called an “anchor ID”). Example:

## Creating audience segments {#creating-audience-segments}

To link to this heading within the same page, use the heading ID as the link:

See [Creating audience segments](#creating-audience-segments)

To link to this heading from a different article in the repo, add the heading ID suffix to the end of the link:

See [Audiences: Creating audience segments](audiences.md#creating-audience-segments)

Open in new tab

If you want a link to open a new tab, such as when you jump to a different guide, use the {target="_blank"} property in the link.

Example:

[See What's new](/docs/authoring-guide-exl/using/whats-new.html?lang=en){target="_blank"}

Image Links
If you want to allow users to click an image to jump to a different page, use this format.

Syntax

[![image](/docs/authoring-guide-exl/assets/core-services_96.png?lang=en)](https://www.adobe.com)

To create numbered lists, begin a line with 1. or 1), but pick one method and use it consistently within the article. You don’t need to specify the numbers. GitHub does that for you.

Use the number 1 for every step in the numbered list.

Add blank lines before and after lists.

Syntax

1. This is step 1.

1. This is the next step.

   1. This is a sub-step

   1. This is a sub-step

1. This is yet another step, the third.

Best practice: Use * for bullets. Visual Studio Code applies the asterisk for bullets, so it’s easier to stay with asterisks to automate creating an unordered list. (You might have noticed that the TOC.md file uses plus signs + for lists. That’s a holdover from migration. Any valid bullet character would work as long as it’s consistent within the article.)

Syntax

* First item in an unordered list.
* Another item.
* Here we go again.

You can also embed lists within lists and add content between list items. Indent content between list items to avoid starting a new list. Items between steps should be indented to the start of the text—3 spaces for numbered lists, 2 spaces for bullet lists.

1. Set up your table and code blocks.
2. Perform this step.

   ![screen](/docs/authoring-guide-exl/assets/core-services_96.png?lang=en)

3. Make sure that your table looks like this:

   | Hello | World |
   |---|---|
   | How | are you? |

4. This is the fourth step.

   >[!NOTE]
   >
   >This is note text.

5. Do another step.

   This is an indented line.

Collapsible sections
You can create a collapsible section (sometimes called an accordion) that is hidden by default. The user can click the title to expand or collapse the section.

Collapsible text can be used to simplify complex content, such as streamlining an FAQ page or de-cluttering a complex procedure with nested lists. For example, instead of displaying a set of sub-steps, you can collapse the sub-steps into a “View details” section.

Syntax

+++Click me
This is text inside a collapsible section.

* Bullet one
* Bullet two
* Bullet three

+++

Tables
Tables are problematic in Markdown. When tables are migrated from the previous authoring system, simple tables (one line per cell) are formatted as native Markdown tables (preferred). More advanced tables are formatted as HTML.

| Header | Another header | Yet another header |
|--- |--- |--- |
| row 1 | row 1 column 2 | row 1 column 3 |
| row 2 | row 2 column 2 | row 2 column 3 |

Simple tables work adequately in Markdown. However, tables that include multiple paragraphs or lists within a cell are difficult to work with. For such content, we recommend using a different format, such as headings & text.

Markdown table with paragraph breaks and lists

| Header | Another header | Yet another header |
|------------|----------|----------------|
| row 1 | first paragraph in cell<p>second paragraph in cell(`<p>`)<br>line break (`br`) | row 1 column 3 |
| row 2 | bullet list<ul><li>item 1</li><li>item 2</li><li>item 3</li></ul> | row 2 column 3 |

Markdown table with line breaks and fake list

Workaround with manual bullets.

| Color | Things to Do |
|--- |--- |
| Red | * Read <br> * Write <br> * Study |
| Blue | * Swim <br> * Run <br> * Lift <br> **Note**: Remember to train smart.|

Extended Markdown Components
We need to extend Markdown to support items that aren’t included in common Markdown.

Special components are declared in a containing block quote using square brackets and an exclamation mark plus the reference for the type of block it is. For example, here’s how to declare a note:

>[!NOTE]
>
>This is a note.

Syntax

>[!TIP]
>
>This is a standard tip.

>[!WARNING]
>
>This is a standard warning block.

>[!IMPORTANT]
>
>This is a standard important block.

>[!NOTE]
>
>This is a standard NOTE block.
>
>It includes multiple paragraphs.

>[!VIDEO](https://video.tv.adobe.com/v/29770/?quality=12)

More Like This
Use the “More Like This” component to display related links at the end of an article. When rendered, the Related Articles component is rendered as “Related Articles” (and localized in other languages).