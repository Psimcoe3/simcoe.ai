---
created: 2026-01-28T21:34:59 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Export_html
author: 
---

# Help | Export | Autodesk

> ## Excerpt
> The Revit API allows for a Revit document, or a portion thereof, to be exported to various formats for use with other software. The Document class has an overloaded Export() method that will initiate an export of a document using the built-in exporter in Revit (when available). For more advanced needs, some types of exports can be customized with a Revit add-in, such as export to IFC and export to Navisworks. (Note, Navisworks export is only available as an add-in exporter).

---
The Revit API allows for a Revit document, or a portion thereof, to be exported to various formats for use with other software. The Document class has an overloaded Export() method that will initiate an export of a document using the built-in exporter in Revit (when available). For more advanced needs, some types of exports can be customized with a Revit add-in, such as export to IFC and export to Navisworks. (Note, Navisworks export is only available as an add-in exporter).

The Document.Export() method overloads are outlined in the table below.

**Table: Document.Export() Methods**

<table summary="" id="GUID-A1BE34A2-DA7C-4C2C-9CCB-958A56F1150D__TABLE_EDA7D7AB3C5944EA8D4A0E634918E5E0"><tbody><tr><td><b>Format</b></td><td><b>Export() parameters</b></td><td><b>Comments</b></td></tr><tr><td>gbXML</td><td>String, String, GBXMLExportOptions</td><td>Exports a gbXML file from a mass model document</td></tr><tr><td>gbXML</td><td>String, String, GBXMLExportOptions</td><td>Exports the document in Green-Building XML format. If EnergyDataSettings is set to use conceptual models, this function cannot be used: instead use the method above.</td></tr><tr><td>IFC</td><td>String, String, IFCExportOptions</td><td>Exports the document to the Industry Standard Classes (IFC) format.</td></tr><tr><td>NWC</td><td>String, String, NavisworksExportOptions</td><td>Exports a Revit project to the Navisworks .nwc format. Note that in order to use this function,you must have a compatible Navisworks exporter add-in registered with your session of Revit.</td></tr><tr><td>DWF</td><td>String, String, ViewSet, DWFExportOptions</td><td>Exports the current view or a selection of views in DWF format.</td></tr><tr><td>DWFX</td><td>String, String, ViewSet, DWFXExportOptions</td><td>Exports the current view or a selection of views in DWFX format.</td></tr><tr><td>FBX</td><td>String, String, ViewSet, FBXExportOptions</td><td>Exports the document in 3D-Studio Max (FBX) format.</td></tr><tr><td>DGN</td><td>String, String, ICollection(ElementId), DGNExportOptions</td><td>Exports a selection of views in DGN format.</td></tr><tr><td>DWG</td><td>String, String, ICollection(ElementId), DWGExportOptions</td><td>Exports a selection of views in DWG format.</td></tr><tr><td>DXF</td><td>String, String, ICollection(ElementId), DXFExportOptions</td><td>Exports a selection of views in DXF format.</td></tr><tr><td>SAT</td><td>String, String, ICollection(ElementId), SATExportOptions</td><td>Exports the current view or a selection of views in SAT format.</td></tr><tr><td>PDF</td><td>String, IList(ElementId), PDFExportOptions</td><td>Exports a selection of views in PDF format.</td></tr></tbody></table>

#### Exporting to gbXML

There are two methods for exporting to the Green Building XML format. The one whose last parameter is GBXMLExportOptions is only available for projects containing one or more instances of Conceptual Mass families. The GBXMLExportOptions object to pass into this method can be constructed with just the ids of the mass zones to analyze in the exported gbXML, or with the mass zone ids and the ids of the masses to use as shading surfaces in the exported gbXML. Whe using masses, they must not have mass floors or mass zones so as not to end up with duplicate surface information in the gbXML output.

The GBXMLExportOptions object used for the other gbXML export option has no settings to specify. It uses all default settings. Note that this method does not generate the energy model. The main energy model must already be stored in the document before this export is invoked.

#### Exporting to IFC

Calling Document.Export() using the IFC option will either use the default Revit IFC export implementation or a custom [IFC Export](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Export_IFC_Export_html), if one has been registered with the current session of Revit. In either case, the IFCExportOptions class is used to set export options such as whether to export IFC standard quantities currently supported by Revit or to allow division of multi-level walls and columns by levels.

