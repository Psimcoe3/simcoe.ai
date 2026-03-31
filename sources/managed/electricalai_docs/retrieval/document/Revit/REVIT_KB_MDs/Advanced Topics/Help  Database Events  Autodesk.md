---
created: 2026-01-28T21:17:34 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Events_Database_Events_html
author: 
---

# Help | Database Events | Autodesk

> ## Excerpt
> The following table lists database events, their type and whether they are available at the application and/or document level:

---
The following table lists database events, their type and whether they are available at the application and/or document level:

**Table 53: DB Event Types**

<table summary="" id="GUID-BB901E53-61FD-4D4A-8571-3CC6582DA85A__TABLE_DF9946D275D04F2785B0ED6712065C42"><tbody><tr><td><b>Event</b></td><td><b>Type</b></td><td><b>Application</b></td><td><b>Document</b></td></tr><tr><td><a href="https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Events_Database_Events_DocumentChanged_event_html" data-url="https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/files/Revit_API_Developers_Guide/Advanced_Topics/Events/Database_Events/Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Events_Database_Events_DocumentChanged_event_html.html">DocumentChanged event</a></td><td>single</td><td>X</td><td></td></tr><tr><td>DocumentClosing</td><td>pre</td><td>X</td><td>X</td></tr><tr><td>DocumentClosed</td><td>post</td><td>X</td><td></td></tr><tr><td>DocumentCreating</td><td>pre</td><td>X</td><td></td></tr><tr><td>DocumentCreated</td><td>post</td><td>X</td><td></td></tr><tr><td>DocumentOpening</td><td>pre</td><td>X</td><td></td></tr><tr><td>DocumentOpened</td><td>post</td><td>X</td><td></td></tr><tr><td>DocumentPrinting</td><td>pre</td><td>X</td><td>X</td></tr><tr><td>DocumentPrinted</td><td>post</td><td>X</td><td>X</td></tr><tr><td>DocumentSaving</td><td>pre</td><td>X</td><td>X</td></tr><tr><td>DocumentSaved</td><td>post</td><td>X</td><td>X</td></tr><tr><td>DocumentSavingAs</td><td>pre</td><td>X</td><td>X</td></tr><tr><td>DocumentSavedAs</td><td>post</td><td>X</td><td>X</td></tr><tr><td>DocumentSynchronizingWithCentral</td><td>pre</td><td>X</td><td></td></tr><tr><td>DocumentSynchronizedWithCentral</td><td>post</td><td>X</td><td></td></tr><tr><td>FailuresProcessing</td><td>single</td><td>X</td><td></td></tr><tr><td>FileExporting</td><td>pre</td><td>X</td><td></td></tr><tr><td>FileExported</td><td>post</td><td>X</td><td></td></tr><tr><td>FileImporting</td><td>pre</td><td>X</td><td></td></tr><tr><td>FileImported</td><td>post</td><td>X</td><td></td></tr><tr><td>ProgressChanged</td><td>single</td><td>X</td><td>&nbsp;</td></tr><tr><td>ViewPrinting</td><td>pre</td><td>X</td><td>X</td></tr><tr><td>ViewPrinted</td><td>post</td><td>X</td><td>X</td></tr></tbody></table>

-   DocumentChanged - notification when a transaction is committed, undone or redone
-   DocumentClosing - notification when Revit is about to close a document
-   DocumentClosed - notification just after Revit has closed a document
-   DocumentCreating - notification when Revit is about to create a new document
-   DocumentCreated - notification when Revit has finished creating a new document
-   DocumentOpening - notification when Revit is about to open a document
-   DocumentOpened - notification after Revit has opened a document
-   DocumentPrinting - notification when Revit is about to print a view or ViewSet of the document
-   DocumentPrinted - notification just after Revit has printed a view or ViewSet of the document
-   DocumentSaving - notification when Revit is about to save the document
-   DocumentSaved - notification just after Revit has saved the document
-   DocumentSavingAs - notification when Revit is about to save the document with a new name
-   DocumentSavedAs - notification when Revit has just saved the document with a new name
-   DocumentSynchronizingWithCentral - notification when Revit is about to synchronize a document with the central file
-   DocumentSynchronizedWithCentral - notification just after Revit has synchronized a document with the central file
-   FailuresProcessing - notification when Revit is processing failures at the end of a transaction
-   FileExporting - notification when Revit is about to export to a file format supported by the API
-   FileExported - notification after Revit has exported to a file format supported by the API
-   FileImporting - notification when Revit is about to import a file format supported by the API
-   FileImported - notification after Revit has imported a file format supported by the API
-   ProgressChanged - notification when an operation in Revit has progress bar data
-   ViewPrinting - notification when Revit is about to print a view of the document
-   ViewPrinted - notification just after Revit has printed a view of the document
