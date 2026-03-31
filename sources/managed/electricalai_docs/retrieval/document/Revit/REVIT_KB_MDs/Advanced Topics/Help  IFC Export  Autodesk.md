---
created: 2026-01-28T21:18:08 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Export_IFC_Export_html
author: 
---

# Help | IFC Export | Autodesk

> ## Excerpt
> Custom IFC Export

---
Custom IFC Export

The Revit API allows custom applications to override the default implementation for the IFC export process.

When an IExporterIFC object is registered with Revit, it will be used both when the user invokes an export to IFC from the UI as well as from the API method Document.Export(String, String, IFCExportOptions). In both cases, if no custom IFC exporter if registered, the default Revit implementation for IFC export is used.

When invoking an IFC export from the API, IFCExportOptions can be used to set the same export options as are available to the user from the Export IFC dialog box.

The functions:

-   IFCImportOptions.GetExtraOptions()
-   IFCImportOptions.SetExtraOptions()

allow for passing in arbitrary options for custom IFC importers. Users can pass in a string to string map specifying extra data they wish to pass for IFC import.

### IExporterIFC

The interface IExporterIFC has only one method to implement, ExportIFC(). This method is invoked by Revit to perform an export to IFC. An ExporterIFC object is passed to this method as one of its parameters. ExporterIFC is the main class provided by Revit to allow implementation of an IFC export. It contains information on the options selected by the user for the export operation, as well as members used to access specific types of data needed to implement the export properly.

The Autodesk.Revit.DB.IFC namespace contains numerous IFC related API classes that can be utilized by a custom implementation of the IFC export process. For a complete sample of a custom IFC export application, see the Open Source example at [http://sourceforge.net/projects/ifcexporter/](http://sourceforge.net/projects/ifcexporter/).
