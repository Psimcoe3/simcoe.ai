---
created: 2026-01-28T21:27:02 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Appendices_API_User_Interface_Guidelines_Dialog_Guidelines_html
author: 
---

# Help | Dialog Guidelines | Autodesk

> ## Excerpt
> A dialog is a separate controllable area of the application that contains information and/or controls for editing information. Dialogs are the primary vehicle for obtaining input from and presenting information to the user. Use the following guidelines when deciding which dialog to use.

---
A dialog is a separate controllable area of the application that contains information and/or controls for editing information. Dialogs are the primary vehicle for obtaining input from and presenting information to the user. Use the following guidelines when deciding which dialog to use.

<table summary=""><tbody><tr><td><b>Dialog Type</b></td><td><b>Definition</b></td><td><b>Use When</b></td></tr><tr><td>Modal</td><td><p>Halts the rest of the application and waits for user input</p></td><td><ul><li>Task(s) in the dialog are infrequent</li><li>It is acceptable to halt the system while the user enters data</li><ul></ul></ul></td></tr><tr><td>Modeless</td><td><p>User can switch between the dialog and the rest of the application without closing the dialog</p></td><td><ul><li>Task(s) in the dialog are frequent</li><li>Halting the system would interrupt the user workflow</li></ul></td></tr></tbody></table>

## Behavior Rules

-   A dialog can either be user initiated (prompted by clicking a control) or system initiated (a warning triggered by a system event)
-   The initial dialog location typically should be centered on the screen, but this rule may vary based on variation or on a particular context of use, but should have an immediate focus
-   Dialogs should be resizable when the content is dynamic, please see Dynamic Layout section below for more on this topic

## Dialog Controls

<table summary=""><tbody><tr><td><b>Control</b></td><td><b>Use When</b></td><td><b>Example</b></td></tr><tr><td><a href="https://docs.microsoft.com/en-us/windows/win32/uxguide/guidelines" target="_blank">CHECK BOX</a></td><td>The choice being made (and its opposite) can be clearly expressed to the user with a single label</td><td><img src="https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-94C50DE2-A8B4-45D6-8A09-AAD500A68A24-low.png">The opposite of enable is disable</td></tr><tr><td><a href="https://docs.microsoft.com/en-us/windows/win32/uxguide/guidelines" target="_blank">RADIO BUTTON</a></td><td>There are between 2 - 5 mutually exclusive but related choices and the user can only make one selection per choice</td><td><img src="https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-D888ACBB-EB8D-4D2C-B245-8A46EA1B5C9E-low.png"></td></tr><tr><td><a href="https://docs.microsoft.com/en-us/windows/win32/uxguide/guidelines" target="_blank">TEXT BOX</a></td><td>This choice requires manually entering a numerical text value</td><td>&nbsp;</td></tr><tr><td><a href="https://docs.microsoft.com/en-us/windows/win32/uxguide/guidelines" target="_blank">DROP DOWN LIST</a></td><td>Select from a list of mutually exclusive choices<p>It is appropriate to hide the rest of the choices and only show the default selection</p><p>Also, use this instead of radio buttons when there are more than four choices or if real estate is limited</p></td><td><img src="https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-62972525-BF49-4001-9244-4E104432F5D4-low.png"></td></tr><tr><td><a href="https://docs.microsoft.com/en-us/windows/win32/uxguide/guidelines" target="_blank">COMBO BOX</a></td><td>Similar to a drop-down list box, but allows the user to enter information not pre-populated in the drop-down</td><td><img src="https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-39969C8D-6F22-40F5-829F-0C3AB32C2AAA-low.png"></td></tr><tr><td><a href="https://docs.microsoft.com/en-us/windows/win32/uxguide/guidelines" target="_blank">SLIDER</a></td><td>Use when the expected input or existing data will be in a specific range.<p>Sliders can also be combined with text boxes to give additional level of user control and give feedback as the slider is moved</p></td><td><img src="https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-4CCA1FD6-516A-473E-95D6-C4D1EA7A23C6-low.png"></td></tr><tr><td><a href="https://docs.microsoft.com/en-us/windows/win32/uxguide/guidelines" target="_blank">SPINNER</a></td><td>Use this option if the data can be entered sequentially and has a logical limit. This can be used in conjunction with an editable text box</td><td><img src="https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-28E819AC-706D-442F-ABF0-A45BE3855561-low.png"></td></tr></tbody></table>

## Laying Out a Dialog

### Basic Elements

Every dialog contains the following elements:

<table summary=""><tbody><tr><td></td><td>Element</td><td>Requirements</td><td>Illustration</td></tr><tr><td>1</td><td><i>Title bar</i></td><td>Title bars text describes the contents of the window.</td><td><img src="https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-98821925-59A4-4A1C-AAD7-5665C0025C3D-low.png"></td></tr><tr><td>2</td><td><i>Help button</i></td><td>A button in the title bar next to the close button.<ul><li>Help button is optional - use only when a relevant section is available in the documentation</li><li>Note that many legacy dialogs in Revit still have the Help button located in the bottom right of the dialog</li></ul></td></tr><tr><td>3</td><td><i>Controls</i></td><td>The bulk of a dialog consists of controls used to change settings and/or interact with data within an application. The layout of the controls should follow the Layout Flow, Spacing and Margins, Grouping and Dialog Controls sections outlined below.<p>When an action control interacts with another control, such as a text box with a Browse button, denote the relationship by placing the <em>RELATED</em> controls in one of three places:</p><ul><li>To the right of and top-aligned with the other control</li><li>Below and left-aligned with the other control. See Content Editor</li><li>Vertically centered between related controls. See List Builder</li><ul></ul></ul></td></tr><tr><td>4</td><td><i>Commit Buttons</i></td><td>See the Committing Changes section. The most frequently-used Commit buttons include:<ul><li>OK</li><li>Cancel</li><li>Yes</li><li>No</li><li>Retry</li><li>Close</li></ul></td></tr></tbody></table>

### Layout Flow

