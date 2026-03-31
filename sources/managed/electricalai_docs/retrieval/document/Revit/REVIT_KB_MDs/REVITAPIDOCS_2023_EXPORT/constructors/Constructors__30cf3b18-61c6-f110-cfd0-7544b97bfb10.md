[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Frame Members

---



|  |
| --- |
| [Frame Class](d44b3fd1-34d0-bfd0-55f6-de24235edf2e.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [Frame](d44b3fd1-34d0-bfd0-55f6-de24235edf2e.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [Frame](c7377867-7820-d794-dc11-83dae15a3a19.htm) | Default constructor. Uses global origin and standard basis vectors. |
| Public method | [Frame(XYZ, XYZ, XYZ, XYZ)](54dba681-7199-f73f-2908-9bbe54689f6d.htm) | Constructor that takes the frame's base point and three basis vectors. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method Static member | [CanDefineRevitGeometry](49a621dd-b76c-d0b2-7850-a846a14edbfe.htm) | Tests whether the supplied Frame object may be used to define a Revit curve or surface. In order to satisfy the requirements the Frame must be orthonormal and its origin is expected to lie within the Revit design limits  [IsWithinLengthLimits(XYZ)](ac2171af-4250-8a30-faa7-4d7030d29a03.htm)  . |
| Public method | [Dispose](01664e31-f00c-d00b-4b5a-ae563a69e73b.htm) | Releases all resources used by the  [Frame](d44b3fd1-34d0-bfd0-55f6-de24235edf2e.htm) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [IsOrthogonal](50351f59-56cc-0e6a-9db6-02b6b5cb0f21.htm) | Determines if this frame's basis vectors are orthogonal. |
| Public method | [IsOrthonormal](8ef3b2a0-119d-12c1-9e13-a3a878e76580.htm) | Determines if this frame's basis vectors are orthonormal. |
| Public method | [IsRightHanded](9a9727f4-270c-f6b0-60ce-482889e15213.htm) | Determine if this frame's basis is right-handed. |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [Transform](50ef89f7-1c5b-46ad-a33d-911b6834f8e6.htm) | Applies the input transform to this frame. |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [BasisX](b28df9ee-1363-aa44-8a8f-db0c631dd797.htm) | The first basis vector of the frame. |
| Public property | [BasisY](129f694e-8943-2999-3d2f-25d19a3bb9f2.htm) | The second basis vector of the frame. |
| Public property | [BasisZ](b0d0e152-5f46-cbb0-bf2c-8f90b4ef59ee.htm) | The third basis vector of the frame. |
| Public property | [IsValidObject](46ce3715-590e-d9b3-4ad0-a3e739961a66.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [Origin](7899dacb-82bb-f1a6-b2fb-786aa2792f6f.htm) | The frame's base point. |

# See Also

[Frame Class](d44b3fd1-34d0-bfd0-55f6-de24235edf2e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)