[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OnElementBegin2D Method

---



|  |
| --- |
| [IExportContext2D Interface](a4578846-6ecf-e354-668d-96d8ef5d1a32.htm)   [See Also](#seeAlsoToggle) |

This method marks the beginning of an element to be exported.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` RenderNodeAction OnElementBegin2D( 	ElementNode node ) ``` |

 

| Visual Basic |
| --- |
| ``` Function OnElementBegin2D ( _ 	node As ElementNode _ ) As RenderNodeAction ``` |

 

| Visual C++ |
| --- |
| ``` RenderNodeAction OnElementBegin2D( 	ElementNode^ node ) ``` |

#### Parameters

node
:   Type:  [Autodesk.Revit.DB ElementNode](45f8a303-c479-9d6e-c39e-7705169820c2.htm)    
     Node representing the element that is about to start being exported. Contains element ID and document.

#### Return Value

Return RenderNodeAction.Skip if you wish to skip exporting this element, or return RenderNodeAction.Proceed otherwise.

# Remarks

For views having non-Wireframe display style, geometry of elements is output outside of view, instance and link begin/end brackets. Therefore the argument to this method is ElementNode that has both element ID and the host document.

# See Also

[IExportContext2D Interface](a4578846-6ecf-e354-668d-96d8ef5d1a32.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)