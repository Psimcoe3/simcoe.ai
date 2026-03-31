---
created: 2026-01-28T20:53:06 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_Displaced_Views_html
author: 
---

# Help | Displaced Views | Autodesk

> ## Excerpt
> Create a displaced view using the DisplacementElement class. DisplacementElement is a view-specific element that can be used to cause elements to appear displaced from their actual location. Displaced views are useful to illustrate the relationship model elements have to the model as a whole. The DisplacementElement does not actually change the location of any model elements; it merely causes them to be displayed in a different location.

---
Create a displaced view using the DisplacementElement class. DisplacementElement is a view-specific element that can be used to cause elements to appear displaced from their actual location. Displaced views are useful to illustrate the relationship model elements have to the model as a whole. The DisplacementElement does not actually change the location of any model elements; it merely causes them to be displayed in a different location.

For a detailed example of creating displaced views, see the DisplacementElementAnimation sample in the Revit SDK.

### Creating a Displaced View

The static DisplacementElement.Create() method c reates a new DisplacementElement. The new DisplacementElement may be a child of a parent DisplacementElement if the parentDisplacementElement parameter is not null. If a parent is specified, the child DisplacementElement's transform will be concatenated with that of the parent, and the displacement of its associated elements will be relative to the parent DisplacementElement.

The Create() method also requires a document, a list of elements to be displaced, the owner view, and t he translation to be applied to the graphics of the displaced elements. An element may only be displaced by a single DisplacementElement in any view. Assigning an element to more than one DisplacementElement will result in an exception.

Other static methods of DisplacementElement can be used prior to calling Create() to help prevent any exceptions. CanCategoryBeDisplaced() tests whether elements belonging to a specific category can be displaced, while the overloaded static method CanElementsBeDisplaced() indicates if specific elements may be assigned to a new DisplacementElement. IsAllowedAsDisplacedElement() tests a single element for eligibility to be displaced.

The static GetAdditionalElementsToDisplace() method will return any additional elements that should be displaced along with the specified element in a specified view. For example, when a wall is displaced, any inserts or hosted elements should also be displaced.

When creating a child DisplacementElement, the static IsValidAsParentInView() can be used to verify a specific DisplacementElement may be used as a parent in a specific View.

Other static methods of DisplacementElement can be used to find the DisplacementElement that includes a specific element, to get a list of all displaced elements in a View, or to get all the DisplacementElements owned by a specified View.

### Working with Displaced Elements

Once a new DisplacementElement has been created, methods are available to obtain any child DisplacementElements, to get the ids of all elements affected by the DisplacementElement, or to obtain the ids of all elements affected by the DisplacementElement as well as any child DisplacementElements. The ParentId property will return the element id of the parent DisplacementElement, if there is one.

After creation, the set of elements affected by the DisplacementElement can be modified using SetDisplacedElementIds() or RemoveDisplacedElement(). Additionally, the relative displacement can be changed.

The method ResetDisplacedElements() will set the translation of the DisplacementElement to (0, 0, 0). The DisplacementElement continues to exist, but its elements are displayed in their actual location.

### Creating a Displaced Path

DisplacementPath is a view-specific annotation related to a DisplacementElement. The DisplacementPath class creates an annotation that depicts the movement of the element from its actual location to its displaced location. The DisplacementPath is anchored to the DisplacementElement by a reference to a point on an edge of a displaced element of the DisplacementElement. It is represented by a single line, or a series of jogged lines, originating at the specified point on the displaced element.

The static DisplacementPath.Create() method requires a document, id of the associated DisplacementElement, a reference that refers to an edge or curve of one of the elements displaced by the DisplacementElement, and a value in the range \[0,1\] that is a parameter along the edge specified. Once created, the path style of the DisplacementPath can get set using the PathStyle property. The anchor point can also be changed using SetAnchorPoint().

The following example creates a new displacement by moving the first wall found vertically and horizontally and then adds a displacement path for it.

| **Code Region: Create displacement and path** |
| --- |
| 
```
public static void CreateDisplacementAndPath(Document doc, View view)
{
    // Find roof
    FilteredElementCollector fec = new FilteredElementCollector(doc);
    fec.OfClass(typeof(RoofBase));
    RoofBase roof = fec.FirstElement() as RoofBase;

    // Get a geometric reference for the path
    Reference edgeRef = GetHorizontalEdgeReference(roof);

    using (Transaction t = new Transaction(doc, "CreateDisplacementAndPath"))
    {
        t.Start();
        // Create a new top level DisplacementElement
        DisplacementElement dispElem = DisplacementElement.Create(doc, new ElementId[] { roof.Id }, new XYZ(10, 0, 20), view, null);

        // Create the path associated to the element
        DisplacementPath.Create(doc, dispElem, edgeRef, 0.5);
        t.Commit();
    }
}

private static Reference GetHorizontalEdgeReference(Element elem)
{
    //Find target edge from lower face of roof
    Options options = new Options();
    options.ComputeReferences = true;

    GeometryElement geomElem = elem.get_Geometry(options);

    foreach (var geomObj in geomElem)
    {
        if (geomObj is Solid)
        {
            Solid solid = geomObj as Solid;
            var faces = solid.Faces;

            foreach (Face face in faces)
            {
                BoundingBoxUV box = face.GetBoundingBox();
                UV midpoint = (box.Min + box.Max) / 2.0;
                if (face.ComputeNormal(midpoint).Normalize().Z < -0.1) // Downward facing, this is good enough
                {
                    var edgeLoops = face.EdgeLoops;
                    foreach (EdgeArray edgeArray in edgeLoops)
                    {
                        foreach (Edge edge in edgeArray)
                        {
                            // horizontal?
                            if (Math.Abs(edge.AsCurve().ComputeDerivatives(0.0, true).BasisX.DotProduct(XYZ.BasisZ)) - 1 <= 0.00001)
                            {
                                return edge.Reference;
                            }
                        }
                    }
                }
            }
        }
    }

    return null;
}
```

 |

The associated DisplacementElement may have a parent DisplacementElement and this parent may have its own parent DisplacementElement, producing a series of ancestors. The terminal point may be the point's original (un-displaced) location, or the corresponding point on any of the intermediate displaced locations corresponding to these ancestor DisplacementElements. The DisplacementPath . AncestorIdx property specifies the end point of the path.
