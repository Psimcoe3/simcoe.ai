[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetAvailableAttachedDetailGroupTypeIds Method

---



|  |
| --- |
| [Group Class](ca54af3c-52d8-0aed-cd22-440ec2584b89.htm)   [See Also](#seeAlsoToggle) |

Returns the attached detail groups available for this group type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2019.1

# Syntax

| C# |
| --- |
| ``` public ISet<ElementId> GetAvailableAttachedDetailGroupTypeIds() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetAvailableAttachedDetailGroupTypeIds As ISet(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: ISet<ElementId^>^ GetAvailableAttachedDetailGroupTypeIds() ``` |

#### Return Value

Returns the collection of attached detail group Ids that match this group's type.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The input group is not a model group and can therefore not have attached detail groups. |

# See Also

[Group Class](ca54af3c-52d8-0aed-cd22-440ec2584b89.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)