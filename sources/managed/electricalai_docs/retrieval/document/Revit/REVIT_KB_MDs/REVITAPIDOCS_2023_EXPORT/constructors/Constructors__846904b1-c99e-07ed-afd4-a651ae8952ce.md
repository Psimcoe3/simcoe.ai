[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IFCExtrusionCreationData Members

---



|  |
| --- |
| [IFCExtrusionCreationData Class](9447a335-6861-0533-6896-e6ff1fd41761.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [IFCExtrusionCreationData](9447a335-6861-0533-6896-e6ff1fd41761.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [IFCExtrusionCreationData](1526b1df-8abf-df78-55a7-241b95043513.htm) | The default constructor. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddOpening](55c7a07d-e4a0-2a58-1beb-2b858767265b.htm) | Adds an opening to the data. |
| Public method | [ClearOpenings](a72eec8f-83c7-c53c-04fd-c49650c3c20d.htm) | Removes all cached openings from the data. |
| Public method | [Dispose](bdb0d5dd-bee1-23e9-6bca-ebf29f38c3eb.htm) | Releases all resources used by the  [IFCExtrusionCreationData](9447a335-6861-0533-6896-e6ff1fd41761.htm) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetLocalPlacement](faf76fac-5c98-193d-5fe0-aa7724898564.htm) | Gets the reference to the IfcLocalPlacement handle used when creating the extrusion. |
| Public method | [GetOpenings](a338038d-e7d2-d89e-bad5-5249dbf63baa.htm) | Gets a collection of all of the openings stored in this data. |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [SetLocalPlacement](0053794b-01e0-bc6e-ff1c-f78b16be0c71.htm) | Sets the data to reference an IfcLocalPlacement handle when creating the extrusion. Side effect: will set ReuseLocalPlacement to true. |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [AllowVerticalOffsetOfBReps](903dec76-11dd-2302-4a93-e6ea12910f26.htm) | Allows vertical shifting of breps when moving towards the origin. |
| Public property | [AreInnerRegionsOpenings](5f33204d-6147-d044-2e34-bb9f3168a2b6.htm) | True if inner regions of the extrusion should become openings, false otherwise. |
| Public property | [CustomAxis](080c7d43-0546-b996-b0f1-6ca0ad79bc53.htm) | The custom extrusion axis to try when generating an extrusion. |
| Public property | [ExtrusionDirection](5f5c831f-f0dd-f46a-028c-dd0d6ac09123.htm) | The extrusion direction to generate an extrusion. |
| Public property | [ForceOffset](f30370e6-0b0f-2e41-ac1e-d54fa189c672.htm) | True to create new local placement with identity transform. |
| Public property | [HasCustomAxis](c40ae541-f0bc-fc8d-3fa8-5a40a5183d34.htm) | Identifies if the data contains a custom extrusion axis. |
| Public property | [HasExtrusionDirection](7b1c95e7-5d86-5151-9969-0beaf98b7d89.htm) | Identifies if the data contains a extrusion direction. |
| Public property | [IsValidObject](51dcad87-fd8f-4776-ed1c-e9cdd6dd808f.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [PossibleExtrusionAxes](ce756e53-f2a1-190d-0004-d0ba6d6e7988.htm) | The axes to try when generating the properties of the extrusion. |
| Public property | [ReuseLocalPlacement](85c18673-c186-4313-a063-9658072de7fa.htm) | Allows re-use of local placement when creating a new local placement due to shifting of breps when moving towards the origin. |
| Public property | [ScaledArea](02b42f72-06de-b50c-b542-943aef85958d.htm) | The area of the extrusion, scaled to the units of export. |
| Public property | [ScaledHeight](a6b5d0b7-3cfa-b9db-a273-e2aac2360a57.htm) | The height of the extrusion, scaled to the units of export. |
| Public property | [ScaledInnerPerimeter](81db0c0e-c1df-7b1c-736e-04ccb1a4f134.htm) | The inner perimeter of the extrusion, scaled to the units of export. |
| Public property | [ScaledLength](8c1426ed-4987-665a-0dad-01cd4e8605b7.htm) | The length of the extrusion, scaled to the units of export. |
| Public property | [ScaledOuterPerimeter](c9e65d57-e306-0549-4b52-91eb47926b8a.htm) | The outer perimeter of the extrusion, scaled to the units of export. |
| Public property | [ScaledWidth](0311bde5-b7c0-b381-4981-d9bab8b9727a.htm) | The width of the extrusion, scaled to the units of export. |
| Public property | [Slope](881d9da7-e457-8116-0fc1-2340037a04bb.htm) | The slope of the extrusion, in degrees. |

# See Also

[IFCExtrusionCreationData Class](9447a335-6861-0533-6896-e6ff1fd41761.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)