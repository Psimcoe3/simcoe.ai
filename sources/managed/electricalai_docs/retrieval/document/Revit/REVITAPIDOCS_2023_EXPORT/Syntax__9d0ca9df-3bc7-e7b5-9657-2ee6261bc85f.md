[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExtendIntoWall Property

---



|  |
| --- |
| [FootPrintRoof Class](97eb52e6-5dfd-86b3-708d-aabcda389f4a.htm)   [See Also](#seeAlsoToggle) |

Retrieve or set whether extend into wall the curve.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool this[ 	ModelCurve pCurve ] { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ExtendIntoWall ( _ 	pCurve As ModelCurve _ ) As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool ExtendIntoWall[ModelCurve^ pCurve] { 	bool get (ModelCurve^ pCurve); 	void set (ModelCurve^ pCurve, bool value); } ``` |

#### Parameters

pCurve
:   Type:  [Autodesk.Revit.DB ModelCurve](f15a85c2-3aee-9055-f9f8-9001b47fcefb.htm)

# Remarks

Only applicable when the FootPrintRoof is created with Pick Walls.

# See Also

[FootPrintRoof Class](97eb52e6-5dfd-86b3-708d-aabcda389f4a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)