#### Exporting to Navisworks

The Export method for Navisworks requires a compatible Navisworks exporter add-in registered with the current Revit session. If there is no compatible exporter registered, the method will throw an exception. Use the OptionalFunctionalityUtils.IsNavisworksExporterAvailable() method to determine if a Navisworks exporter is registered.

The NavisworksExportOptions object can be used to set numerous export settings for exporting to Navisworks, such as whether to divide the file into levels and whether or not to export room geometry. Additionally, the NavisworksExportOptions.ExportScope property specifieds the export scope. The default is Model. Other options include View and SelectedElements. When set to View, the NavisworksExportOptions . ViewId property should be set accordingly. This property is only used when the export scope is set to View. When set to SelectedElements, the NavisworksExportOptions . SetSelectedElementIds() method should be called with the ids of the elements to be exported.

#### Exporting to DWF and DWFX

Both DWF and DWFX files can be exported using the corresponding Document.Export() overloads. Both methods have a ViewSet parameter that represents the views to be exported. All the views in the ViewSet must be printable in order for the export to succeed. This can be checked using the View.CanBePrinted property of each view. The last parameter is either DWFExportOptions or DWFXExportOptions. DWFXExportOptions is derived from DWFExportOptions and has all the same export settings. Options include whether or not to export the crop box, the image quality whether or not to export textures to 3D DWF files, and the paper format.

<table summary="" id="GUID-A1BE34A2-DA7C-4C2C-9CCB-958A56F1150D__TABLE_1BB826B11FB04198B5250D174FFC45D8"><tbody><tr><td><b>Code Region: Export DWF</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>bool</span><span> </span><span>ExportViewToDWF</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>View</span><span> view</span><span>,</span><span> </span><span>string</span><span> pathname</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>DWFExportOptions</span><span> dwfOptions </span><span>=</span><span> </span><span>new</span><span> </span><span>DWFExportOptions</span><span>();</span><span>
    </span><span>// export with crop box and area and room geometry</span><span>
    dwfOptions</span><span>.</span><span>CropBoxVisible</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
    dwfOptions</span><span>.</span><span>ExportingAreas</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
    dwfOptions</span><span>.</span><span>ExportTexture</span><span> </span><span>=</span><span> </span><span>false</span><span>;</span><span>
    </span><span>ViewSet</span><span> views </span><span>=</span><span> </span><span>new</span><span> </span><span>ViewSet</span><span>();</span><span>
    views</span><span>.</span><span>Insert</span><span>(</span><span>view</span><span>);</span><span>
    </span><span>return</span><span> </span><span>(</span><span>document</span><span>.</span><span>Export</span><span>(</span><span>Path</span><span>.</span><span>GetDirectoryName</span><span>(</span><span>pathname</span><span>),</span><span>
        </span><span>Path</span><span>.</span><span>GetFileNameWithoutExtension</span><span>(</span><span>pathname</span><span>),</span><span> views</span><span>,</span><span> dwfOptions</span><span>));</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

#### Exporting to 3D-Studio Max

FBX Export requires the presence of certain modules that are optional and may not be part of the installed Revit, so the OptionalFunctionalityUtils . IsFBXExportAvailable() method reports whether the FBX Export functionality is available. The Export() method for exporting to 3D-Studio Max has a ViewSet parameter representing the set of views to export. Only 3D views are allowed. The FBXExportOptions parameter can be used to specify whether to export without boundary edges, wther to use levels of detail, and whether the export process should stop when a view fails to export.

#### Exporting to CAD Formats

Exporting to DGN , DWG and DXF format files have similar export methods and options.

DGN , DWG and DXF Export all require the presence of certain modules that are optional and may not be part of the installed version of Revit, so the OptionalFunctionalityUtils class as corresponding methods to reports whether the each of these types of export functionality are available.

The Export() methods for exporting to DGN, DWG and DXF formats all have a parameter representing the views to be exported (as an ICollection of the ElementIds of the views). At least one valid view must be present and it must be printable for the export to succeed. This can be checked using the View.CanBePrinted property of each view.

