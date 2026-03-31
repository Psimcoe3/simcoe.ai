---
created: 2026-01-28T21:08:50 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_Electrical_Analysis_for_Preliminary_Design_html
author: 
---

# Help | Electrical Analysis for Preliminary Design | Autodesk

> ## Excerpt
> Electrical engineers can estimate the building load throughout the distribution system without placing physical electrical families in the model, enabling conceptual analysis and planning.

---
Electrical engineers can estimate the building load throughout the distribution system without placing physical electrical families in the model, enabling conceptual analysis and planning.

## Overview

-   Create area-based load boundary lines based on one or more lines and a specified level using `CurveElement.CreateAreaBasedLoadBoundaryLine` or `CurveElement.CreateAreaBasedLoadBoundaryLines`
-   For a given level and phase, check if there are any empty plan circuits that do not have electrical load areas with `ElectricalLoadAreaData.HasCircuitsWithoutElectricalLoadAreas`
    -   If this returns true, create electrical load areas on all the empty plan circuits of the given level using `ElectricalLoadAreaData.CreateElectricalLoadAreas`
-   Because electrical load areas are special kind of `SpatialElement`, you can find all existing and any newly created ones using a `FilteredElementCollector`
-   Finally, create Area Based Loads by creating a Zone with `Zone.CreateAreaBasedLoad` and a `AreaBasedLoadData` then add the Electrical Load Area to the AreaBasedLoadData. Note that one Load Area can be included by more than one Area Based Loads - for example Area Based Load 1 can include Load Area X and Area Based Load 2 can also include Load Area X.

```
public void CreateAreaBasedElectricalLoads(Document doc, List<Curve> lines, Level level, Phase phase)
{
    IEnumerable<SpatialElement> electricalLoadAreas;
    using (Transaction transaction = new Transaction(doc, "Create Electrical Load Areas"))
    {
        transaction.Start();
        //Create Area Based Load Boundary Lines.
        CurveElement.CreateAreaBasedLoadBoundaryLines(doc, lines, level.Id);

        if (ElectricalLoadAreaData.HasCircuitsWithoutElectricalLoadAreas(doc, level.Id, phase.Id))
        {
            //Create Electrical Load Areas.
            ISet<ElementId> createdElectricalLoadAreaIds = ElectricalLoadAreaData.CreateElectricalLoadAreas(doc, level.Id, phase.Id);
        }

        electricalLoadAreas = new FilteredElementCollector(doc)
                .OfClass(typeof(SpatialElement))
                .WherePasses(new ElementLevelFilter(level.Id))
                .WherePasses(new ElementPhaseStatusFilter(phase.Id, ElementOnPhaseStatus.None))
                .Cast<SpatialElement>()
                .Where(x => x.SpatialElementType == SpatialElementType.ElectricalLoadArea);

        transaction.Commit();
    }

    using (Transaction transaction = new Transaction(doc, "Create Area Based Loads"))
    {
        transaction.Start();

        //Create Area Based Load on each Load Area.
        foreach (SpatialElement electricalLoadArea in electricalLoadAreas)
        {
            Zone areaBasedLoad = Zone.CreateAreaBasedLoad(doc, "AreaBasedLoad1", level.Id, phase.Id);
            AreaBasedLoadData areaBasedLoadData = areaBasedLoad.GetDomainData() as AreaBasedLoadData;
            areaBasedLoadData.AddElectricalLoadArea(electricalLoadArea.Id);
            areaBasedLoadData.Voltage = UnitUtils.ConvertToInternalUnits(100, UnitTypeId.Volts);
        }
        transaction.Commit();
    }
}
```

## Defining Electrical Analytical Loads

When defining loads, you can define area-based loads and equipment loads.

Area-based loads let you define a closed region and indicate power requirements based on power/area density. For example, lighting in 2nd floor office spaces is 2w/ft2, while lighting in conference rooms is 3w/ft2, and general power across the entire floor is 3.5 w/ft2.

An Area Based Load is composed by one or more Electrical Load Areas. One Electrical Load Area can be included by more than one Area Based Loads. Geometrically, an Electrical Load Area is a minimized enclosed region surrounded by area-based load boundary lines. In the Revit API, Electrical Load Area elements are represented as SpatialElement objects with their property SpatialElementType = ElectricalLoadArea. The SpatialElement.GetSpatialElementDomainData() method gets the SpatialElementDomainData for a given spatial element, and then down-casts it as ElectricalLoadAreaData to GetAreaBasedLoadIds() of it.

The Electrical Load Area elements can be created by `CreateElectricalLoadAreas()`. This function creates electrical load areas on all the empty plan circuits of the given level.

Equipment loads allow you to capture load requirements associated with major equipment components, such as elevators, chillers, or any other component beyond the general power density-based loads.

Equipment load elements can be created by ElectricalAnalyticalNode.Create() with the parameter ElectricalAnalyticalNodeType as EquipmentLoad. The `AnalyticalEquipmentLoadData` class provides access to this data.

When defining the distribution system, you can create Electrical Analytical Equipment (busses, transformers, transfer switches, and power sources), and interconnect these components. You can then associate area and equipment loads with the distribution system components to sum load throughout the distribution system.

## Electrical Analytical Nodes

The ElectricalAnalyticalNode class represents an electrical analytical node under the Analytical Power Distribution in the System Browser. The type of this node can be any of the value of the ElectricalAnalyticalNodeType enum:

-   Power Source
-   Bus
-   Transformer
-   Transfer Switch
-   Equipment Load

The static method ElectricalAnalyticalNode.Create is used to create these nodes.
