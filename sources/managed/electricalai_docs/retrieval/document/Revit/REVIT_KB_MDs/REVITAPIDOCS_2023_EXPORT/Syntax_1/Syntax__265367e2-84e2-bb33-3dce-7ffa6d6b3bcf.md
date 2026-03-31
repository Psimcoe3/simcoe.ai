[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetEntity Method

---



|  |
| --- |
| [PipeFittingAndAccessoryPressureDropUIDataItem Class](c1471c51-00e6-067b-164a-d00f4d66f97e.htm)   [See Also](#seeAlsoToggle) |

Stores the entity in the UI data item.

**Namespace:**   [Autodesk.Revit.UI.Plumbing](a4cc3644-f568-6568-9c2f-dcdb6eafdf6b.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void SetEntity( 	Entity entity ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetEntity ( _ 	entity As Entity _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetEntity( 	Entity^ entity ) ``` |

#### Parameters

entity
:   Type:  [Autodesk.Revit.DB.ExtensibleStorage Entity](cf17f0e8-33bd-ef95-bf4b-e6298406f29b.htm)    
     The Entity to be stored.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Writing of Entities of this Schema is not allowed to the current add-in. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PipeFittingAndAccessoryPressureDropUIDataItem Class](c1471c51-00e6-067b-164a-d00f4d66f97e.htm)

[Autodesk.Revit.UI.Plumbing Namespace](a4cc3644-f568-6568-9c2f-dcdb6eafdf6b.htm)