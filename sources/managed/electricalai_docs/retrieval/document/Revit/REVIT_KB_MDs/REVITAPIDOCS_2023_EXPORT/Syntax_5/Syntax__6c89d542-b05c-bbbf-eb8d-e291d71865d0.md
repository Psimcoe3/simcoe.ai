[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MeshFromGeometryOperationIssue Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Issues encountered while constructing meshes as fallbacks for geometrical operations.

Issues, which can be encountered while building a mesh as a fallback for geometrical operations.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public enum MeshFromGeometryOperationIssue ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration MeshFromGeometryOperationIssue ``` |

 

| Visual C++ |
| --- |
| ``` public enum class MeshFromGeometryOperationIssue ``` |

# Members

| Member name | Description |
| --- | --- |
| AllFine | No issues were encountered. Issues of this type should not be present in MeshFromGeometryOperationResult. |
| NoUsableCurveLoopsInInput | While one or more curve loops were expected as one of the input parameters while building a mesh, no loops containing curves were provided. |
| MissingCurveLoopsInInput | While several curve loops were expected as one of the input parameters while building a mesh, some of them were not provided. |
| EmptyCurveLoopsInInput | Among curve loops expected as input parameters while building a mesh, some are empty. |
| CurveLoopsWithoutCurvesInInput | Among curve loops expected as input parameters while building a mesh, some are not empty, but do not have any curves. |
| NonPlanarProfileLoop | Among curve loops expected as input parameters while building a mesh, some are not planar. |
| InputCurveLoopProblemWithFallback | An unidentified problem with an input curve loop. A fallback is attempted. |
| InputCurveLoopWrongOpenFlag | An input curve has incorrect open flag. |
| NonContinuousInputCurveLoop | A non-continuous input curve loop. Either wrong curve flips or genuine gaps. |
| MissingCurvesInInputLoop | An input curve loop has missing curves. |
| InternalUtilityError | An internal Revit problem. Issues of this type should not normally be present in MeshFromGeometryOperationResult. Please notify Autodesk support if encountered. |
| InternalMissingError | An internal Revit problem. Issues of this type should not be present in TessellatedShapeBuilderResult. Please notify Autodesk support if encountered. |
| InternalError | An internal Revit problem. Issues of this type should not normally be present in MeshFromGeometryOperationResult. Please notify Autodesk support if encountered. |
| NotSetYet | An issue has not been set yet. |
| NumberOfIssueTypes | Not a code of some issue, but the number of known types of issues. Issues of this type should not be present in TessellatedShapeBuilderResult. Please notify Autodesk support if encountered |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)