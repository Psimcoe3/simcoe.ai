[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarShapeConstraintProjectedSegmentLength Members

---



|  |
| --- |
| [RebarShapeConstraintProjectedSegmentLength Class](a41486b4-25c4-c955-f1ab-c585ffb92bd2.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [RebarShapeConstraintProjectedSegmentLength](a41486b4-25c4-c955-f1ab-c585ffb92bd2.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [RebarShapeConstraintProjectedSegmentLength](99ce7f5e-aa7d-479c-db28-ac76699f5c72.htm) | Constructs a new instance of a RebarConstraintProjectEdgedLength object using a shape parameter, direction, and reference types. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](80be3c21-c088-51c7-7d4a-8df7a2554062.htm) | (Inherited from  [RebarShapeConstraint](21c642f3-7aae-759b-4aac-ff4e2dd77d57.htm)  .) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetParamId](bfb42a51-8d55-41f3-aea9-21f60b228923.htm) | Return the Id of the parameter associated with this constraint. (Inherited from  [RebarShapeConstraint](21c642f3-7aae-759b-4aac-ff4e2dd77d57.htm)  .) |
| Public method | [GetSegmentEndReferenceType](b97eb2c5-4cbc-6229-e0c6-968037f007ff.htm) | Choice of two possibilities for the start and end references of the length constraint. |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Direction](ac104515-67aa-8988-1197-ed1093b2ad28.htm) | A vector specifying the direction of the constraint. The direction is fixed, and the shape is always constructed so that the segment direction has a positive dot product with this vector. |
| Public property | [IsValidObject](11bccb40-f634-003a-439b-88308d41d04f.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from  [RebarShapeConstraint](21c642f3-7aae-759b-4aac-ff4e2dd77d57.htm)  .) |
| Public property | [TripleProductSign](328f466e-e8f3-f393-968e-75ca63c9d441.htm) | Sign of the z-coordinate of the cross product of the Direction property with the segment vector. TripleProductSign is 1 if the segment direction is to be on the left of the constraint direction, or -1 if the segment direction is to be on the right. |

# See Also

[RebarShapeConstraintProjectedSegmentLength Class](a41486b4-25c4-c955-f1ab-c585ffb92bd2.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)