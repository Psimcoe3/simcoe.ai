[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddItem Method

---



|  |
| --- |
| [ComboBox Class](a5667995-e628-13df-c157-39c95b2435d6.htm)   [See Also](#seeAlsoToggle) |

Adds a new item to the ComboBox.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public ComboBoxMember AddItem( 	ComboBoxMemberData memberData ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AddItem ( _ 	memberData As ComboBoxMemberData _ ) As ComboBoxMember ``` |

 

| Visual C++ |
| --- |
| ``` public: ComboBoxMember^ AddItem( 	ComboBoxMemberData^ memberData ) ``` |

#### Parameters

memberData
:   Type:  [Autodesk.Revit.UI ComboBoxMemberData](aba69b9c-dae6-c872-8dea-91ef7fda5e81.htm)    
     An object containing the data needed to construct the ComboBoxMember.

#### Return Value

The newly added ComboBoxMember.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when memberData is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when button with memberData.Name already exists in the drop-down list. |

# See Also

[ComboBox Class](a5667995-e628-13df-c157-39c95b2435d6.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)