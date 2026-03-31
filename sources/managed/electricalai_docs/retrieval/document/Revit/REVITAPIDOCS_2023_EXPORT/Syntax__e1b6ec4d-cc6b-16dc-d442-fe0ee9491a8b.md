[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ComputeSecondDerivatives Method

---



|  |
| --- |
| [Face Class](e32b3b1f-66fc-57cb-6e1c-aa81d1bf3e63.htm)   [See Also](#seeAlsoToggle) |

Returns the second partial derivatives of the face at the specified point.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public FaceSecondDerivatives ComputeSecondDerivatives( 	UV point ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function ComputeSecondDerivatives ( _ 	point As UV _ ) As FaceSecondDerivatives ``` |

 

| Visual C++ |
| --- |
| ``` public: FaceSecondDerivatives^ ComputeSecondDerivatives( 	UV^ point ) ``` |

#### Parameters

point
:   Type:  [Autodesk.Revit.DB UV](1724be37-059b-91ff-aa74-d1508082f76d.htm)    
     The parameters to be evaluated, in natural parameterization of the face.

#### Return Value

The second partial derivatives of the face at the specified point.

# Remarks

It does not take the bounding edge loops into account.

# See Also

[Face Class](e32b3b1f-66fc-57cb-6e1c-aa81d1bf3e63.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)