The export options for each of these formats derives from BaseExportOptions, so there are many export settings in common, such as the color mode or whether or not to hide the scope box. BaseExportOptions also has a static method called GetPredefinedSetupNames() which will return any predefined setups for a document. The name of a predefined setup can then be passed into the static method GetPredefinedOptions() available from the corresponding options class: DWGExportOptions, DGNExportOptions or DXFExportOptions. The export options for DWG and DXF files have even more options in common as they share the base class ACADExportOptions.

The following example exports the active view (if it can be printed) to a DGN file using the first predefined setup name and the predefined options, without making any changes.

<table summary="" id="GUID-A1BE34A2-DA7C-4C2C-9CCB-958A56F1150D__TABLE_828E9F5353004D06ACED2092FD80BF66"><tbody><tr><td><b>Code Region: Export DGN</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>bool</span><span> </span><span>ExportDGN</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>View</span><span> view</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>bool</span><span> exported </span><span>=</span><span> </span><span>false</span><span>;</span><span>
    </span><span>// Get predefined setups and export the first one</span><span>
    </span><span>IList</span><span>&lt;string&gt;</span><span> setupNames </span><span>=</span><span> </span><span>BaseExportOptions</span><span>.</span><span>GetPredefinedSetupNames</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>setupNames</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Get predefined options for first predefined setup</span><span>
        </span><span>DGNExportOptions</span><span> dgnOptions </span><span>=</span><span> </span><span>DGNExportOptions</span><span>.</span><span>GetPredefinedOptions</span><span>(</span><span>document</span><span>,</span><span> setupNames</span><span>[</span><span>0</span><span>]);</span><span>

        </span><span>// export the active view if it is printable</span><span>
        </span><span>if</span><span> </span><span>(</span><span>document</span><span>.</span><span>ActiveView</span><span>.</span><span>CanBePrinted</span><span> </span><span>==</span><span> </span><span>true</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> views </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;();</span><span>
            views</span><span>.</span><span>Add</span><span>(</span><span>view</span><span>.</span><span>Id</span><span>);</span><span>
            exported </span><span>=</span><span> document</span><span>.</span><span>Export</span><span>(</span><span>Path</span><span>.</span><span>GetDirectoryName</span><span>(</span><span>document</span><span>.</span><span>PathName</span><span>),</span><span>
                </span><span>Path</span><span>.</span><span>GetFileNameWithoutExtension</span><span>(</span><span>document</span><span>.</span><span>PathName</span><span>),</span><span> views</span><span>,</span><span> dgnOptions</span><span>);</span><span>
        </span><span>}</span><span>
 </span><span>}</span><span>

    </span><span>return</span><span> exported</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

For these file types it is possible to specify or modify various mapping settings, such as layer mapping or text font mapping by creating the corresponding table and passing it into the appropriate method of the BaseExportOptions class. For layer mapping, you may alternatively pass in a string value to BaseExportOptions.LayerMapping of a predefined layer mapping style or the filename of a layer mapping file. For more information on creating or modifying export tables, see the [Export Tables](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Export_Export_Tables_html) topic.

#### Exporting to SAT

The Export method for SAT has a parameter representing the views to be exported (as an ICollection of the ElementIds of the views). At least one valid view must be present and it must be printable for the export to succeed. This can be checked using the View.CanBePrinted property of each view. The SATExportOptions object has no settings to specify. It uses all default settings.

#### Exporting to Civil Engineering Design Applications

The last Export() method exports a 3D view of the document in the format of Civil Engineering design applications. One parameter of the method is a Viewplan that specifies the gross area plan. All the areas on the view plan will be exported and it must be 'Gross Building' area plan. To check whether its area scheme is Gross Building, use the AreaScheme.GrossBuildingArea property. The BuildingSiteExportOptions object allows custom values for settings such as gross area or total occupancy.

#### Exporting to PDF

**Code Region: Print all sheets to PDF**

```
private void PDFExport(Document doc)
{
    PDFExportOptions opt = new PDFExportOptions();
    opt.Combine = true;
    opt.FileName = "My House";
    opt.PaperFormat = ExportPaperFormat.ARCH_E;
    doc.Export(
        Environment.GetFolderPath(Environment.SpecialFolder.Desktop),
        new FilteredElementCollector(doc)
            .OfClass(typeof(ViewSheet))
            .ToElementIds().ToList(),
        opt);
}
```
