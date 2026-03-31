[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HideAllAttachedDetailGroups Method

---



|  |
| --- |
| [Group Class](ca54af3c-52d8-0aed-cd22-440ec2584b89.htm)   [See Also](#seeAlsoToggle) |

Hides all the available attached detail groups for this element group type that are compatible with the input view type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2019.1

# Syntax

| C# |
| --- |
| ``` public void HideAllAttachedDetailGroups( 	View view ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub HideAllAttachedDetailGroups ( _ 	view As View _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void HideAllAttachedDetailGroups( 	View^ view ) ``` |

#### Parameters

view
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The view that the attached detail groups must be compatible with.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The input group is not a model group and can therefore not have attached detail groups. |

# See Also

[Group Class](ca54af3c-52d8-0aed-cd22-440ec2584b89.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)