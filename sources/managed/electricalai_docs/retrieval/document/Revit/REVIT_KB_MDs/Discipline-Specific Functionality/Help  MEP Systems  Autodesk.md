---
created: 2026-01-28T21:08:28 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_MEP_Systems_html
author: 
---

# Help | MEP Systems | Autodesk

> ## Excerpt
> MEPSystem is the base class for electrical, mechanical and piping systems in Revit MEP.

---
MEPSystem is the base class for electrical, mechanical and piping systems in Revit MEP.

ElectricalSystem, MechanicalSystem and PipingSystem all derive from the MEPSystem class. The base class has some common functionality across system types, such as adding elements to the system or finding the base panel or equipment of the system. A few methods in the base class only apply to HVAC and plumbing systems, such as the DivideSystem() method which divides the physical networks in the system and creates a new system for each network.

The derived classes have additional methods and properties specific to the system type.

## MEPSection

The MEPSystem class has a SectionsCount property which returns the number of sections for the system. An MEPSection object can be obtained using either the GetSectionByIndex() method or the GetSectionByNumber() method. Although these methods are in the base MEPSystem class, the MEPSection class represents duct and pipe sections and is mainly for pressure loss calculation. It is a series of connected elements (segments - ducts or pipes, fittings, terminals and accessories) which can be obtained from the GetElementIds() method. All section members should have same flow analysis properties: Flow, Size, Velocity, Friction and Roughness.

The segment length, pressure drop and loss coefficient for each element in the section can vary, so methods are available in MEPSection to get these values given a specific element id for an element in the section. The coefficient for ducts is the loss coefficient. For pipes this is the same as the friction factor.

## Calculations

Some properties of MEP systems are calculated by Revit. Both MechanicalSystem and PipingSystem have an IsWellConnected property which indicates if the system is well connected or not. If the system is not well connected, parameters which need to be calculated are invalid.

For mechanical and piping systems, some values are calculated based on properties of the sections of the system. The MEPSystem.GetCriticalPathSectionNumbers() method returns a list of the critical path section numbers in order of the direction of flow and PressureLossOfCriticalPath() gets the total pressure loss of the sections in the critical path.

The GetFlow() and GetStaticPressure() methods available from MechanicalSystem and PipingSystem get the flow and static pressure for the system.

PipingSystem has additional calculated properties: GetFixtureUnits() and GetVolume()

Note: Due to the way these calculated properties are handled internally by Revit, they do not support dynamic model update. However, other system properties that are not calculated do support dynamic model update.
