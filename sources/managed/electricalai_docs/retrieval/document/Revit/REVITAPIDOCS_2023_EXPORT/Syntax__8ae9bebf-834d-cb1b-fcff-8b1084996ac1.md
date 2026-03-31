[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Bounds Property

---



|  |
| --- |
| [BoundingBoxXYZ Class](3c452286-57b1-40e2-2795-c90bff1fcec2.htm)   [See Also](#seeAlsoToggle) |

Indexed access for loops. Use 0 for Min and 1 for Max.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public XYZ this[ 	int bound ] { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Bounds ( _ 	bound As Integer _ ) As XYZ 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ Bounds[int bound] { 	XYZ^ get (int bound); 	void set (int bound, XYZ^ value); } ``` |

#### Parameters

bound
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)

# Remarks

The bounds are defined in the coordinate space of the box.

# See Also

[BoundingBoxXYZ Class](3c452286-57b1-40e2-2795-c90bff1fcec2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)