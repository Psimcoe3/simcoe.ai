[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetFirstCoreLayerIndex Method

---



|  |
| --- |
| [CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)   [See Also](#seeAlsoToggle) |

Gets the index of the first core layer.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public int GetFirstCoreLayerIndex() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetFirstCoreLayerIndex As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: int GetFirstCoreLayerIndex() ``` |

#### Return Value

The index of the first core layer.

# Remarks

This is the index on the exterior side. You can change the shell/core layer boundary using  [SetNumberOfShellLayers(ShellLayerType, Int32)](8b8ea4e3-e697-6176-92c0-dc2687723a71.htm)  .

# See Also

[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)