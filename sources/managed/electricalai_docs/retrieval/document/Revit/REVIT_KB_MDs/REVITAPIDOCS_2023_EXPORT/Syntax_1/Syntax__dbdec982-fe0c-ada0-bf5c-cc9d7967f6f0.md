[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetAssignedElectricalSystems Method

---



|  |
| --- |
| [MEPModel Class](dd78bce5-2ed6-ed3c-f329-1663bf08afa6.htm)   [See Also](#seeAlsoToggle) |

Retrieves the electrical systems this electrical panel currently is assigned to.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public ISet<ElectricalSystem> GetAssignedElectricalSystems() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetAssignedElectricalSystems As ISet(Of ElectricalSystem) ``` |

 

| Visual C++ |
| --- |
| ``` public: ISet<ElectricalSystem^>^ GetAssignedElectricalSystems() ``` |

# Remarks

This property returns a set of Electrical Systems. If there are no electrical systems created for this model, this property will be an empty set. This method supersedes an older  *AssignedElectricalSystems*  property which has been deprecated.

# See Also

[MEPModel Class](dd78bce5-2ed6-ed3c-f329-1663bf08afa6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)