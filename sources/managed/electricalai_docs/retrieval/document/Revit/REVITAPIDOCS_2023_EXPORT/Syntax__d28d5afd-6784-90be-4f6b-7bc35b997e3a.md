[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetTransformFromViewToView Method

---



|  |
| --- |
| [ElementTransformUtils Class](82e737d5-fda4-bc10-6099-88999cd51300.htm)   [See Also](#seeAlsoToggle) |

Returns a transformation that is applied to elements when copying from one view to another view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static Transform GetTransformFromViewToView( 	View sourceView, 	View destinationView ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetTransformFromViewToView ( _ 	sourceView As View, _ 	destinationView As View _ ) As Transform ``` |

 

| Visual C++ |
| --- |
| ``` public: static Transform^ GetTransformFromViewToView( 	View^ sourceView,  	View^ destinationView ) ``` |

#### Parameters

sourceView
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The source view

destinationView
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The destination view

#### Return Value

The transformation from source view to destination view.

# Remarks

Both source and destination views must be 2D graphics views capable of drawing details and view-specific elements (floor and ceiling plans, elevations, sections, drafting views.) The result is a transformation needed to copy an element from drawing plane of the source view to the drawing plane of the destination view. The destination view can be in the same document as the source view. The destination view can be the same as the source view.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The specified view cannot be used as a source or destination for copying elements between two views. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ElementTransformUtils Class](82e737d5-fda4-bc10-6099-88999cd51300.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)