When viewing a dialog within a user interface, the user has multiple tasks to accomplish. How the information is designed and laid out must support the user in accomplishing their task(s). Keeping this in mind, it is important to remember users:

-   Scan (not read) an interface and then stop when they get to what they were looking for and ignore anything beyond it
-   Focus on items that are different
-   Not scroll unless they need to

Lay out the window in such a way that suggests and prompts a "path" with a beginning, middle, and end. This path should be designed to be easily scanned. The information and controls in the "middle" of the path must be designed to be well balanced and clearly delineate the relationship between controls. Of course, not all users follow a strictly linear path when completing a task. The path is intended for a typical task flow.

<table summary=""><tbody><tr><td><i>Variation A: Top-Down</i><p><i>Place UI items that:</i></p><ol><li>Initiate a task in the upper-left corner or upper-center</li><li>User must interact with to complete the task(s) in the middle</li><li>Complete the task(s) in the lower-right corner</li></ol><p>In this example (Materials dialog), the user does the following:</p><ol><li>Searches/filters the list</li><li>Selects an item</li><li>Commits or Cancels</li></ol><p><i>Variation B: Left-Right</i></p><p><i>Place UI items that:</i></p><ol><li>Initiate a task or change between modes in the far left</li><li>User must interact with to complete the task(s) in the middle. This may be separated into separate distinct sections</li><li>Complete the task(s) in the lower-right corner</li></ol></td><td><img src="https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-DC6DB2A2-0FE1-4A08-BD09-AFDE9E809FA5-low.png"><b>Figure 198 - Materials dialog</b></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-41A781E3-F25B-45D7-BD1E-85F4E73896D4-low.png)

**Figure 199 - Revit File Open dialog**

Note: A top-down flow can also be used within this dialog, if they user is browsing the file hierarchy instead of the shortcuts on the far left.

### Variation C: Hybrid

As seen in Variation B, many windows that are laid out left to right are actually a hybrid of left-right and top-down.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-F0FB138A-47F1-473D-9190-6859D7232081-low.png)

**Figure 200 - Revit Filters dialog**

In this example (Revit Filters), the three primary tasks are grouped into columns, delineated by the group boxes: Filters, Categories and Filter Rules. Each of these columns contains a top-down flow that involves selecting from a collection of items or modifying a control.

### Spacing and Margins

The following table lists the recommended spacing between common UI elements (for 9 pt. Segoe UI at 96 dpi). For a definition of the difference between dialog units (DLU) and relative pixels.

### Spacing and Margins Table

### Grouping

Group boxes are the most common solution used to explicitly group related controls together in a dialog and give them a common grouping.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-AFEDF3C3-84A5-492B-A012-8AB277C296AD-low.png)

**Figure 201 - Group box within a standard Print dialog**

A group box should include:

-   Two or more related controls
-   Exists with at least one other group box
-   A label that:
    -   describes the group
    -   follows sentence style
    -   is in the form of a noun or noun phrase
    -   does not use ending punctuation
-   A Spacing and Margins section describes spacing rules

### Poor Examples- What Not to Use

The following are examples of what _should not_ be done:

Group boxes without a label or a group box with only one control.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-5BA9EFCF-ED89-4072-A6B4-CA192BF2CC23-low.png) One group box in a dialog.

The (Materials) single group box title is redundant with the dialog title and can be removed.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-05F93841-DC17-4768-AF02-35F38344F213-low.png)

**Figure 202 - Group box with no label and group box with one control and Group box with title that is redundant with dialog title**

Avoid "nesting" two of more group boxes within one another and placing Commit buttons inside a group box.

### Horizontal Separator

An alternative to the traditional group box is a horizontal separator. Use this only when the groups are stacked vertically in a single column.

The following example is from Microsoft Outlook 2007:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-BF491B40-6BCC-4C43-96FA-45210F6EA14C-low.png)

**Figure 203 - Horizontal separators in Microsoft Outlook 2007**

Spacing between the last control in the previous group and the next grouping line should be 12 DLUs (18 relative pixels).

### Dynamic Layout

Content that is presented on different types or sizes of display devices usually requires the ability to adapt to the form that it is displayed in. Using a dynamic layout can help when environment changes such as localizing to other languages, changing the font size of content, and for allowing user to manually expand the window to see more information.

To create a dynamic layout:

-   Treat the content of the window as dynamic and expand to fill the shape of its container unless constrained.
-   Add a resizing grip to the bottom right corner of the dialog.
-   The dialog should not be resizable to a size smaller than the default size.
-   The user defined size should be remembered within and between application sessions.
-   Elements in the dialog should maintain alignment during resizing based on the quadrant they are described in the following table:

<table summary=""><tbody><tr><td><b>Home Quadrant</b></td><td><b>Alignment</b></td></tr><tr><td>1</td><td>Left and Top</td></tr><tr><td>2</td><td>Right and Top</td></tr><tr><td>3</td><td>Left and Bottom</td></tr><tr><td>4</td><td>Right and Bottom</td></tr><tr><td>Multiple</td><td>If control is located in multiple quadrants, it should anchor to quadrant 1 and/or 3 (to the left) and expand/contract to the right to maintain alignments</td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-AFE57269-96AF-464A-9D7A-BF3DC68BFAF5-low.png)

**Figure 204 - Four square grid applied to Revit View Templates dialog to demonstrate how it should be resized**

In this example, the list box is located in all four quadrants. So, it is anchored to the top-left and expands to the right and to the bottom.

### Implementation Notes

Here are the some steps to consider when implementing a dynamic layout:

-   Break the design on sections based on the structure of the content and flow you would like to achieve when container's size changes.
-   Define the minimum, maximum and other size constrains for the various sections and control used. This is usually driven by the purpose of the data type we are presenting, images, supplemental information and controls.
-   Consider alignment, that is, how the content will flow when re-sized. Consider which items should be static and which dynamic and how they are expandable - which should usually be for left-to-right languages, and dialogs should flow to the right and bottom, being anchored and aligned to the top and left.

