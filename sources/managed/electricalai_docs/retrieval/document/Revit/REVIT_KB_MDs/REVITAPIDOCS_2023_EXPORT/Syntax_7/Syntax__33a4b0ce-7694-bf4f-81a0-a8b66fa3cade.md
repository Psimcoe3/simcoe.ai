[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCoreBoundaryLayerIndex Method

---



|  |
| --- |
| [CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)   [See Also](#seeAlsoToggle) |

Returns the index of the layer just below the core boundary.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public int GetCoreBoundaryLayerIndex( 	ShellLayerType shellLayerType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetCoreBoundaryLayerIndex ( _ 	shellLayerType As ShellLayerType _ ) As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: int GetCoreBoundaryLayerIndex( 	ShellLayerType shellLayerType ) ``` |

#### Parameters

shellLayerType
:   Type:  [Autodesk.Revit.DB ShellLayerType](75c640b9-9904-7882-43fc-a4dfc25ff53c.htm)    
     If ShellLayerType.Exterior return the index on the exterior side (or top side for a roof, floor, or ceiling type). If ShellLayerType.Interior return the index on the interior side (or bottom side for a roof, floor, or ceiling type).

#### Return Value

The index of the layer.

# Remarks

-1 returned if there is no such a layer. You can change the shell/core layer boundary using  [SetNumberOfShellLayers(ShellLayerType, Int32)](8b8ea4e3-e697-6176-92c0-dc2687723a71.htm)  .

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)