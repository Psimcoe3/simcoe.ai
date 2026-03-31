[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReferenceIntersector Members

---



|  |
| --- |
| [ReferenceIntersector Class](36f82b40-1065-2305-e260-18fc618e756f.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [ReferenceIntersector](36f82b40-1065-2305-e260-18fc618e756f.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [ReferenceIntersector(View3D)](ba15191c-61f4-bf9e-72d7-d0f4976fd3f3.htm) | Constructs a ReferenceIntersector which is set to return intersections from all elements and representing all reference target types. |
| Public method | [ReferenceIntersector(ElementFilter, FindReferenceTarget, View3D)](929ca688-af0f-6e6a-d812-44017c8955e7.htm) | Constructs a ReferenceIntersector which is set to return intersections from any element which passes an input filter. |
| Public method | [ReferenceIntersector(ElementId, FindReferenceTarget, View3D)](80392f86-eab8-7485-6e5a-28d4e40f7528.htm) | Constructs a ReferenceIntersector which is set to return intersections from a single target element only. |
| Public method | [ReferenceIntersector(ICollection ElementId , FindReferenceTarget, View3D)](4b624cc1-fc7f-62dd-3593-22861c991afd.htm) | Constructs a ReferenceIntersector which is set to return intersections from any of a set of target elements. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](4bad58d0-1ed4-176b-81cc-3a0181744ebe.htm) | Releases all resources used by the  [ReferenceIntersector](36f82b40-1065-2305-e260-18fc618e756f.htm) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [Find](6abd0586-5d7e-68c6-2e64-46199f457499.htm) | Projects a ray from the origin along the given direction, and returns all references from intersected elements which match the ReferenceIntersector's criteria. |
| Public method | [FindNearest](866e1f2b-c79a-4d9f-1db1-9e386dd42941.htm) | Projects a ray from the origin along the given direction, and returns the nearest reference from intersected elements which match the ReferenceIntersector's criteria. |
| Public method | [GetFilter](614c9ce9-9918-b551-a4f1-552030cdb0c9.htm) | Gets the ElementFilter used in intersection testing. |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetTargetElementIds](ec2affbb-5386-cdc6-b89c-e3605dbe7f64.htm) | Gets the set of ElementIds to test from in intersection testing. |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [SetFilter](e94fc91b-34fb-f12b-ecd7-d9c30de9a7dd.htm) | Sets the ElementFilter used in intersection testing. |
| Public method | [SetTargetElementIds](600d7702-878d-26ed-e3db-d70b05bb3c6c.htm) | Sets the set of ElementIds to test from in intersection testing. |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [FindReferencesInRevitLinks](027d8736-697e-ebe8-37d9-901f96713540.htm) | Determines if references inside Revit Links should be found. |
| Public property | [IsValidObject](4c356722-e215-f7a3-1e4a-728e09229955.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [TargetType](c7a99118-5365-2baf-2494-1879cb06038e.htm) | The type of reference to find. |
| Public property | [ViewId](502978f2-9efb-02a9-ab6e-f54eafbe6c10.htm) | The id of the 3D view used for evaluation. |

# See Also

[ReferenceIntersector Class](36f82b40-1065-2305-e260-18fc618e756f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)