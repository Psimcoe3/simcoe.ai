[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Project Method

---



|  |
| --- |
| [Face Class](e32b3b1f-66fc-57cb-6e1c-aa81d1bf3e63.htm)   [See Also](#seeAlsoToggle) |

Projects the specified point on the face.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public IntersectionResult Project( 	XYZ point ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Project ( _ 	point As XYZ _ ) As IntersectionResult ``` |

 

| Visual C++ |
| --- |
| ``` public: IntersectionResult^ Project( 	XYZ^ point ) ``` |

#### Parameters

point
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The point to be projected.

#### Return Value

Geometric information if projection is successful; if projection fails or the nearest point is outside of this face, returns    a null reference (  Nothing  in Visual Basic)  .

# Remarks

The following is the meaning of IntersectionResult's members:

* XYZPoint is the nearest point to the projected point on the face.
* UVPoint is the UV coordinates of the nearest point on the face.
* Distance is the distance from the point to the face.
* EdgeObject is the edge if projected point is near an edge.
* EdgeParameter is the parameter of the nearest point on the edge.

# See Also

[Face Class](e32b3b1f-66fc-57cb-6e1c-aa81d1bf3e63.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)