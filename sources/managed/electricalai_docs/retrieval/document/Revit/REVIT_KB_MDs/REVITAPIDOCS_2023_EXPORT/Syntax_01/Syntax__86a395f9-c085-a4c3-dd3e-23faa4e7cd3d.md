[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateGreaterRule Method (ElementId, Int32)

---



|  |
| --- |
| [ParameterFilterRuleFactory Class](317755a4-24ba-9f36-7639-f6fb2aa5a1a7.htm)   [See Also](#seeAlsoToggle) |

Creates a filter rule that determines whether integer values from the document are greater than a certain value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static FilterRule CreateGreaterRule( 	ElementId parameter, 	int value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateGreaterRule ( _ 	parameter As ElementId, _ 	value As Integer _ ) As FilterRule ``` |

 

| Visual C++ |
| --- |
| ``` public: static FilterRule^ CreateGreaterRule( 	ElementId^ parameter,  	int value ) ``` |

#### Parameters

parameter
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     An integer-typed parameter used to get values from the document for a given element.

value
:   Type:  System Int32    
     The user-supplied value against which values from the document will be compared.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ParameterFilterRuleFactory Class](317755a4-24ba-9f36-7639-f6fb2aa5a1a7.htm)

[CreateGreaterRule Overload](3885f1a1-d26c-a3c3-54e1-81f75c04148a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)