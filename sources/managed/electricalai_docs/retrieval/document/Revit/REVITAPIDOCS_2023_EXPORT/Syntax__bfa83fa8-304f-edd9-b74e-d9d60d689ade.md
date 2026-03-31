[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UsesLevelFiltering Method

---



|  |
| --- |
| [FilterElementIdRule Class](4675442b-8c75-4e20-ba18-71df13b86896.htm)   [See Also](#seeAlsoToggle) |

This function checks if a parameter uses level filtering.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public static bool UsesLevelFiltering( 	Document doc, 	ElementId parameterId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function UsesLevelFiltering ( _ 	doc As Document, _ 	parameterId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool UsesLevelFiltering( 	Document^ doc,  	ElementId^ parameterId ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document which owns the parameter.

parameterId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the parameter that will be tested to see if it uses level filtering.

#### Return Value

True if the parameter uses level filtering, false otherwise.

# Remarks

When level-filtering parameters are compared, the comparisons will first compare the values of the levels' elevations, then compare the levels' names, and finally the levels' element ids to rank and sort the levels.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FilterElementIdRule Class](4675442b-8c75-4e20-ba18-71df13b86896.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)