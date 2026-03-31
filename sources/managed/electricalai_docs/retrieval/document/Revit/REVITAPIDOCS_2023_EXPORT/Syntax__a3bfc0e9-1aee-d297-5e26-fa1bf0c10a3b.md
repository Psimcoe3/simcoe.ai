[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [DuctFittingAndAccessoryPressureDropUIDataItem Class](21430cd5-52d1-fcae-d793-43fcef03dfdc.htm)   [See Also](#seeAlsoToggle) |

Specifies whether the .NET object represents a valid Revit entity.

**Namespace:**   [Autodesk.Revit.UI.Mechanical](9c9cf593-a9fe-7469-53c5-7b56ba7cd17e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool IsValidObject { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsValidObject As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsValidObject { 	bool get (); } ``` |

#### Return Value

True if the API object holds a valid Revit native object, false otherwise.

# Remarks

If the corresponding Revit native object is destroyed, or creation of the corresponding object is undone, a managed API object containing it is no longer valid. API methods cannot be called on invalidated wrapper objects.

# See Also

[DuctFittingAndAccessoryPressureDropUIDataItem Class](21430cd5-52d1-fcae-d793-43fcef03dfdc.htm)

[Autodesk.Revit.UI.Mechanical Namespace](9c9cf593-a9fe-7469-53c5-7b56ba7cd17e.htm)