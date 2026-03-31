[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OnPolyline Method

---



|  |
| --- |
| [IExportContextBase Interface](6691ecd5-a88a-1f58-7a71-a8f6233b6c51.htm)   [See Also](#seeAlsoToggle) |

This method is called when a Polyline is being output.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)

# Syntax

| C# |
| --- |
| ``` RenderNodeAction OnPolyline( 	PolylineNode node ) ``` |

 

| Visual Basic |
| --- |
| ``` Function OnPolyline ( _ 	node As PolylineNode _ ) As RenderNodeAction ``` |

 

| Visual C++ |
| --- |
| ``` RenderNodeAction OnPolyline( 	PolylineNode^ node ) ``` |

#### Parameters

node
:   Type:  [Autodesk.Revit.DB PolylineNode](d0d38779-f0a4-e975-e71d-c8e7026cadfd.htm)    
     An output node that represents a Polyline.

#### Return Value

Return RenderNodeAction.Proceed if you wish to receive tessellated geometry (polyline segments) for this polyline, or otherwise return RenderNodeAction.Skip.

Note for 2D export: if the export is performed for the view in non-Wireframe display style tesselated geometry will be output regardless of the return value.

# Remarks

Note that this method is invoked only if the custom exporter was set up to include geometric objects in the output stream. See  [IncludeGeometricObjects](2ce1075e-380e-01e7-6459-b7467c2a2414.htm)  for mode details.

Note for 2D export: if the export is performed for the view in non-Wireframe display style this method will be called regardless of whether the object will be eventially output, i.e. even if it's occluded by another element.

# See Also

[IExportContextBase Interface](6691ecd5-a88a-1f58-7a71-a8f6233b6c51.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)