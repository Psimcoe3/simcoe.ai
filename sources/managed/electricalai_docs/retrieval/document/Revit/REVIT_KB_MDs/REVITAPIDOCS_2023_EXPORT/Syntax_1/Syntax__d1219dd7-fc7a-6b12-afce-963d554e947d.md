[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Evaluate Method

---



|  |
| --- |
| [Face Class](e32b3b1f-66fc-57cb-6e1c-aa81d1bf3e63.htm)   [See Also](#seeAlsoToggle) |

Evaluates and returns the XYZ coordinates of a point at the indicated UV parameterization of the face.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public XYZ Evaluate( 	UV params ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Evaluate ( _ 	params As UV _ ) As XYZ ``` |

 

| Visual C++ |
| --- |
| ``` public: XYZ^ Evaluate( 	UV^ params ) ``` |

#### Parameters

params
:   Type:  [Autodesk.Revit.DB UV](1724be37-059b-91ff-aa74-d1508082f76d.htm)    
     The parameters to be evaluated, in natural parameterization of the face.

#### Return Value

The XYZ coordinates.

# Remarks

The evaluation is performed on the underlying Surface, and can return results outside of the boundaries of the face.

# See Also

[Face Class](e32b3b1f-66fc-57cb-6e1c-aa81d1bf3e63.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)