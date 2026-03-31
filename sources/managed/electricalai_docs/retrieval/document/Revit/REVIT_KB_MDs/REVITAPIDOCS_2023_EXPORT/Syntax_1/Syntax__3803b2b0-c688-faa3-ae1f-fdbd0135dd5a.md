[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RemoveControl Method

---



|  |
| --- |
| [TemporaryGraphicsManager Class](1dd29f70-d381-fa60-8ffa-1076eac55ed7.htm)   [See Also](#seeAlsoToggle) |

Deletes the existing control identified by the unique index.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public void RemoveControl( 	int index ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub RemoveControl ( _ 	index As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void RemoveControl( 	int index ) ``` |

#### Parameters

index
:   Type:  System Int32    
     Unique index of the control to be deleted.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | index is out of range of TemporaryGraphicsManager managed objects, or the indexed object has been removed from the document. |

# See Also

[TemporaryGraphicsManager Class](1dd29f70-d381-fa60-8ffa-1076eac55ed7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)