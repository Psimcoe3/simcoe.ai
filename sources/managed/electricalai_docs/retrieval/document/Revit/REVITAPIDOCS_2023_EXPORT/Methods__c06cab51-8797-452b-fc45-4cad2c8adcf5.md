[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TessellatedShapeBuilderResult Members

---



|  |
| --- |
| [TessellatedShapeBuilderResult Class](16e1e032-d9fd-2708-0704-ed00b0b85441.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [TessellatedShapeBuilderResult](16e1e032-d9fd-2708-0704-ed00b0b85441.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](c6fe4067-905b-9f4a-7403-ec7ee52a5ca7.htm) | Releases all resources used by the  [TessellatedShapeBuilderResult](16e1e032-d9fd-2708-0704-ed00b0b85441.htm) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetGeometricalObjects](3c5c4efb-8960-869f-76c0-338979e5a484.htm) | When called the first time, returns geometrical objects which were built. Later calls will throw exceptions. |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetIssuesForFaceSet](9063460c-2dd8-a00e-6519-8733117870cb.htm) | Returns the array of issues encountered while processing a face set with index 'setIndex'. |
| Public method | [GetNumberOfFaceSets](c5e36953-ef39-f868-f49b-313db8055bcc.htm) | Gets number of face sets for which 'this' result was obtained. |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [AreObjectsAvailable](ea616568-4dc6-0ea7-8bf9-f0d91d4fca66.htm) | Shows whether 'issues' still contains the original data or whether these data have already been relinquished by 'getGeometricalObjects'. The former is true, the later is false. |
| Public property | [HasInvalidData](032f5f15-04f3-1257-14a2-2eb47d7bdf36.htm) | Whether there were any inconsistencies in the face sets, stored in the tessellated shape builder while building geometrical objects. |
| Public property | [IsValidObject](8b8076fd-3775-a91b-40f2-fb7145028d66.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [Outcome](2da60445-35fa-81b1-e3df-e56f0ec408a1.htm) | What kinds of geometrical objects were built. |

# See Also

[TessellatedShapeBuilderResult Class](16e1e032-d9fd-2708-0704-ed00b0b85441.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)