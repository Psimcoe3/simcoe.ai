[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsChangeTriggered Method

---



|  |
| --- |
| [UpdaterData Class](58751d04-6f56-0346-e7ba-f21e61a459be.htm)   [See Also](#seeAlsoToggle) |

Allows updater to check if specific change has happened to an element. Compares input type to the types that caused Updater::execute() to be triggered. If input type was not registered as a trigger for the associated Updater, this method will always return false for that ChangeType. For example, if the only trigger registered for UpdaterX is ChangeTypeAny for Element A, then passing in ChangeTypeGeometry will return false even if the geometry of A changed because the registered trigger was ChangeTypeAny. However, passing in ChangeTypeAny will return true.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public bool IsChangeTriggered( 	ElementId id, 	ChangeType type ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsChangeTriggered ( _ 	id As ElementId, _ 	type As ChangeType _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsChangeTriggered( 	ElementId^ id,  	ChangeType^ type ) ``` |

#### Parameters

id
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Id of element to check

type
:   Type:  [Autodesk.Revit.DB ChangeType](bf7c5e20-b639-da97-4586-4a0bc0010705.htm)    
     ChangeType to check

#### Return Value

True if ChangeType happened to specified element

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[UpdaterData Class](58751d04-6f56-0346-e7ba-f21e61a459be.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)