For guidelines on how different controls should handle resizing, see the table below:

<table summary=""><tbody><tr><td><b>Control</b></td><td><b>Content</b></td><td><b>Re-sizable</b></td><td><b>Moveable</b></td></tr><tr><td><i>Button</i></td><td>Static</td><td>No</td><td>Yes</td></tr><tr><td><i>Link</i></td><td>Static</td><td>No</td><td>Yes</td></tr><tr><td><i>Radio Button</i></td><td>Static</td><td>No</td><td>Yes</td></tr><tr><td><i>Spin Control</i></td><td>Static</td><td>No</td><td>Yes, based on the element to which it is attached</td></tr><tr><td><i>Slider</i></td><td>Static</td><td>X Direction</td><td>Yes</td></tr><tr><td><i>Scroll Bar</i></td><td>Static</td><td>X Direction</td><td>Yes</td></tr><tr><td><i>Tab</i></td><td>Dynamic</td><td>X and Y Direction</td><td>Yes, but not smaller then the biggest control contained</td></tr><tr><td><i>Progressive Disclosure</i></td><td>Dynamic</td><td>X and Y Direction</td><td>Yes, but not smaller then the biggest control contained</td></tr><tr><td><i>Check Box</i></td><td>Static</td><td>No</td><td>Yes</td></tr><tr><td><i>Drop-Down List</i></td><td>Dynamic</td><td>X Direction</td><td>Yes but not smaller then the biggest text contained.</td></tr><tr><td><i>Combo Box</i></td><td>Dynamic</td><td>X and Y Direction</td><td>Yes, but not smaller then the biggest text contained</td></tr><tr><td><i>List View</i></td><td>Dynamic</td><td>X and Y Direction</td><td>Yes, but not smaller then the biggest text contained</td></tr><tr><td><i>Text Box</i></td><td>Dynamic</td><td>X and Y if multi-line</td><td>Yes</td></tr><tr><td><i>Date Time Box</i></td><td>Dynamic</td><td>X Direction</td><td>Yes, but not smaller then the biggest text contained</td></tr><tr><td><i>Tree View</i></td><td>Dynamic</td><td>X and Y Direction</td><td>Yes, but not smaller then the biggest text contained</td></tr><tr><td><i>Canvas</i></td><td>Dynamic</td><td>X and Y Direction</td><td>Yes</td></tr><tr><td><i>Group Box</i></td><td>Dynamic</td><td>X and Y Direction</td><td>Yes, but not smaller then the biggest control contained</td></tr><tr><td><i>Progress Bar</i></td><td>Static</td><td>X</td><td>Yes</td></tr><tr><td><i>Status Bar</i></td><td>Dynamic</td><td>X</td><td>Yes</td></tr><tr><td><i>Table or data grid</i></td><td>Dynamic</td><td>X and Y</td><td>Yes, table columns should grow proportionally in the X direction</td></tr></tbody></table>

## Dialog Types

There are a handful of dialog types that persist throughout the Revit products. Utilizing these standard types helps to drive consistency and leverage users' existing learning and knowledge patterns.

### Standard input dialog

This is the most basic dialog type. This should be used when the user needs to make a number of choices and then perform a discrete operation based on those choices. Controls should follow rules for Grouping, Spacing and Margins, and Layout Flow.

The Revit Export 2D DWF Options dialog is a good example of a Standard Input dialog.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-7F33075B-D86D-4732-B25F-FA678D5AF416-low.png)

**Figure 205 - The Export 2D DWF Options dialog**

### Property Editor

Use when an item's properties need to be modified by the user. To create a property editor, provide a Table View that presents a name/property pair. The property field can be modified by a Text Box, Check Box, Command Button, Drop-Down List, or even a slider.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-2EED135C-B3FD-4556-9590-E4CA9AA08D82-low.png)

**Figure 206 - Property Grid**

### Supported Behaviors

<table summary=""><tbody><tr><td><b>ID</b></td><td><b>Behavior</b></td><td><b>Description</b></td><td><b>Required</b></td></tr><tr><td>1</td><td>Filter</td><td>Filters the list of properties based on specified criteria</td><td>No</td></tr><tr><td>2</td><td>Grouping</td><td>Grouping the properties makes them easier to scan</td><td>No</td></tr><tr><td>3</td><td>Controls (Edit properties of an item)</td><td>Each value cell can contain a control that can be edited (or disabled) depending on the context</td><td>Yes</td></tr><tr><td>4</td><td>Commit (Buttons)</td><td>Optional, only use if within a modal dialog</td><td>No</td></tr></tbody></table>

### Content Editor

If multiple action controls interoperate with the same content control (such as a list box), vertically stack them to the right of and top-aligned with the content control, or horizontally place them left-aligned under the content control. This layout decision is at the developer's discretion.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-169AC0FE-B618-49BF-B103-0BBA071B0865-low.png)

**Figure 207 - Action controls to the right of content and action controls below content**

### Collection Viewer

In applications such as Revit, the user must view and manage collections of items to complete their tasks. The Collection View provides the user a variety of ways of viewing the items (browsing, searching and filtering) in the collection. Provide a way for a user to easily browse through a collection of items for the purpose of selecting an item to view or edit. Optionally provide the ability to search and/or filter the collection.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-EF5D3804-34F2-48B4-9D3D-AB77D99E8AD2-low.png)

**Figure 208 - Materials dialog from Revit**

The example above shows Collection Viewer represented as a List. Table View and Tree View are also options for displaying the collection items.

### Supported Behaviors

