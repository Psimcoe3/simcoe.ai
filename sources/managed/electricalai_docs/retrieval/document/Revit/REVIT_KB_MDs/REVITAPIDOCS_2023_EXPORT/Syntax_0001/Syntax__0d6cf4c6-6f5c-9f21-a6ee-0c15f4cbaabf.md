[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidHost Method (Element)

---



|  |
| --- |
| [RebarHostData Class](2b39b172-ad0f-e1c6-99a4-3b828346200c.htm)   [See Also](#seeAlsoToggle) |

Identifies whether a given element can host reinforcement.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public static bool IsValidHost( 	Element element ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidHost ( _ 	element As Element _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidHost( 	Element^ element ) ``` |

#### Parameters

element
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The element to check.

#### Return Value

True if the input Element can host reinforcement elements, false otherwise.

# Remarks

Many different elements are allowed to host reinforcement, for example, beams, walls, columns, or parts. Often there are specific restrictions about whether an element can host rebar beyond its type or category. For example, the material type of the element may determine this. Or for parts, the part must have been created from layers that have their role set to Structure.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RebarHostData Class](2b39b172-ad0f-e1c6-99a4-3b828346200c.htm)

[IsValidHost Overload](aaff4dec-529b-0e41-aeb5-e632c4ad084c.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)