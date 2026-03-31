[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarShapeDefinitionByArc Members

---



|  |
| --- |
| [RebarShapeDefinitionByArc Class](a92742a5-9781-3691-ec78-5b318fbf5ad3.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [RebarShapeDefinitionByArc](a92742a5-9781-3691-ec78-5b318fbf5ad3.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [RebarShapeDefinitionByArc(Document, RebarShapeDefinitionByArcType)](dcbcb0ed-b1ac-499f-fed0-44d8ff69951b.htm) | Create a non-spiral shape definition. |
| Public method | [RebarShapeDefinitionByArc(Document, Double, Double, Int32, Int32)](5a80585c-198b-040e-f889-481214cceb8f.htm) | Create a spiral shape definition. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddConstraintArcLength](61df5a7c-d82f-88f7-318c-ed602b8ba3b1.htm) | Specify a parameter to drive the arc length of the shape. |
| Public method | [AddConstraintChordLength](0b96af18-bd89-7927-c4e9-012236774f12.htm) | Specify a parameter to drive the chord length (the straight-line distance between the endpoints of the arc). |
| Public method | [AddConstraintCircumference](962fe913-b744-09cd-2f0e-adcac46376c7.htm) | Specify a parameter to drive the circumference of the shape. |
| Public method | [AddConstraintDiameter](d493f0bc-6df5-0304-7dc0-180084d3b434.htm) | Specify a parameter to drive the diameter of the shape. |
| Public method | [AddConstraintRadius](c952aa14-83ea-a21b-6262-fd5128a399a3.htm) | Specify a parameter to drive the radius of the shape. |
| Public method | [AddConstraintSagittaLength](febb3519-72df-7741-e793-21465f9476b1.htm) | Specify a parameter to drive the sagittal length (the height of the circular segment, measured perpendicular to the chord). |
| Public method | [AddFormulaParameter](669bcf80-e0b7-ee57-30c0-82fdf4184012.htm) | Add a formula-driven parameter to the shape definition. (Inherited from  [RebarShapeDefinition](bb1f59be-c95e-a45b-8d2b-8121df179676.htm)  .) |
| Public method | [AddParameter](8e314f3c-3e6c-a3b2-8bd4-68c1fe61b0c4.htm) | Add a parameter to the shape definition. (Inherited from  [RebarShapeDefinition](bb1f59be-c95e-a45b-8d2b-8121df179676.htm)  .) |
| Public method | [CheckDefaultParameterValues](12f60994-60cf-edad-41a0-f8a8b233f75c.htm) | Check that the shape can be solved with the default parameter values. (Inherited from  [RebarShapeDefinition](bb1f59be-c95e-a45b-8d2b-8121df179676.htm)  .) |
| Public method | [Dispose](bfd06e38-ab77-d149-4da0-43ecc8837793.htm) | (Inherited from  [RebarShapeDefinition](bb1f59be-c95e-a45b-8d2b-8121df179676.htm)  .) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetConstraints](0adcf75b-22dd-9672-68a7-9cec782759f5.htm) | Retrieve the list of constraints associated with this definition. |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetParameterDefaultValue](148ee5cc-0ca8-96ca-6b73-91fe86437660.htm) | Return the parameter's default value as stored in the definition. (Inherited from  [RebarShapeDefinition](bb1f59be-c95e-a45b-8d2b-8121df179676.htm)  .) |
| Public method | [GetParameterFormula](0a713eab-1202-249e-cfb3-a9f7796be443.htm) | Return the parameter's formula, if one is associated with it. (Inherited from  [RebarShapeDefinition](bb1f59be-c95e-a45b-8d2b-8121df179676.htm)  .) |
| Public method | [GetParameters](619c0dac-a7f6-5e57-54b2-76370da248f9.htm) | Return the Ids of the shared parameters in the Definition. (Inherited from  [RebarShapeDefinition](bb1f59be-c95e-a45b-8d2b-8121df179676.htm)  .) |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [HasParameter](beb7f2f1-6d94-210c-2928-09bbfa4a1294.htm) | Whether the definition stores the parameter. (Inherited from  [RebarShapeDefinition](bb1f59be-c95e-a45b-8d2b-8121df179676.htm)  .) |
| Public method | [RemoveParameter](78f59d6a-8d6b-cdd9-f045-535e64c007bc.htm) | Remove the parameter from the definition. (Inherited from  [RebarShapeDefinition](bb1f59be-c95e-a45b-8d2b-8121df179676.htm)  .) |
| Public method | [SetArcTypeSpiral](cd7dbab8-c8de-f4ad-2cbe-2d24eb11341f.htm) | Set the RebarShapeDefinitionByArc.Type property to Spiral. |
| Public method | [SetConstraints](250412ee-3cf3-ccba-0cf6-3ee991ac4221.htm) | Assign a new list of constraints to this definition. |
| Public method | [SetParameterDefaultValue](6aef48cc-9b24-d2cc-3890-dda1598a6157.htm) | Change the parameter's value as stored in the definition. (Inherited from  [RebarShapeDefinition](bb1f59be-c95e-a45b-8d2b-8121df179676.htm)  .) |
| Public method | [SetParameterFormula](d1211a0e-cdd6-bfe0-4a08-f58493863d63.htm) | Associate a formula with the parameter. (Inherited from  [RebarShapeDefinition](bb1f59be-c95e-a45b-8d2b-8121df179676.htm)  .) |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Complete](570cadd6-28ca-7828-dd6a-0e4bcb53256a.htm) | Report whether the shape definition is fully constrained. (Inherited from  [RebarShapeDefinition](bb1f59be-c95e-a45b-8d2b-8121df179676.htm)  .) |
| Public property | [IsPlanar](a401ad32-ed12-66d3-2f50-09039d112c25.htm) | Reports whether the shape definition lies within a plane: false if a spiral, true in all other cases. (Inherited from  [RebarShapeDefinition](bb1f59be-c95e-a45b-8d2b-8121df179676.htm)  .) |
| Public property | [IsValidObject](47e5ab9c-5b4a-fc69-6745-89b296cc0900.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from  [RebarShapeDefinition](bb1f59be-c95e-a45b-8d2b-8121df179676.htm)  .) |
| Public property | [Type](55d48817-1a60-05eb-dfeb-d053ac80328e.htm) | Among those rebar shapes defined by an arc, specify which kind. |

# See Also

[RebarShapeDefinitionByArc Class](a92742a5-9781-3691-ec78-5b318fbf5ad3.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)