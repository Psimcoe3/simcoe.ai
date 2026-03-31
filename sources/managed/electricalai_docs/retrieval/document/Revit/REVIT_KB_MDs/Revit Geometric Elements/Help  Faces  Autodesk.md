---
created: 2026-01-28T21:02:14 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_Faces_html
author: 
---

# Help | Faces | Autodesk

> ## Excerpt
> Faces in the Revit API can be described as mathematical functions of two input parameters “u” and “v”, where the location of the face at any given point in XYZ space is a function of the parameters.

---
Faces in the Revit API can be described as mathematical functions of two input parameters “u” and “v”, where the location of the face at any given point in XYZ space is a function of the parameters.

The U and V directions are automatically determined based on the shape of the given face. Lines of constant U or V can be represented as gridlines on the face, as shown in the example below:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/face_params.png)**U and V gridlines on a cylindrical face**

You can use the UV parameters to evaluate a variety of properties of the face at any given location:

-   Whether the parameter is within the boundaries of the face, using Face.IsInside()
-   The XYZ location of the given face at the specified UV parameter value. This is returned from Face.Evaluate(). If you are also calling ComputeDerivatives(), this is also the .Origin property of the Transform returned by that method.
-   The tangent vector of the given face in the U direction. This is the .BasisX property of the Transform returned by Face.ComputeDerivatives()
-   The tangent vector of the given face in the V direction. This is the .BasisY property of the Transform returned by Face.ComputeDerivatives().
-   The normal vector of the given face. This is the .BasisZ property of the Transform returned by Face.ComputeDerivatives().
-   The second derivative with respect to U. This is the .UUDerivative property of the FaceSecondDerivatives returned by Face.ComputeSecondDerivatives().
-   The second derivative with respect to V. This is the .VVDerivative of the FaceSecondDerivatives returned by Face.ComputeSecondDerivatives().
-   The mixed derivative of the given face. This is the .MixedDerivative of the FaceSecondDerivatives returned by Face.ComputeSecondDerivatives().

All of the vectors returned are non-normalized.
