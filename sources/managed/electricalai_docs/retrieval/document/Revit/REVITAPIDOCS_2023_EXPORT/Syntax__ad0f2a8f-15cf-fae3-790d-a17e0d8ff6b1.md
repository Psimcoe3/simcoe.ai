[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetAnalyticalNodeData Method

---



|  |
| --- |
| [AnalyticalNodeData Class](24e7600a-2ae0-f25c-c36a-62b5bfcdc2eb.htm)   [See Also](#seeAlsoToggle) |

Returns AnalyticalNodeData associated with this element, if it exists.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static AnalyticalNodeData GetAnalyticalNodeData( 	Element element ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetAnalyticalNodeData ( _ 	element As Element _ ) As AnalyticalNodeData ``` |

 

| Visual C++ |
| --- |
| ``` public: static AnalyticalNodeData^ GetAnalyticalNodeData( 	Element^ element ) ``` |

#### Parameters

element
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The element from which we try to obtain AnalyticalNodeData.

# Remarks

If the input element doesn't have AnalyticalNodeData than it retuns    a null reference (  Nothing  in Visual Basic)  . The input element should be a ReferencePoint.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[AnalyticalNodeData Class](24e7600a-2ae0-f25c-c36a-62b5bfcdc2eb.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)