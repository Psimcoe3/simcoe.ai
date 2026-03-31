[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsAllowedForSolidCut Method

---



|  |
| --- |
| [SolidSolidCutUtils Class](f1a2d176-2ab6-fa4c-293e-970c5866e87c.htm)   [See Also](#seeAlsoToggle) |

Validates that the element is eligible for a solid-solid cut.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static bool IsAllowedForSolidCut( 	Element element ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsAllowedForSolidCut ( _ 	element As Element _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsAllowedForSolidCut( 	Element^ element ) ``` |

#### Parameters

element
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The solid to be cut or the cutting solid.

#### Return Value

True if the input element can participate in a solid-solid cut. False otherwise.

# Remarks

The element must be solid and must be a GenericForm, GeomCombination, or a FamilyInstance.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[SolidSolidCutUtils Class](f1a2d176-2ab6-fa4c-293e-970c5866e87c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)