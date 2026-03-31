[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateFromCenterline Method

---



|  |
| --- |
| [FabricationPartRouteEnd Class](58bd199f-5114-67de-011b-d054a1a4c4d9.htm)   [See Also](#seeAlsoToggle) |

Create fabrication routing end from centreline point on straight element.

**Namespace:**   [Autodesk.Revit.DB.Fabrication](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static FabricationPartRouteEnd CreateFromCenterline( 	Element element, 	XYZ ptAt ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateFromCenterline ( _ 	element As Element, _ 	ptAt As XYZ _ ) As FabricationPartRouteEnd ``` |

 

| Visual C++ |
| --- |
| ``` public: static FabricationPartRouteEnd^ CreateFromCenterline( 	Element^ element,  	XYZ^ ptAt ) ``` |

#### Parameters

element
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The straight element that the centerline is on.

ptAt
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     A point along the straight element where the fitting to be cut in should be positioned.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FabricationPartRouteEnd Class](58bd199f-5114-67de-011b-d054a1a4c4d9.htm)

[Autodesk.Revit.DB.Fabrication Namespace](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)