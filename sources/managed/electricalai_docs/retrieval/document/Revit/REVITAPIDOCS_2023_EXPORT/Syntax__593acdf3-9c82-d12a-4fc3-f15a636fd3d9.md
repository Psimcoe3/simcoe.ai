[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetModelToProjectionTransforms Method

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

Gets the transforms from the model space to the view projection space.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public IList<TransformWithBoundary> GetModelToProjectionTransforms() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetModelToProjectionTransforms As IList(Of TransformWithBoundary) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<TransformWithBoundary^>^ GetModelToProjectionTransforms() ``` |

#### Return Value

The transformations from the model space to view projection space.

# Remarks

Model space is the global 3D coordinate space in which the geometry of the model lives.

View projection space is the 3D Euclidean space with a coordinate system such that X and Y are horizontal and vertical directions in the view projection plane and Z is the cross product of X and Y. Distances in the projection space are the same as would be measured on paper if the view is printed without additional scaling.

Most views will return just one  [TransformWithBoundary](5d7db6ff-8538-2c84-8e39-d683e0de9ca5.htm)  . The exceptions are views with split crop regions. Split crop regions can be independently moved and therefore each region of a split crop gets its own transform and boundary. You can check if a view has split crop regions by getting the  [ViewCropRegionShapeManager](2610cb66-5dae-9fc8-4e83-7dfe88085abb.htm)  and calling  [!:ViewCropRegionShapeManager.IsSplit()]  .

When the view's crop region is split, many TransformWithBoundary objects will be returned. Each TransformWithBoundary corresponds to one region of the split crop. To determine which TransformWithBoundary to use when converting a model point into view projection space, first test to see which split crop region boundary contains the model point. See  [!:TransformWithBoundary.GetBoundary()]  .

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The view does not return transforms. -or- The view is a perspective view. |

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)