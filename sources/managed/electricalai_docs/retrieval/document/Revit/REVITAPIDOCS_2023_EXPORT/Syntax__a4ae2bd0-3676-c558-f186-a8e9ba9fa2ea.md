[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [DoubleClickOptions Class](910f7cb7-9027-ed13-8502-2bfb9c347aee.htm)   [See Also](#seeAlsoToggle) |

Specifies whether the .NET object represents a valid Revit entity.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 16.0.0.0 (16.0.0.0)   
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

[DoubleClickOptions Class](910f7cb7-9027-ed13-8502-2bfb9c347aee.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)