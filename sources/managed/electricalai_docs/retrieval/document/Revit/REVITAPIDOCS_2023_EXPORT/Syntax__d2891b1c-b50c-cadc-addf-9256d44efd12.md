[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BoundingBoxContainsPointFilter Constructor (XYZ, Double, Boolean)

---



|  |
| --- |
| [BoundingBoxContainsPointFilter Class](a5ea9f5a-ddba-9db7-eaa0-2b37098f0142.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of a filter to match elements with a bounding box that contains the given point, while specifying the tolerance to be used in deciding if the point matches the criteria. This constructor includes the option to invert the filter and match all elements with a bounding box that do not contain the given point.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public BoundingBoxContainsPointFilter( 	XYZ point, 	double tolerance, 	bool inverted ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	point As XYZ, _ 	tolerance As Double, _ 	inverted As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: BoundingBoxContainsPointFilter( 	XYZ^ point,  	double tolerance,  	bool inverted ) ``` |

#### Parameters

point
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The point used to find elements with a bounding box containing it.

tolerance
:   Type:  System Double    
     The tolerance value to use instead of zero. See the tolerance property for details.

inverted
:   Type:  System Boolean    
     True if the filter should be inverted and match all elements with a bounding box that do not contain the given point.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given value for tolerance is not finite -or- The given value for tolerance is not a number |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[BoundingBoxContainsPointFilter Class](a5ea9f5a-ddba-9db7-eaa0-2b37098f0142.htm)

[BoundingBoxContainsPointFilter Overload](293da828-ed6d-9a64-5143-953021760779.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)