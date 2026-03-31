[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRebarHostData Method

---



|  |
| --- |
| [RebarHostData Class](2b39b172-ad0f-e1c6-99a4-3b828346200c.htm)   [See Also](#seeAlsoToggle) |

Gets a RebarHostData object referring to the specified rebar host element.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static RebarHostData GetRebarHostData( 	Element host ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetRebarHostData ( _ 	host As Element _ ) As RebarHostData ``` |

 

| Visual C++ |
| --- |
| ``` public: static RebarHostData^ GetRebarHostData( 	Element^ host ) ``` |

#### Parameters

host
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     An element to host rebar.

#### Return Value

A RebarHostData object, or    a null reference (  Nothing  in Visual Basic)  .

# Remarks

Returns    a null reference (  Nothing  in Visual Basic)  for elements that cannot ever be rebar hosts, such as levels.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |

# See Also

[RebarHostData Class](2b39b172-ad0f-e1c6-99a4-3b828346200c.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)