<table summary=""><tbody><tr><td></td><td><b>Action</b></td><td><b>Description</b></td><td><b>Required</b></td></tr><tr><td><i>1</i></td><td>Filter</td><td>This provides options for filtering the list view. This can be represented as a:<ul><li>Drop down - default criteria must be selected and should include "All" as an option</li><li>Check boxes - check box ON would refine the list. Default set by designer</li><li>Radio buttons - choosing between radio buttons refines the list. Default set by designer Once a choice is selected, the collection will automatically update based on the selected criteria. Controls must follow the <a href="https://docs.microsoft.com/en-us/windows/win32/uxguide/guidelines" target="_blank">Microsoft Windows User Experience Guidelines</a></li></ul></td><td>No</td></tr><tr><td><i>2</i></td><td>Search Box</td><td>A search box allows users to perform a keyword search on a collection. The search box must follow <a href="http://https//docs.microsoft.com/en-us/windows/win32/uxguide/guidelines%3C/a%3E%0A%0A%3C/td%3E%0A%0A%3Ctd%20class=" entry="" target="_blank">No</a></td></tr><tr><td><i>3</i></td><td>Change viewing mode</td><td>If the collection is viewed as list, the items can be optionally displayed with small or large icons instead of text</td><td>No</td></tr><tr><td><i>4</i></td><td>Collection Manager</td><td><ul><li>A separate UI will be provided to edit, rename, delete or add items to the collection.</li><li>This is only displayed if managing the collection is user-editable</li></ul></td><td>No</td></tr><tr><td><i>5</i></td><td>View the collection</td><td>The collection itself can be viewed in the following ways: List View, Table View, Tree View, or as a Tree Table</td><td>Yes</td></tr><tr><td><i>6</i></td><td>Show More</td><td>This button hides/shows the additional data associated with the currently selected item.</td><td>No</td></tr></tbody></table>

### List View

When the user needs to view and browse and optionally select, sort, group, filter, or search a flat collection of items. If the list is hierarchical, use Tree View or Tree Table and if the data is grouped into two or more columns, use Table View instead.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-697A36A7-DE63-42CB-B7A0-90BFC4866437-low.png)

**Figure 209 - List View, showing different ways of presenting the data**

There are four basic variations of this pattern that includes the following:

### Drop down list

Use a drop down list box when you only need to present a flat list of names, only a single selection is required and space is limited. The [Microsoft Windows User Experience Guidelines](https://docs.microsoft.com/en-us/windows/win32/uxguide/guidelines) should be followed when using a drop-down list.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-C3350684-6B66-4AC7-86A3-ED6B9E8EC2B7-low.png)

**Figure 210 - Drop-down list**

### Combo box

Use a combo box when you want the functionality of the drop-down list box but also need to the ability to edit the drop-down list box. The [Microsoft Windows User Experience Guidelines](https://docs.microsoft.com/en-us/windows/win32/uxguide/guidelines) should be followed when using this option, including for how to decide between drop-down and combo box.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-3F73CE12-6BAC-4D2C-AA89-69ADD09CF4C4-low.png)

**Figure 211 - The font selector in Microsoft Office 2007 is an example of a combo box**

### List box

Use when you only need to present a - list of names, it benefits the user to see all items and when there is sufficient room on the UI to display list box. Use also if selecting more than one option is required. The [Microsoft Windows User Experience Guidelines](https://docs.microsoft.com/en-us/windows/win32/uxguide/guidelines) should be followed when using a list box.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-1C925E89-561F-40EB-BEDA-364AEE19A347-low.png)

**Figure 212 - List box**

### List View

Use when the data includes the option of list, details and/or graphical thumbnail previews, such as a Windows Open Dialog.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-2DF324AA-2EDF-4718-8871-811E6A3EB58F-low.png)

**Figure 213 - List view**

### Table View

Users often need to view the contents of a collection so that they can easily comprehend and compare the attributes of many items at once. To accommodate this, present the user with a table that is formatted in such a way that is conducive to scanning.

### Examples

Good Example - The following is an example of a well-formatted table.

Note: The header cells are differentiated from the data cells and the alignment differs to makes it easier to scan the data.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-45FEF9F8-9C05-4F41-A254-3110B8B56536-low.png) **Figure 214 - Good table example**

Poor Example - The following is an example of a poorly formatted table.

Note: The header cells are not differentiated from the data cells and the alignment makes it difficult to scan the data.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-49A8581F-8488-4293-8CAA-8F7649AFB34B-low.png)

**Figure 215 - Bad table example**

## Table title and header cells

-   Highlight and bold the table title to differentiate it from the data cells and the header cells
-   For columns that are sort able, clicking the header sorts the collection. To differentiate table rows from each other, a different shade is used as background color for every second row. Keep the difference between the two colors to a minimum to preserve a gentle feeling. The colors should be similar in value and low in saturation - the one should be slightly darker or lighter than the other. It is often seen that one of the two colors is the background color of the page itself
-   Ensure that the colors are different than header and title rows
-   Title and header cells should be in title case

## Columns containing numeric data

-   Right align the column heading\_s\_ for the data column
-   Right (decimal) align data in numeric columns
-   Format the values in percentage columns with percentage signs immediately to the right of the values to ensure that users are aware that the values are percentages

Note: People can easily forget that they are looking at percentages so the redundancy is important here, especially for tables with many values

## Columns containing numerical data

-   Right align the column headings for the data column
-   Right (decimal) align data in financial columns

## Columns with a mix of positive and negative numeric data

Align the data so that decimals align

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-94AC7716-F429-423B-985E-897FC7AFB3F6-low.png)

**Figure 216 - Properly aligned numeric data**

## Columns containing only single letter or control (such as check box)

-   Center the data or check symbol in this column
-   Center the heading for the column

## Columns with text that does not express numbers or dates

-   Left align the column header of the number column
-   Left align the text data
-   Left align data that are not used as numbers like product IDs or registration numbers

## Columns containing dates (treat dates as text)

-   Left align the column header of a date column
-   Left align the dates
-   Include a date format in the column header if you are presenting to an international audience to avoid confusion

## Column Sorter

Use a column sorter when users are viewing a collection (such as a large table), possibly spanning multiple pages, that they must scan for interesting values.

There are several meaningful possibilities for sorting the table and users may be more effective if they can dynamically change the column that is used for sorting the values on.

