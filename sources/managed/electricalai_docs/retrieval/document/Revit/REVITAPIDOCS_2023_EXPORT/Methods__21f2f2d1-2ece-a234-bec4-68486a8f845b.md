[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BRepBuilderEdgeGeometry Members

---



|  |
| --- |
| [BRepBuilderEdgeGeometry Class](b0051e1b-8b8b-f819-78c2-67053dd7a241.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [BRepBuilderEdgeGeometry](b0051e1b-8b8b-f819-78c2-67053dd7a241.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method Static member | [Create(Curve)](da8be410-f630-3384-e203-32b81cd0e90c.htm) | Construct BRepBuilderEdgeGeometry based on any GCurve, including GLine and GArc. The curve will be simplified if possible, and the concrete type of the returned value will reflect that simplification: BRepBuilderLinearEdgeGeometry if the curve could be simplified to a line, BRepBuilderArcEdgeGeometry if it could be simplified to an arc, BRepBuilderGenericCurveEdgeGeometry otherwise. |
| Public method Static member | [Create(XYZ, XYZ)](f2d295f0-1ff9-a8c4-d723-6e521fcbab9c.htm) | Constructs a BRepBuilderEdgeGeometry representing a straight line between the two given points. |
| Public method | [Dispose](4ad68cf2-e2e4-b69a-bbfa-bf7f84980c86.htm) | Releases all resources used by the  [BRepBuilderEdgeGeometry](b0051e1b-8b8b-f819-78c2-67053dd7a241.htm) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsValidObject](b5e6346c-5061-37ad-677b-f5db3ccaa6cf.htm) | Specifies whether the .NET object represents a valid Revit entity. |

# See Also

[BRepBuilderEdgeGeometry Class](b0051e1b-8b8b-f819-78c2-67053dd7a241.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)