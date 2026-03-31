---
created: 2026-01-28T21:10:13 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Analytical_Model_html
author: 
---

# Help | Analytical Model | Autodesk

> ## Excerpt
> In structural engineering, an analytical model is the engineering description of a structural physical model. The Analytical Model is an essential part of BIM data and is subject to collaborative workflows within engineering teams and across project teams. The Analytical Model implementation in Revit enables engineers to:

---
In structural engineering, an analytical model is the engineering description of a structural physical model. The Analytical Model is an essential part of BIM data and is subject to collaborative workflows within engineering teams and across project teams. The Analytical Model implementation in Revit enables engineers to:

-   Have freedom of analytical modeling to reflect their individual design decisions with respect to structural elements and buildings/structures seen as whole systems.
-   Analytically represent any types of structure
-   Create consistent Analytical Models enabling structural analysis jobs from Revit models
-   Perform full bi-directional workflow with analysis software and capture model modifications made there
-   Preserve Analytical Model from unexpected changes if needed
-   Create multiple analytical models reflecting diverse analysis types and configurations
-   Replicate the ease of analytical modeling like in dedicated structural analysis software, combined with the power of parametric and collaboration enabling BIM platform.

## AnalyticalElement

AnalyticalElement represents the base class for all analytical objects.

-   Transform GetTransform() - Returns the transform which reflects Analytical Element orientation.
-   AnalyzeAs AnalyzeAs - This represents the Analyze As parameter assigned to Analytical Element.
-   Reference GetReference(AnalyticalModelSelector selector) - Returns a reference to a given curve within the Analytical Element.
-   ElementId MaterialId - Defines the Material Id for the Analytical Element.

## AnalyticalMember

AnalyticalMember represents a linear element in the structural analytical model.

-   AnalyticalMember Create(Document document, Curve curve) - Method which creates a new instance of an Analytical Member within the project
-   AnalyticalStructuralRole StructuralRole - The structural role assigned to the Analytical Member
-   Curve GetCurve() - Returns the curve of the Analytical Member.
-   void SetCurve(Curve curve) - Sets the curve for the Analytical Member. This method disconnects elements from other analytical elements (if the end nodes are in the same position). If the user wants to move the corner, and keep the connection, there are other ways for achieving that like ElementTransformUtils.moveElements.
-   bool IsValidCurve(Curve curve) - Verifies if the curve is valid for an Analytical Member
-   void FlipCurve() - Flips the ends of the Analytical Member
-   StructuralSectionShape StructuralSectionShape - The structural section shape of the Analytical Member (read only)
-   ElementId SectionType - The id of the type from the structural Family assigned to the Analytical Member
-   double CrossSectionRotation - Cross section rotation of the Analytical Member

## AnalyticalPanel

AnalyticalPanel represents a surface in the structural analytical model.

-   AnalyticalPanel Create(Document document, CurveLoop curveLoop) - Method which creates a new instance of an Analytical Panel within the project.
-   CurveLoop GetOuterContour() - Returns the Curve Loop that defines the geometry of the Analytical Surface element
-   bool IsCurveLoopValid(CurveLoop profile) - Checks if curve loop is valid for Analytical Panel
    -   To modify Analytical Panel geometry, users should use SketchEditScope framework.
    -   void StartWithNewSketch(ElementId elementId) - Starts a sketch edit mode for an element which, at this moment, doesn't have a sketch. Another way of editing geometry is SetOuterContour(CurveLoop outerContour) - Sets the Curve Loop that defines the geometry of the Analytical Surface element Like for AnalyticalMember, setting the contour for analytical panel will break the connection with other analytical elements. If the user wants to move the corner, and keep the connection, there are other ways for achieving that like ElementTransformUtils.MoveElements.
-   `ISet<ElementId> GetAnalyticalOpeningsIds()` - Returns the Analytical Openings Ids of the Analytical Panel
-   ElementId SketchId - Sketch associated to this Revit element
-   AnalyticalStructuralRole StructuralRole - Structural role assigned to the Analytical Panel

## AnalyticalOpening

AnalyticalOpening is an element which represents an opening in an Analytical Panel.

-   AnalyticalOpening Create(Document doc, CurveLoop curveLoop, ElementId panelId) - Method which creates a new instance of an Analytical Opening within the project
-   CurveLoop GetOuterContour() - Returns the Curve Loop that defines the geometry of the Analytical Surface element
-   bool IsCurveLoopValidForAnalyticalOpening(CurveLoop loop, Document document, ElementId panelId) - Checks if curve loop is valid for Analytical Opening To modify Analytical Opening geometry, you should use SketchEditScope framework. Another way to modify Analytical Opening geometry is: void SetOuterContour(CurveLoop outerContour) - Sets the Curve Loop that defines the geometry of the Analytical Surface element.
-   ElementId PanelId - ElementId of the host Analytical Panel.
-   ElementId SketchId - Sketch associated to this Revit element

## AnalyticalToPhysicalAssociationManager

AnalyticalToPhysicalAssociationManager manages the associations between analytical and physical elements. In the past solution, the elements itself knew about each other and the user had no control over it (the association could not be modified). With this new approach, the association can be edited. Revit supports 1-1 association and elements cannot be part of multiple associations at the same time.

-   AnalyticalToPhysicalAssociationManager GetAnalyticalToPhysicalAssociationManager(Document doc) Returns the AnalyticalToPhysicalAssociationManager for this document
-   void AddAssociation(ElementId analyticalElementId, ElementId physicalElementId) - Adds a new association between an analytical element and a physical element.
-   void RemoveAssociation(ElementId elementId) - This method will remove the association for the element with the given ElementId.
-   ElementId GetAssociatedElementId(ElementId elementId) - Returns id of the element which is associated with the given ElementId.
-   bool HasAssociation(ElementId id) - Verifies if the element has already defined an association

## AnalyticalNodeData

The AnalyticalNodeData class holds information about connection status of analytical nodes.

-   AnalyticalNodeData GetAnalyticalNodeData(Element element) - Returns AnalyticalNodeData associated with this element, if it exists.
-   AnalyticalNodeConnectionStatus GetConnectionStatus() - Returns the Connections Status for an Analytical Node.

## Loads

-   LineLoad.Create(Document document, ElementId hostElemId, XYZ forceVector1, XYZ momentVector1, LineLoadType symbol)
-   LineLoad.Create(Document document, ElementId hostElemId, int curveIndex, XYZ forceVector1, XYZ momentVector1, Structure.LineLoadType symbol)
-   LineLoad.IsValidHostId(Document doc, ElementId hostElemId)
-   AreaLoad.IsValidHostId(Document doc, ElementId hostElemId)
-   AreaLoad.Create(Document doc, ElementId hostElemId, XYZ forceVector1, AreaLoadType symbol)
-   PointLoad.Create(Document doc, ElementId hostElemId, AnalyticalElementSelector selector, XYZ forceVector, XYZ momentVector, AreaLoadType symbol)
-   PointLoad.IsValidHostId(Document doc, ElementId hostElemId)
