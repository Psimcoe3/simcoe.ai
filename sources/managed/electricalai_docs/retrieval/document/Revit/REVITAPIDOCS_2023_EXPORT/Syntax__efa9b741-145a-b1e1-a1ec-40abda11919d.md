[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SlabShapeEditor Property

---



|  |
| --- |
| [Floor Class](96cc6685-003d-ff90-1c5b-c25a4830f0f7.htm)   [See Also](#seeAlsoToggle) |

Get the SlabShapeEditor used for slab shape editing.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public SlabShapeEditor SlabShapeEditor { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property SlabShapeEditor As SlabShapeEditor 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property SlabShapeEditor^ SlabShapeEditor { 	SlabShapeEditor^ get (); } ``` |

# Remarks

Only flat and horizontal floor is valid for slab shape edit. Otherwise, ShapeEditor will be    a null reference (  Nothing  in Visual Basic)  .

# See Also

[Floor Class](96cc6685-003d-ff90-1c5b-c25a4830f0f7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)