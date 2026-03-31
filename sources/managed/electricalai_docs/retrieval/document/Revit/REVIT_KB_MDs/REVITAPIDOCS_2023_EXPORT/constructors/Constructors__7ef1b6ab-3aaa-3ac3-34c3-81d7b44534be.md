[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BoundingBoxIntersectsFilter Members

---



|  |
| --- |
| [BoundingBoxIntersectsFilter Class](1fbe1cff-ed94-4815-564b-05fd9e8f61fe.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [BoundingBoxIntersectsFilter](1fbe1cff-ed94-4815-564b-05fd9e8f61fe.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [BoundingBoxIntersectsFilter(Outline)](3a1c089f-082f-e0f6-fc80-68a3c60db8ef.htm) | Constructs a new instance of a filter to match elements with a bounding box that intersects the given Outline. |
| Public method | [BoundingBoxIntersectsFilter(Outline, Boolean)](608e7bd7-432c-9b73-de4f-d17d8aa6cce3.htm) | Constructs a new instance of a filter to match elements with a bounding box that intersects the given Outline, with the option to invert the filter and match all elements with a bounding box that are not intersecting the given Outline. |
| Public method | [BoundingBoxIntersectsFilter(Outline, Double)](12de85f3-3aa7-fcb9-eda1-7744b052e442.htm) | Constructs a new instance of a filter to match elements with a bounding box that intersects the given Outline. |
| Public method | [BoundingBoxIntersectsFilter(Outline, Double, Boolean)](be97c617-d4b7-54d8-545e-a3fd9647f73c.htm) | Constructs a new instance of a filter to match elements with a bounding box that intersects the given Outline, with the option to invert the filter and match all elements with a bounding box that are not intersecting the given Outline. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](5d3ffdf8-dce9-0724-d101-44693775671c.htm) | (Inherited from  [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)  .) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetBoundingBox](2b287737-ceae-f54f-fccf-7012fd9b6703.htm) | Gets the outline being used for this filter. |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [PassesFilter(Element)](1402f6e0-995c-2644-c7a9-7016a81a4ef4.htm) | Applies the filter to a given element. (Inherited from  [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)  .) |
| Public method | [PassesFilter(Document, ElementId)](a8e86084-b91f-c3cf-c334-e163168328d6.htm) | Applies the filter to a given element. (Inherited from  [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)  .) |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Inverted](ceab2eea-cc4c-d7dc-b34c-b3c1f012eda1.htm) | True if the results of the filter are inverted; elements that would normally be accepted by this filter will be rejected, and elements that would normally be rejected will be accepted. (Inherited from  [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)  .) |
| Public property | [IsValidObject](027ccc75-b7f6-4ee2-cf98-563df96b0dbb.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from  [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)  .) |
| Public property | [Tolerance](2c9269cc-09c6-576a-ddf9-7f0599088944.htm) | Allows control over the match criteria by using a tolerance in the geometry comparison. It is suggested to use this in cases where trivial differences should be considered when matching elements. |

# See Also

[BoundingBoxIntersectsFilter Class](1fbe1cff-ed94-4815-564b-05fd9e8f61fe.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)