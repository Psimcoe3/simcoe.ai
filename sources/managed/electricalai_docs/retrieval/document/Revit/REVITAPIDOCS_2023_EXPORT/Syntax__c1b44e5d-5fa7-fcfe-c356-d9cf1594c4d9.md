[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [StructuralSectionAnalysisParams Class](e5bd2059-9102-0c1c-e9d4-16a015a4cb5e.htm)   [See Also](#seeAlsoToggle) |

Specifies whether the .NET object represents a valid Revit entity.

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
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

[StructuralSectionAnalysisParams Class](e5bd2059-9102-0c1c-e9d4-16a015a4cb5e.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)