---
created: 2026-01-28T21:05:19 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_Thermal_Properties_html
author: 
---

# Help | Thermal Properties | Autodesk

> ## Excerpt
> Certain assembly types such as Wall, Floor, Ceiling, Roof and Building Pad have calculated and settable thermal properties which are represented by the ThermalProperties class.

---
Certain assembly types such as Wall, Floor, Ceiling, Roof and Building Pad have calculated and settable thermal properties which are represented by the ThermalProperties class.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/ThermalProperties-76171.jpg)The ThermalProperties class has properties for the values shown above. Absorptance and Roughness are modifiable while HeatTransferCoefficient, ThermalResistance, and ThermalMass are read-only. The units for these calculated values are shown in the table below.

<table summary="" id="GUID-3039C4C4-B35C-4EFA-B93E-99833E12444D__TABLE_FB19236D5E804DC38F27F878579F1DAF"><tbody><tr><td><b>Property</b></td><td><b>Unit</b></td></tr><tr><td>HeatTransferCoefficient</td><td>watts per meter-squared kelvin<p>(W/(m^2*K)</p></td></tr><tr><td>ThermalResistance</td><td>meter-squared kelvin per watt<p>((m^2*K)/Watt)</p></td></tr><tr><td>ThermalMass</td><td>kilogram feet-squared per second squared kelvin<p>(kg ft^2/(s^2 K))</p></td></tr></tbody></table>

Thermal properties can be retrieved using the ThermalProperties property on the following types:

-   WallType
-   FloorType
-   CeilingType
-   RoofType
-   BuildingPadType
