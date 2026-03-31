[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetFilterableParametersInCommon Method

---



|  |
| --- |
| [ParameterFilterUtilities Class](50afdc29-3a0c-e3d9-c547-0fcdb40d3ce8.htm)   [See Also](#seeAlsoToggle) |

Returns the filterable parameters common to the given categories.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static ICollection<ElementId> GetFilterableParametersInCommon( 	Document aDoc, 	ICollection<ElementId> categories ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetFilterableParametersInCommon ( _ 	aDoc As Document, _ 	categories As ICollection(Of ElementId) _ ) As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: static ICollection<ElementId^>^ GetFilterableParametersInCommon( 	Document^ aDoc,  	ICollection<ElementId^>^ categories ) ``` |

#### Parameters

aDoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document containing the categories and parameters to query.

categories
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The categories for which to determine the common parameters.

#### Return Value

The set of filterable parameters common to the given categories.

# Remarks

A filterable category in Revit has a set of filterable parameters. The filterable parameters common to a set of categories is the intersection of all these filterable parameter sets.

This set defines the set of parameters that may be used to define a rule on a ParameterFilterElement with a certain set of categories.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ParameterFilterUtilities Class](50afdc29-3a0c-e3d9-c547-0fcdb40d3ce8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)