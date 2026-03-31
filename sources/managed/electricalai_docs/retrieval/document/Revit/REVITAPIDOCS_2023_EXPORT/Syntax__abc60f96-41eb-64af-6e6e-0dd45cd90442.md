[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PlacementPoint Property

---



|  |
| --- |
| [ImagePlacementOptions Class](20d793a0-4309-dac8-1e43-61d275237887.htm)   [See Also](#seeAlsoToggle) |

Identifies which point of the  [ImageInstance](ff77d6c8-a94a-067a-cd95-4f2cd3ec8dcc.htm)  will be aligned to the  [Location](9e5ffb2b-a732-b118-e551-3966dad02d20.htm)

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public BoxPlacement PlacementPoint { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property PlacementPoint As BoxPlacement 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property BoxPlacement PlacementPoint { 	BoxPlacement get (); 	void set (BoxPlacement value); } ``` |

# Remarks

The location of the corners of the image in the model depends on the size and orientation of the  [ImageInstance](ff77d6c8-a94a-067a-cd95-4f2cd3ec8dcc.htm)  and the orientation of the view it is placed in.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[ImagePlacementOptions Class](20d793a0-4309-dac8-1e43-61d275237887.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)