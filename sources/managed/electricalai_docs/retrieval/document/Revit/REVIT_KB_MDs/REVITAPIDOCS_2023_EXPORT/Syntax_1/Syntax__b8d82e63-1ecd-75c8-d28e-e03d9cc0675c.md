[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsParameterApplicable Method

---



|  |
| --- |
| [ParameterFilterUtilities Class](50afdc29-3a0c-e3d9-c547-0fcdb40d3ce8.htm)   [See Also](#seeAlsoToggle) |

Used to determine whether the element supports the given parameter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static bool IsParameterApplicable( 	Element element, 	ElementId parameter ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsParameterApplicable ( _ 	element As Element, _ 	parameter As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsParameterApplicable( 	Element^ element,  	ElementId^ parameter ) ``` |

#### Parameters

element
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The element to query for support of the given parameter.

parameter
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The parameter for which to query support.

#### Return Value

True if the element supports the given parameter, false otherwise.

# Remarks

This operation is supported for external (e.g., shared, project) parameters only.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ParameterFilterUtilities Class](50afdc29-3a0c-e3d9-c547-0fcdb40d3ce8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)