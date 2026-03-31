---
created: 2026-01-28T21:15:42 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Analysis_Detailed_Energy_Analysis_Model_html
author: 
---

# Help | Detailed Energy Analysis Model | Autodesk

> ## Excerpt
> The Autodesk.Revit.DB.Analysis namespace includes several classes to obtain and analyze the contents of a project's detailed energy analysis model.

---
The Autodesk.Revit.DB.Analysis namespace includes several classes to obtain and analyze the contents of a project's detailed energy analysis model.

The Export to gbXML and the Heating and Cooling Loads features produce an analytical thermal model from the physical model of a building. The analytical thermal model is composed of spaces, zones and planar surfaces that represent the actual volumetric elements of the building.

The classes related to the detailed energy analysis model are:

-   EnergyAnalysisDetailModel
-   EnergyAnalysisDetailModelOptions
-   EnergyAnalysisOpening
-   EnergyAnalysisSpace
-   EnergyAnalysisSurface
-   Polyloop
    
    ### Energy analysis model creation
    

Use the static method EnergyAnalysisDetailModel.Create() to create and populate the energy analysis model. The EnergyAnaysisDetailModel is stored as an element in the Revit model, and thus the EnergyAnalysisDetailModel.Create() method requires there to be an open transaction. The generated model is always returned in world coordinates, but the method TransformModel() transforms all surfaces in the model according to ground plane, shared coordinates and true north.

If an energy analysis model is already created, the static method EnergyAnalysisDetailModel.GetMainEnergyAnalysisDetailModel() returns the main EnergyAnalysisDetailModel contained in the given document (or null if none has been created). The energy analysis detail model can be displayed in associated views.

Set the appropriate options using the EnergyAnalysisDetailModelOptions class.

The options available when creating the energy analysis detail model include:

-   The level of computation for energy analysis model - NotComputed, FirstLevelBoundaries, meaning analytical spaces and zones, SecondLevelBoundaries, meaning analytical surfaces, or Final, meaning constructions, schedules, and non-graphical data
-   Whether the energy model is based on rooms/spaces or building elements
-   Whether mullions should be exported as shading surfaces
-   Whether shading surfaces will be included
-   Whether to simplify curtain systems - When true, a single large window/opening will be exported for a curtain wall/system regardless of the number of panels in the system

The EnergyAnalysisDetailModelOptions.EnergyModelType property can be set to SpatialElement (where the energy model is based on rooms or spaces) or BuildingElement (where the energy model is based on analysis of building element volumes). However, note that the generated energy model is also affected by settings in EnergyDataSettings, including the EnergyDataSettings.AnalysisType property. If this property is set to AnalysisMode.ConceptualMassesAndBuildingElements, the EnergyAnalysisDetailModel will use the combination of conceptual masses and building elements.

The following example creates a new energy analysis detailed model from the physical model then displays the originating element for each surface of each space in the model.