-   Allow users to sort a collection of items by clicking on a column header
-   As users click on the column label, the table is sorted by that column
-   Another click reverses the order, which should be visualized using an up or down-wards pointing arrow
-   Make sure it is visible which columns can be clicked on and which one is active now

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-ADA13062-4987-4738-A3ED-558DEC6A4001-low.png)

**Figure 217 - Column sorter**

## Tree View

Often a user may need to understand complex relationships within a hierarchy of items and this can often best displayed within a "tree view." The user may also need to select one or more of the items. If the collection is a flat list, use the List View and if the data is grouped into two or more columns, use Table View or Tree Table instead.

A tree UI follows the principle of user initiated [Progressive Disclosure](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Appendices_API_User_Interface_Guidelines_Progressive_Disclosure_html). Using a tree allows complex hierarchical data to be presented in a simple, yet progressively complex manner. If the data becomes too broad or deep, a search box should be considered.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-CFE0FEE9-B261-4158-8ACF-7054FE01464D-low.png)

**Figure 218 - The Revit Project Browser is a good example of a tree view**

### Tree Table

As with a Tree View, the user may need to view and browse a hierarchically organized collection of items with the intent of selecting one or more of the items. However, the user also needs to see more properties of the item than just the name. To accommodate this, present the user with a tree embedded within a table. Each row presents additional attributes of the item. Expanding a node exposes another row.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-6FCCFB18-1A14-4282-BB1F-1C3D33FF9BAA-low.png)

**Figure 219 - The Revit Visibility/Graphics dialog is a good example of a Tree Table Collection Search / Filter**

When the user is viewing a collection with many items, they may need to filter the number of items. To accomplish this, provide a way for the user choose between either a system-provided list of filter criteria and/or user-creatable criteria. Selecting the criteria automatically filters the collection. The two most common ways are demonstrated in the Revit Materials dialog.

-   A search box allows the list to be filtered based on a keyword
-   A drop-down allows the list to be filtered based on a set of defined criteria

### Collection Editor

In addition to viewing a collection of items, a user will also typically want to edit the collection. This can be accomplished by associating a toolbar for editing, creating, duplicating, renaming, and deleting items.

### The Edit Bar

The buttons should be ordered left to right in the following order and with the following as tooltip labels: Edit, New, Duplicate, Delete, Rename. If a feature does not utilize one or more buttons, the rest move to the left.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-69C3715F-21A5-412E-A315-B5D4D388A990-low.png)

**Figure 220 - The Edit Bar**

<table summary=""><tbody><tr><td></td><td><b>Action</b></td><td><b>Context</b></td></tr><tr><td>1</td><td>Edit</td><td>Use If an item can be edited. Editing an item may launch a separate dialog if there are less than three properties to edit. See the Collection Viewer section for more details on displaying collection items</td></tr><tr><td>2</td><td>New</td><td>Use New if the application is creating a new item</td></tr><tr><td>3</td><td>Duplicate</td><td>Use Duplicate if the feature can only duplicate existing items</td></tr><tr><td>4</td><td>Rename</td><td>Use Rename if the feature allows items to be renamed</td></tr><tr><td>5</td><td>Delete</td><td>Use Delete to remove the feature</td></tr></tbody></table>

To ensure that the primary UI element is placed first in the layout path, the following rules should be followed when placing the manage controls:

-   Navigating list is primary task: place at the bottom-left of the list control
-   Managing list is primary task: place at top left of list control
-   When the main collection being managed is represented as a combo box: place to the right of the combo box

### Add/Remove

A slight variation on the Edit Bar is the use of Add and Remove buttons, denoted by plus and minus icons, as shown below. Add and Remove is used when data is being added to an existing item in the model.

The following is a good example of a Collection Editor dialog that uses both forms of the Edit Bar. The Add (+) and Remove (-) buttons are used to add values to an already existing demand factor type.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-1A366A7F-D630-4776-9CC2-FE3BFFEFA55F-low.png)

**Figure 221 - Demand Factors dialog in Revit MEP 2011**

### List Builder

Use when there is a number of items that the user has to add/remove from one list to another. This is typically used when there is a list (located on the right) that needs to have items added to it from an existing list (located on the left.) Provide a List Box View of the two lists with button controls between, one for adding and the other for removing items.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-1CBF8D65-92D8-4232-A51A-D86F67EF819C-low.png)

**Figure 222 - The Curtain System SDK sample**

### Supported Behaviors

<table summary=""><tbody><tr><td></td><td><b>Action</b></td><td><b>Description</b></td><td><b>Required</b></td></tr><tr><td>1</td><td>Add (to list)</td><td>Takes an item from list A and adds it to list B</td><td>Yes</td></tr><tr><td>2</td><td>Remove (from list)</td><td>Removes item from List B</td><td>Yes</td></tr><tr><td>3</td><td>Collection Editor</td><td>If List A can be managed in this context, use Collection Manager</td><td>No</td></tr></tbody></table>

Depending on the feature, the List Builder can act in one of two ways:

-   Item can only be added once items from List A can only be added to List B once. In this case, the Add button should be disabled when a previously added item is selected in List A.
-   Item can be added multiple times. In this case, the Add button is not disabled, and the user can add an item from List A to List B multiple times (the amount determined by the feature.) See Edit Label example below.

If the user needs to arbitrarily move an item up or down in a collection, provide up/down buttons next to the list.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-D06A743F-C796-4221-AFC2-934EC1001330-low.png)

**Figure 223 - Up/down buttons**

### Task Dialog

Task dialogs are a type of modal dialog. They have a common set of controls that are arranged in a standard order to assure consistent look and feel.

A task dialog is used when the system needs to:

-   provide users with information
-   ask users a question
-   or allow users to select options to perform a command or task

The image below shows a mockup of a task dialog with all possible controls enabled. Most of the controls shown are optional and one would never create a task dialog that had everything on. The mockup below simple illustrates all the parts of a task dialog that could be utilized in one image.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-83114C82-1F0A-4227-92B6-E44075F9EEF1-low.png)

**Figure 224 - A task dialog with all components visible**

