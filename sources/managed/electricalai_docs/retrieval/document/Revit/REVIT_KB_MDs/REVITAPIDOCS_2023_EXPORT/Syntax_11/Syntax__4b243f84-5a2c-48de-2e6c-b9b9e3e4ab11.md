[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsAllowedAsDisplacedElement Method

---



|  |
| --- |
| [DisplacementElement Class](08113547-eaaa-5ec1-5ff1-de609fe7c29c.htm)   [See Also](#seeAlsoToggle) |

Indicates if the specified element is allowed to be displaced.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static bool IsAllowedAsDisplacedElement( 	Element element ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsAllowedAsDisplacedElement ( _ 	element As Element _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsAllowedAsDisplacedElement( 	Element^ element ) ``` |

#### Parameters

element
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     Any element.

#### Return Value

Returns true if the element is eligible to be assigned to a DisplacementElement.

# Remarks

Exclusions include view specific elements as well as certain categories of elements.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DisplacementElement Class](08113547-eaaa-5ec1-5ff1-de609fe7c29c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)