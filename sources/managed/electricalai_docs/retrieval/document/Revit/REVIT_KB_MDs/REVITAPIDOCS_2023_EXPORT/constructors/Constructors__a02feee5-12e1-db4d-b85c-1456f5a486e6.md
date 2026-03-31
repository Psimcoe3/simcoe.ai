[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Outline Members

---



|  |
| --- |
| [Outline Class](1ffe9215-0dd5-358f-495d-e983f9e7d295.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [Outline](1ffe9215-0dd5-358f-495d-e983f9e7d295.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [Outline(Outline)](173fe602-1227-907f-a555-eec914b25009.htm) | Constructs a new copy of the input Outline object. |
| Public method | [Outline(XYZ, XYZ)](7be638d8-f794-3247-89d0-39602b2b3f90.htm) | Constructor that uses a minimum and maximum XYZ point to initialize the outline. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddPoint](7338e8cf-442e-9623-b348-a44f904a6f9a.htm) | Adds a point to the bounding box, expanding it if the point is outside the existing boundary. |
| Public method | [Contains](3e10329e-4114-73f7-65a6-17bf40056be9.htm) | Determine if this Outline contains the specified point to within a tolerance. |
| Public method | [ContainsOtherOutline](3fd3d671-4127-c849-e684-6b8697aaa778.htm) | Determine if this Outline contains another Outline to within tolerance. |
| Public method | [Dispose](d96f78d8-4cca-f6f9-c605-f3330453d937.htm) | Releases all resources used by the  [Outline](1ffe9215-0dd5-358f-495d-e983f9e7d295.htm) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetDiagonalLength](430fa61d-2390-f491-774f-486e4975cf78.htm) | Get the length of outline's diagonal. If called on empty outline, 0. is returned |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [Intersects](2c32184b-515c-7597-335b-17f44435b7ab.htm) | Determine if this Outline intersects the input Outline to within a specified tolerance. |
| Public method | [IsScaleValid](6d5c1fa3-8b4d-4cd8-7730-62df951bc03d.htm) | Checks if given scale is valid. Should be greater than zero. |
| Public method | [Scale](7f4644d9-6012-63f7-dff6-8ec4273aeb3b.htm) | Scales the bounding box by given scale. |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsEmpty](989ebb7b-34dd-3a36-0122-6d1ec517cfa8.htm) | Identifies if the outline represents an empty outline. |
| Public property | [IsValidObject](c11d11e9-7d8d-1966-68b1-f097a46383e4.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [MaximumPoint](c615ccfc-a501-c9db-bbc2-15fb11723ce0.htm) | The maximum point of the bounding box. |
| Public property | [MinimumPoint](0c0ea870-876d-9404-3da1-bf5d82d9d71a.htm) | The minimum point of the bounding box. |

# See Also

[Outline Class](1ffe9215-0dd5-358f-495d-e983f9e7d295.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)