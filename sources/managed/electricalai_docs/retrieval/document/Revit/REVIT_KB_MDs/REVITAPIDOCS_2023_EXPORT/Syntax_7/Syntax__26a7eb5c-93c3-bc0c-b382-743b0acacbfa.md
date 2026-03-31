[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetModifiedElementIds Method (ElementFilter)

---



|  |
| --- |
| [DocumentChangedEventArgs Class](8fd170b2-df48-209b-438e-54ec7b01b664.htm)   [See Also](#seeAlsoToggle) |

Returns set of elements that were modified according to the given element filter.

**Namespace:**   [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public ICollection<ElementId> GetModifiedElementIds( 	ElementFilter filter ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetModifiedElementIds ( _ 	filter As ElementFilter _ ) As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: ICollection<ElementId^>^ GetModifiedElementIds( 	ElementFilter^ filter ) ``` |

#### Parameters

filter
:   Type:  [Autodesk.Revit.DB ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)    
     The element filter to be applied.

#### Return Value

The set of ElementId for modified elements that pass the filter. Returns empty set if no elements are found which pass the filter.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DocumentChangedEventArgs Class](8fd170b2-df48-209b-438e-54ec7b01b664.htm)

[GetModifiedElementIds Overload](eb5eab82-7e48-958b-9999-dc8826ca26f3.htm)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.htm)