Note: This particular task dialog would never happen in a real implementation. Only a small subset would ever be used at one time. Task dialogs cannot display other controls such as, text inputs, list boxes, combo boxes, check boxes, etc. They also only accommodate single step, single action operations; meaning a user may make a single choice and complete the task dialog operation. As a result any dialog that requires such additional controls or multiple steps operations (as with a wizard) are not task dialog candidates. They would need to be implemented as custom dialogs using .NET controls to have a similar look & feel to Task Dialogs. The sections to follow explain when, where and how each task dialog component should be used to be consistent with others in Autodesk products.

#### General Design Principles

These are a few guiding principles that can be applied globally to task dialogs.

When reviewing the contents of a task dialog ask:

-   Does it provide all the information needed to take informed action?
-   Is the information too technical or jargon filled to be understood by the target user?

#### The following points apply to English language versions of product releases

-   Text should be written in sentence format - normal capitalization and punctuation. Titles and command button text are the exceptions, which are written in title format.
    
-   Use a _single space_ after punctuation. For example, DO NOT put two spaces after a period at the end of a sentence. Avoid the use of parentheses to address plurals. Instead, recast sentences. For example: _Write "At least one referenced drawing contains one or more objects that were created in…" instead of "The referenced drawing(s) contains object(s) that were created in …"_
    
-   Include a copyright symbol © after any third party application called out in a task dialog.
    

#### Title (required)

All task dialogs require a title. Titles of task dialogs should be descriptive and as unique as possible. Task dialog titles should take the format of the following:

`<featureName> - <shortTitle>`

-   Where `<featureName>` is the module from which the task dialog was triggered
-   And `<shortTitle>` is the action that resulted in the task dialog being shown
-   Examples:
    -   _Reference Edit - Version Conflict_
    -   _Layer - Delete_
    -   _BOM - Edit Formula_

Where possible, use verbs on the second `<shortTitle>` part of the title such as Create, Delete, Rename, Select, etc.

In cases where there is no obviously applicable feature name (or several) applying a short title alone is sufficient.

A task dialog title should never be the product name, such as AutoCAD Architecture.

#### Title bar Icon

The icon appearing in the far left to the title bar should be that of the host application - this includes third party plug-ins. Task dialogs may contain plug-in names in the title to specify the source of the message, but the visual branding of all task dialogs should match the host application; such as Revit, Inventor, AutoCAD Electrical, etc.

#### Main Instructions (required)

This is the large primary text that appears at the top of a task dialog.

-   Every task dialog should have main instructions of some kind
-   Text should not exceed three lines
-   _**\[English Language Versions\]**_ Main instructions should be written in sentence format - normal capitalization and punctuation
-   _**\[English Language Versions\]**_ Address the user directly as "you"
-   _**\[English Language Versions\]**_ When presented with multiple command link options the standard final line for the main instructions should be, "What do you want to do?"

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-39432A00-72E9-4380-BA1A-D9BD0738D59B-low.png)

**Figure 225 - A very simple task dialog with only main instructions for text**

#### Main Content (optional - commonly used)

This is the smaller text that appears just below the main instructions.

-   Main content is optional. It's primarily used when all the required instructions for a task dialog will not fit in the main instruction area
-   Main content should not simply restate the main instructions in a different way, it should contain additional information that builds upon or reinforces the main instructions
-   _**\[English Language Versions\]**_ Main instructions should be written in sentence format (normal capitalization and punctuation)
-   _**\[English Language Versions\]**_ Address the user directly as "you" when needed

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-F1ABD5AA-BF6E-450F-B8C8-1F7B95FB39EC-low.png)

**Figure 226 - A task dialog that uses both main instructions and main content**

#### Expanded Content (optional - rarely used)

This text is hidden by default and will display at the bottom of the task dialog when the "Show" button is pressed.

-   Expanded content is optional, and should be rarely used. It is used for information that is not essential (advance or additional information), or that doesn't apply to most situations
-   _**\[English Language Versions\]**_ Expanded content should be written in sentence format (normal capitalization and punctuation)
-   _**\[English Language Versions\]**_ Address the user directly as "you" when needed ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-E9AD2AA9-554A-485D-9A41-B8DC079C24F1-low.png)

**Figure 227 - The Show Details button displays additional Main Content text**

#### Main Image (optional - low usage)

Task dialogs support the inclusion of an image to the left of the main instructions. Prior to task dialogs it has been common for most dialogs to have some sort of icon to show that the information it contained was informative, a warning, and error, etc.

Because images were used all the time the value of any image in a dialog was low.

_For Autodesk products the warning icon (exclamation point in a yellow triangle) should only be used in situations where a possible action will be destructive in some way and likely cause loss of data or significant loss of time in rework._

A few examples include:

-   Overwriting a file
-   Saving to an older or different format where data may be lost
-   Permanently deleting data
-   Breaking associations between files through moving or renaming

This is only a partial list. With the exception of such situations _usage of a main image should be avoided_. See Figure 228 for an example of a Task Dialog with a warning icon.

#### "Do not show me again" (DNSM) Checkbox (optional)

Task dialogs support a "Do not show me again" checkbox that can be enabled on dialogs that users can opt to not see in the future. The standard wording for the label on this checkbox for English language versions is:

_"Do not show me this message again"_

Do not is not contracted to "Don't" and there is no punctuation at the end of the line.

For the single action the working should be "Always `<action>`" - for example

-   If the action is "Save current drawing" the checkbox label would read "Always save current drawing"
    
-   If the action is "Convert objects to linework" the checkbox label would read "Always convert objects to linework" ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-CBA6468E-0CBC-432D-ABE7-FFE3CF0FED86-low.png)
    
    **Figure 228 - Example of a task dialog using the DNSMA checkbox as an "Always…" checkbox for one choice**
    

Where multiple are choices possible:

-   The generic wording "_Always perform my current choice_" should be used
-   Command links should be used to show the available choices. If buttons are used and a Cancel button is included it looks as though "cancel" is an option that could always be performed in future