<table summary="" id="GUID-471B3969-42E7-436C-8DD3-C5ED18DD9209__TABLE_1A78873357B14703BD52913F64102E94"><tbody><tr><td><b>Code Region: Energy Analysis Detail Model</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetThermalModelData</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Collect space and surface data from the building's analytical thermal model</span><span>
    </span><span>EnergyAnalysisDetailModelOptions</span><span> options </span><span>=</span><span> </span><span>new</span><span> </span><span>EnergyAnalysisDetailModelOptions</span><span>();</span><span>
    options</span><span>.</span><span>Tier</span><span> </span><span>=</span><span> </span><span>EnergyAnalysisDetailModelTier</span><span>.</span><span>Final</span><span>;</span><span> </span><span>// include constructions, schedules, and non-graphical data in the computation of the energy analysis model</span><span>
    options</span><span>.</span><span>EnergyModelType</span><span> </span><span>=</span><span> </span><span>EnergyModelType</span><span>.</span><span>SpatialElement</span><span>;</span><span>   </span><span>// Energy model based on rooms or spaces</span><span>

    </span><span>EnergyAnalysisDetailModel</span><span> eadm </span><span>=</span><span> </span><span>EnergyAnalysisDetailModel</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> options</span><span>);</span><span> </span><span>// Create a new energy analysis detailed model from the physical model</span><span>
    </span><span>IList</span><span>&lt;</span><span>EnergyAnalysisSpace</span><span>&gt;</span><span> spaces </span><span>=</span><span> eadm</span><span>.</span><span>GetAnalyticalSpaces</span><span>();</span><span>
    </span><span>StringBuilder</span><span> builder </span><span>=</span><span> </span><span>new</span><span> </span><span>StringBuilder</span><span>();</span><span>
    builder</span><span>.</span><span>AppendLine</span><span>(</span><span>"Spaces: "</span><span> </span><span>+</span><span> spaces</span><span>.</span><span>Count</span><span>);</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>EnergyAnalysisSpace</span><span> space </span><span>in</span><span> spaces</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>SpatialElement</span><span> spatialElement </span><span>=</span><span> doc</span><span>.</span><span>GetElement</span><span>(</span><span>space</span><span>.</span><span>CADObjectUniqueId</span><span>)</span><span> </span><span>as</span><span> </span><span>SpatialElement</span><span>;</span><span>
        </span><span>ElementId</span><span> spatialElementId </span><span>=</span><span> spatialElement </span><span>==</span><span> </span><span>null</span><span> </span><span>?</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span> </span><span>:</span><span> spatialElement</span><span>.</span><span>Id</span><span>;</span><span>
        builder</span><span>.</span><span>AppendLine</span><span>(</span><span>"   &gt;&gt;&gt; "</span><span> </span><span>+</span><span> space</span><span>.</span><span>SpaceName</span><span> </span><span>+</span><span> </span><span>" related to "</span><span> </span><span>+</span><span> spatialElementId</span><span>);</span><span>
        </span><span>IList</span><span>&lt;</span><span>EnergyAnalysisSurface</span><span>&gt;</span><span> surfaces </span><span>=</span><span> space</span><span>.</span><span>GetAnalyticalSurfaces</span><span>();</span><span>
        builder</span><span>.</span><span>AppendLine</span><span>(</span><span>"       has "</span><span> </span><span>+</span><span> surfaces</span><span>.</span><span>Count</span><span> </span><span>+</span><span> </span><span>" surfaces."</span><span>);</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>EnergyAnalysisSurface</span><span> surface </span><span>in</span><span> surfaces</span><span>)</span><span>
        </span><span>{</span><span>
            builder</span><span>.</span><span>AppendLine</span><span>(</span><span>"            +++ Surface from "</span><span> </span><span>+</span><span> surface</span><span>.</span><span>OriginatingElementDescription</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"EAM"</span><span>,</span><span> builder</span><span>.</span><span>ToString</span><span>());</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

After creating the EnergyAnalysisDetailModel, the spaces, openings and surfaces associated with it can be retrieved with the GetAnalyticalOpenings(), GetAnalyticalSpaces(), GetAnalyticalShadingSurfaces() and GetAnalyticalSurfaces() methods.

It is recommended that applications call Document.Delete() on the EnergyAnalysisDetailModel elements that they create when finished accessing the data, but any energy models created after the main energy model will be deleted automatically before document saving or synchronization.

### EnergyAnalysisSpace

From an EnergyAnalysisSpace you can retrieve the collection of EnergyAnalysisSurfaces which define an enclosed volume bounded by the center plane of walls and the top plane of roofs and floors. Alternatively, GetClosedShell() retrieves a collection of Polyloops, which are planar polygons, that define an enclosed volume measured by interior bounding surfaces. For two-dimensions, use GetBoundary() which returns a collection of Polyloops representing the 2D boundary of the space that defines an enclosed area measured by interior bounding surfaces.

The EnergyAnalysisSpace class also has a number of properties for accessing information about the analysis space, such as AnalyticalVolume, SpaceName and Area.

### EnergyAnalysisSurface

From an EnergyAnalysisSpace you can retrieve the primary analysis space associated with the surface as well as the secondary adjacent analytical space. The GetAnalyticalOpenings() method will retrieve a collection of all analytical openings in the surface. The GetPolyloop() method obtains the planar polygon describing the surface geometry as described in gbXML.

The EnergyAnalysisSurface class has numerous properties to provide more information about the analytical surface, such as Height, Width, Corner (lower-left coordinate for the analytical rectangular geometry viewed from outside), and an originating element description.

The surface type is available either as an EnergyAnalysisSurfaceType or as a gbXMLSurfaceType. The gbXML surface type attribute is determined by the source element and the number of space adjacencies. Possible types are:

<table summary="" id="GUID-471B3969-42E7-436C-8DD3-C5ED18DD9209__TABLE_2C53060F15BF4F5394A1D2BBACD0BC71"><tbody><tr><td><b>Type</b></td><td><b>Source element and space adjacencies</b></td></tr><tr><td>_Shade_</td><td>No associated source element and no space adjacencies</td></tr><tr><td>_Air_</td><td>No associated source element and at least one space adjacency</td></tr><tr><td>_ExteriorWall_</td><td>Source element is a Wall or a Curtain Wall there is one space adjacency</td></tr><tr><td>_InteriorWall_</td><td>Source element is a Wall or a Curtain Wall and: there are two space adjacencies or the type Function parameter is set to "Interior" or "CoreShaft"</td></tr><tr><td>_UndergroundWall_</td><td>Source element is a Wall or a Curtain Wall and there is one space adjacency and if it is below grade</td></tr><tr><td>_SlabOnGrade_</td><td>Source element is a Floor and there is one space adjacency</td></tr><tr><td>_RaisedFloor_</td><td>Source element is a Floor and there is one space adjacency and it is above grade</td></tr><tr><td>_UndergroundSlab_</td><td>Source element is a Floor and there is one space adjacency and it is below grade</td></tr><tr><td>_InteriorFloor_</td><td>Source element is a Floor and: there are two space adjacencies or the type Function parameter is set to "Interior</td></tr><tr><td>_Roof_</td><td>Source element is a Roof or a Ceiling and there is one space adjacency</td></tr><tr><td>_UndergroundCeiling_</td><td>Source element is a Roof or a Ceiling and there is one space adjacency and it is below grade</td></tr><tr><td>_Ceiling_</td><td>Source element is a Roof or a Ceiling and there are two space adjacencies</td></tr></tbody></table>

### EnergyAnalysisOpening

From an EnergyAnalysisOpening you can retrieve the associated parent analytical surface element. The GetPolyloop() method returns the opening geometry as a planar polygon.

A number of properties are available to obtain information about the analytical opening, such as Height, Width, Corner and OpeningName. Similar as for analytical surfaces, the analytical opening type can be obtained as a simple EnergyAnalysisOpeningType enumeration or as a gbXMLOpeningType attribute. The type of the opening is based on the family category for the opening and in what element it is contained, as shown in the following table:

<table summary="" id="GUID-471B3969-42E7-436C-8DD3-C5ED18DD9209__TABLE_BE73E7D705664FEB8F56C30CE131CB3E"><tbody><tr><td><b>Type</b></td><td><b>Family Category or containing element</b></td></tr><tr><td><i>OperableWindow</i></td><td>Window</td></tr><tr><td><i>NonSlidingDoor</i></td><td>Door</td></tr><tr><td><i>FixedSkylight</i></td><td>Opening contained in a Roof</td></tr><tr><td><i>FixedWindow</i></td><td>Opening contained in a Curtain Wall Panel</td></tr><tr><td><i>Air</i></td><td>Opening of the category Openings</td></tr></tbody></table>
