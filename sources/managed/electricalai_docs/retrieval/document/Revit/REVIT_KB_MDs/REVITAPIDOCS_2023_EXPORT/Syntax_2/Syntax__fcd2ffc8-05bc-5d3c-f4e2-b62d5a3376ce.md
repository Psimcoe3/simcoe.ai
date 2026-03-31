[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetWidth Method

---



|  |
| --- |
| [CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)   [See Also](#seeAlsoToggle) |

The width implied by this compound structure.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double GetWidth() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetWidth As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetWidth() ``` |

#### Return Value

The width of a host object with this compound structure.

# Remarks

If the structure is not vertically compound, then this is simply the sum of all layers' widths. If the structure is vertically compound, this is the width of the rectangular grid stored in the vertically compound structure. The presence of a layer with variable width has no effect on the value returned by this method. The value returned assumes that all layers have their specified width.

# See Also

[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)

[GetWidth Overload](b131b5cc-f977-51bb-c0ab-be4a5a025b44.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)