[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsIntersectorValidForCreation Method

---



|  |
| --- |
| [DividedPath Class](8043b21a-7c78-e0cb-f7b3-495ace05de87.htm)   [See Also](#seeAlsoToggle) |

This returns true if the intersector is an element that can be used to intersect with a newly created divided path.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static bool IsIntersectorValidForCreation( 	Document document, 	ElementId intersector ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsIntersectorValidForCreation ( _ 	document As Document, _ 	intersector As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsIntersectorValidForCreation( 	Document^ document,  	ElementId^ intersector ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

intersector
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The intersector.

#### Return Value

True if the reference can be used to create a divided path, false otherwise.

# Remarks

Intersectors can be curve elements, datum planes, or divided paths. This function is should not be used to validate the input to SetIntersectors() because it does not check for self intersection of any other circular dependencies between intersectors. Use isIntersectorValidForDividedPath() instead.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DividedPath Class](8043b21a-7c78-e0cb-f7b3-495ace05de87.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)