Footer text is used to link to help. It replaces the Help or "?" button found on previous dialogs, and will link to the same location as an existing help link. On English language versions the text in the footer should read:

"Click here to learn more"

The text should be written as a statement in sentence format, but with no final punctuation. See Figure 226 for an example of a Task Dialog with footer text.

#### Progress Bar (optional - rarely used)

In instances where a task dialog is showing progress, or handling of an available option may take several seconds or more a progress bar can be used.

#### Command Links (optional - commonly used)

In task dialogs there are two ways a user can select an action - command links and commit buttons.

Command links are used in the following situations:

-   More than one option is available (avoid situations where only one command link is shown)
-   And a short amount of text would be useful in helping a user determine the best choice

Command links handle scenarios such as:

-   Do A, B, or C
-   Do A or B or A and B
-   Do A or do not do A
-   Etc

Command link text has two parts:

1.  _Main content:_ This is required for any command link. It is one line, written as a statement. For English language versions it is in sentence format without final punctuation.
2.  _Supplemental content:_ This is optional additional text to clarify the main content. For English language versions it is written in normal sentence format with final punctuation.

The first command link (one at the top) is the default action for the task dialog. It should be the most common action or the least potentially damaging action if no choice is substantially more likely than the other for the common use case.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-32141501-5143-48D8-BC64-69E80DF1F606-low.png)

**Figure 229 - A task dialog with two command links**

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-77C728A2-42E1-4FFE-A726-4C6660E5A97D-low.png)

**Figure 230 - Task Dialog with command links and a command button**

#### Commit Buttons (optional - commonly used)

Commit buttons are simple buttons in the footer of the task dialog. Standard (English) terms include:

-   OK
-   Cancel
-   Yes
-   No
-   Retry
-   Close

It is possible to use custom text on commit buttons, but that is not recommended.

Notes on proper usage of each of the primary button types:

-   The OK button should only be used in situations where a task dialog poses a question that can be answered by OK.
-   The Cancel button should only be used when a task can truly be canceled, meaning the action that triggered the task dialog will be aborted and no change will be committed. It can be used in combination with other commit buttons or command links.
-   The Yes & No button(s) should always be used in combination, and the text in the main instructions and / or main content should end in a yes / no question.
-   The Retry button must appear with at least a Cancel button as an alternate option, so a user can choose not to retry.
-   The Close button is used on any purely informational task dialog; i.e. where the user has no action to choose, but can just read the text and close the dialog.Previously the OK button was often used on such dialogs. It _should not_ be used in task dialogs for this purpose.

The following are some examples of how commit buttons should be used:

-   See Figure 226 for an example of a Cancel button with command links
-   See Figure 224 for an example of a purely informative task dialog with a close button
-   See Figure 227 for an example of a task dialog with OK and Cancel buttons

### Default button or link

All tasks dialogs should have a default button or link explicitly assigned. If the task dialog contains an OK button, it should be the default.

Note: The exception is custom task dialogs with command links, which have actions that are equally viable, with none being "better" than the other, should not get assigned a default choice. All dialogs using only commit buttons must be assigned a default button.

## Navigation

### Tabs

Use when there are loosely related, yet distinct "chunks" of information need to exist within the same UI, but there is not enough room to display it all in a clear manner.

Separate the UI into distinct modal zones, each one represented by a "tab" with a descriptive label. The entire dialog should be treated as a single window with a single set of Commit buttons.

-   All of the tabs should be visible at the same time
-   Never have a single tab in a static UI such as dialog. Instead, use the tab's title for the page or dialog. Exception: if the number of tabs grows dynamically and the default is one. e.g. Excel's open workbook tabs
-   Tabs are for navigation only. Selecting a tab should not perform any other action (such as a commit) besides simply switching to that page in the window
-   Avoid nesting tabs within tabbed windows. In this case consider launching a child window
-   Do not change the label on a tab dynamically based on interaction within the parent window

## Variations

### Variation A: Horizontal Tabs

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-DA09BB24-6996-4F9E-835E-EC8DF2749A2A-low.png)

**Figure 231 - Horizontal Tabs**

Avoid more than one row of horizontal tabs. If a second row is needed, consider a vertical tab.

### Variation B: Vertical Tabs

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-AB89C399-FBF3-49A0-ACA2-492E3ADB39D8-low.png)

**Figure 232 - Vertical Tabs**

Vertical tabs are useful:

-   In the Left-to-right Layout Flow
-   If there are enough tabs that would force a second row in a horizontal layout

## Keyboard Accessibility

### Tab Order

Pressing the tab key cycles the focus between each editable control in the dialog. The general rule is left-to-right, top-to-bottom.

1.  The default tab stop is at the control at the topmost, leftmost position in the dialog
2.  Move right until there are no more controls in the current row
3.  Move to the next row and start from the left-most control, moving right
4.  Repeat step 2 until there are no more rows. Always end with the OK/Cancel/Apply row

-   Right and left arrow, down and up arrows, Tab and Shift-tab all have the same behavior, respectively. Except for when the focus is on the following:
    -   List control or combo box: The right/left, down/up arrows move the cursor down/up the list, respectively
    -   Grid control: The right/left move the cursor right/left across columns, And down/up arrows move cursor down/up the list, respectively
    -   Slider: The right/left, down/up arrows move the slider right/left, respectively
    -   Spinner: The right/left, down/up arrows move the spinner down/up, respectively
-   Treat each Group conceptually as a nested dialog, following the above rules within each Group first and moving from the top-left Group, moving to the right until no more groups are encountered and then moving to the next row of Groups.
-   If dialog is tabbed, default tab stop should be the default tab.

Tip: Visual Studio can assist with the creation and editing of tab order by toggling the Tab Order visual helper (accessed from the View![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/ac.menuaro.gif) Tab Order menu.)

### Access Keys

