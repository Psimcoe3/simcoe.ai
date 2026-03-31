[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCuttingVoidInstances Method

---



|  |
| --- |
| [InstanceVoidCutUtils Class](68b4818a-d737-be1e-0347-ebe305fe3b70.htm)   [See Also](#seeAlsoToggle) |

Return ids of the instances with unattached voids cutting the element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static ICollection<ElementId> GetCuttingVoidInstances( 	Element element ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetCuttingVoidInstances ( _ 	element As Element _ ) As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: static ICollection<ElementId^>^ GetCuttingVoidInstances( 	Element^ element ) ``` |

#### Parameters

element
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The element being cut

#### Return Value

Ids of instances with unattached voids that cut this element

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[InstanceVoidCutUtils Class](68b4818a-d737-be1e-0347-ebe305fe3b70.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)