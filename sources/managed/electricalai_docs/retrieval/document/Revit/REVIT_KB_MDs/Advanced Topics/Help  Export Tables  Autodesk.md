---
created: 2026-01-28T21:18:04 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Export_Export_Tables_html
author: 
---

# Help | Export Tables | Autodesk

> ## Excerpt
> The classes listed in the table below expose read and write access to the tables used for mapping on export to various formats such as DWG and DGN. Each class contains (key, info) pairs of mapping data.

---
The classes listed in the table below expose read and write access to the tables used for mapping on export to various formats such as DWG and DGN. Each class contains (key, info) pairs of mapping data.

<table summary="" id="GUID-0A59F08C-2627-4DA3-AC25-C2BCBDE09ED8__TABLE_E048117C2F884E9F9EB547A4634FE5BD"><tbody><tr><td><b>Class</b></td><td><b>Description</b></td></tr><tr><td>ExportLayerTable</td><td>Represents a table supporting a mapping of various layer properties (Category, name, color name) to layer name in the target export format.</td></tr><tr><td>ExportLinetypeTable</td><td>Represents a table supporting a mapping of linetype names in the target export format.</td></tr><tr><td>ExportPatternTable</td><td>Represents a table supporting a mapping of FillPattern names and ids to FillPattern names in the target export format.</td></tr><tr><td>ExportFontTable</td><td>Represents a table s upporting a mapping of font names in the target export format.</td></tr><tr><td>ExportLineweightTable</td><td>Represents a table s upporting a mapping of lineweight names in the target export format.</td></tr></tbody></table>

Most of these tables are available through the BaseExportOptions class (the base class for options for DGN, DXF and DWG formats). The ExportLineweightTable is available from the DGNExportOptions class. Each table has a corresponding Get and Set method. To modify the mappings, get the corresponding table, make changes and then set it back to the options class.

The following example modifies the ExportLayerTable prior to exporting a DWG file.

<table summary="" id="GUID-0A59F08C-2627-4DA3-AC25-C2BCBDE09ED8__TABLE_FE3D2F55A2C248E4B26C9BB4B63938B4"><tbody><tr><td><b>Code Region: Export DWG with modified ExportLayerTable</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>bool</span><span> </span><span>ExportDWGModifyLayerTable</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>View</span><span> view</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>bool</span><span> exported </span><span>=</span><span> </span><span>false</span><span>;</span><span>
    </span><span>IList</span><span>&lt;string&gt;</span><span> setupNames </span><span>=</span><span> </span><span>BaseExportOptions</span><span>.</span><span>GetPredefinedSetupNames</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>setupNames</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Get the export options for the first predefined setup</span><span>
        </span><span>DWGExportOptions</span><span> dwgOptions </span><span>=</span><span> </span><span>DWGExportOptions</span><span>.</span><span>GetPredefinedOptions</span><span>(</span><span>document</span><span>,</span><span> setupNames</span><span>[</span><span>0</span><span>]);</span><span>

        </span><span>// Get the export layer table</span><span>
        </span><span>ExportLayerTable</span><span> layerTable </span><span>=</span><span> dwgOptions</span><span>.</span><span>GetExportLayerTable</span><span>();</span><span>

        </span><span>// Find the first mapping for the Ceilings category</span><span>
        </span><span>string</span><span> category </span><span>=</span><span> </span><span>"Ceilings"</span><span>;</span><span>
        </span><span>ExportLayerKey</span><span> targetKey </span><span>=</span><span> layerTable</span><span>.</span><span>GetKeys</span><span>().</span><span>First</span><span>&lt;</span><span>ExportLayerKey</span><span>&gt;(</span><span>layerKey </span><span>=&gt;</span><span> layerKey</span><span>.</span><span>CategoryName</span><span> </span><span>==</span><span> category</span><span>);</span><span>
        </span><span>ExportLayerInfo</span><span> targetInfo </span><span>=</span><span> layerTable</span><span>[</span><span>targetKey</span><span>];</span><span>

        </span><span>// change the color name and cut color number for this mapping</span><span>
        targetInfo</span><span>.</span><span>ColorName</span><span> </span><span>=</span><span> </span><span>"31"</span><span>;</span><span>
        targetInfo</span><span>.</span><span>CutColorNumber</span><span> </span><span>=</span><span> </span><span>31</span><span>;</span><span>

        </span><span>// Set the change back to the map</span><span>
        layerTable</span><span>[</span><span>targetKey</span><span>]</span><span> </span><span>=</span><span> targetInfo</span><span>;</span><span>

        </span><span>// Set the modified table back to the options</span><span>
        dwgOptions</span><span>.</span><span>SetExportLayerTable</span><span>(</span><span>layerTable</span><span>);</span><span>

        </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> views </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;();</span><span>
        views</span><span>.</span><span>Add</span><span>(</span><span>view</span><span>.</span><span>Id</span><span>);</span><span>

        exported </span><span>=</span><span> document</span><span>.</span><span>Export</span><span>(</span><span>Path</span><span>.</span><span>GetDirectoryName</span><span>(</span><span>document</span><span>.</span><span>PathName</span><span>),</span><span>
            </span><span>Path</span><span>.</span><span>GetFileNameWithoutExtension</span><span>(</span><span>document</span><span>.</span><span>PathName</span><span>),</span><span> views</span><span>,</span><span> dwgOptions</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> exported</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