-   Each editable control on a dialog should get a unique access key letter (which is represented by an underlined letter in the control's label)
-   The user presses Alt key plus the assigned key and that control is activated as if it was clicked
-   The default button does not require an access key since Enter is mapped to it
-   The Cancel or Close button also does not need access key since Esc is mapped to it.

### Show More Button

Following the principle of [Progressive Disclosure](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Appendices_API_User_Interface_Guidelines_Progressive_Disclosure_html), users may need a way of showing more data than is presented as a default in the user interface. The Show More button is typically implemented in one of two ways:

_Expander Button_: Provide a button with a label such as " < Preview " or "Show more > " The double brackets > should point towards where the new information pane will be presented. When opened, the double brackets should switch to indicate how the additional pane will be "closed."

See Figure 207 - Materials dialog from Revit for an example.

_Dialog Launcher_: A button with ellipses (…) that launches a separate dialog. This is typically used to provide a separate UI for editing a selected item.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-FC56C88A-82FC-4AD4-AB26-3559FA19BF31-low.png)

**Figure 233 -Dialog launcher button, as implemented in the Revit View Filters dialog**

## Committing Changes

Modal dialogs are used to make changes to data within the project file. Use when there is an editor a series of edits have been queued up in a modal dialog or form and need to be committed at once. If the dialog is purely informational in nature, use a Task Dialog, which has its own committing rules.

Each modal dialog or web-form must have a set of commit buttons for committing the changes and/or canceling the task and/or closing the dialog.

## Sizing

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-7BD704D7-6A41-45C0-9682-0DF01F7A90EB-low.png)

**Figure 234 - Commit Button sizes (taken from Microsoft Windows User Experience Guidelines)**

## Layout

A summary of commit button styles for different window types

<table summary=""><tbody><tr><td><b>Pattern</b></td><td><b>Commit Button style</b></td></tr><tr><td>Modal Dialog</td><td>OK/Cancel or [Action]/Cancel</td></tr><tr><td>Modeless dialog</td><td>Close button on dialog box and title bar</td></tr><tr><td>Progress Indicator</td><td>Use Cancel if returns the environment to its previous state (leaving no side effect); otherwise, use Stop</td></tr></tbody></table>

Commit buttons should follow this layout pattern.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-4E3AD867-2F79-48B7-878F-605767536EFA-low.png)

**Figure 235 - Standard Commit Button layouts**

<table summary=""><tbody><tr><td></td><td><b>Button Type</b></td></tr><tr><td>1</td><td>Default (OK and other Action) buttons</td></tr><tr><td>2</td><td>Cancel or Close Button</td></tr><tr><td>3</td><td>Apply Button</td></tr><tr><td>4</td><td>Dialog buttons (optional)</td></tr></tbody></table>

Position the Default, Cancel, and Apply button(s) in this order and right aligned. The Dialog button(s) (if present) are aligned to the left, but to the right of the help button (if present).

## Default (OK and other Action) buttons

The dialog must have a default action button. This button should be closely mapped to the primary task of the dialog. This can either be labeled OK or a more descriptive verb that describes the action.

-   Make the button with less destructive result to be the Default button
-   Enter key is the keyboard access point for the Default button

## OK button

OK buttons can be used when saving a setting or series of settings. OK button rules:

-   OK button should be used when it is the ONLY action (besides cancel) that can be committed from the dialog. Do not mix OK with other action buttons
-   In modal dialogs, clicking OK means apply the values, perform the task, and close the window Do not use OK buttons to respond to questions
-   Label OK buttons correctly. The OK button should be labeled OK, not Ok or Okay
-   Do not use OK buttons in modeless dialog boxes. Use a action button or Close button

\*

## Action buttons

Action buttons have descriptive verbs that will be defined by the designer. Action button rules:

-   Action buttons can be used to describe more clearly the action that will be taken when clicked
-   One action button must be set as the default. This should be the action most closely mapped to the primary task of the dialog
-   There can be one or more action buttons, but do not mix OK button with action buttons
-   Use Cancel or Close button for negative commit buttons instead of specific responses to the main instruction
-   Otherwise, if user wants to cancel, the negative commit would require more thinking than needed for this particular small task

## Cancel or Close Button

-   Verify the Close button on the title bar has the same effect as Close or Cancel
-   Esc is the keyboard shortcut for Cancel or Close

## Cancel button

-   Cancel button should only be used when a task will be aborted and no change will be committed
-   Clicking the Cancel button means abandon all changes, cancel the task, close the window, and return the environment to its previous state and leaving no side effect
-   For nested choice dialog boxes, clicking the Cancel button in the owner choice dialog typically means any changes made by owned choice dialogs are also abandoned.
-   Don't use Cancel button in modeless dialog boxes. Use Close button instead

## Close Button

-   Use Close button for modeless dialog boxes, as well as modal dialogs that cannot be canceled
-   Clicking Close button means close the dialog box window, leaving any existing side effects

## Apply button (optional)

Apply button will commit any changes made within the dialog on all tabs, pages, or levels within a hierarchy without closing the dialog. Optimally, the user will receive visual feedback of the applied changes. Here are some basic Apply Button rules:

-   In modal or modeless dialogs, clicking Apply means apply the values, perform the task, and do not close the window
-   In modeless dialog use Apply button only on those tasks that require significant or unknown upfront time to be performed, otherwise data change should be applied immediately
-   The Apply button is disabled when no changes have been made. It becomes enabled when changes have been made
-   Clicking cancel will NOT undo any changes that have been already committed with the Apply button
-   Interacting with a child dialog (such as a confirmation) should not cause the Apply function to become enabled
-   Clicking the Apply button after committing a child dialog (such as a confirmation message) will apply all the changes made previous to the action triggering the confirmation

## Dialog Button (optional)

A dialog button performs an action on the dialog itself. Examples include: Reset and Tools for managing Favorites in an Open Dialog. They should be aligned to the far left of the dialog (to the right of the help button if present) and should never be the default.

## Implementation Notes

-   Keyboard Access - each commit button should have a keyboard access key mapped to it. The default button should be mapped to Enter
-   The close button (whether it is Cancel or Close) should be mapped to Esc
-   If Apply exists, and is NOT the default button, it should be mapped to Alt-A
