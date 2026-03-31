---
created: 2026-01-28T21:08:54 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_Electrical_Settings_html
author: 
---

# Help | Electrical Settings | Autodesk

> ## Excerpt
> Some of the settings available on the Manage tab under MEP Settings - Electrical Settings are also available through the Revit API.

---
Some of the settings available on the Manage tab under MEP Settings - Electrical Settings are also available through the Revit API.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/ElectricalSettings.png)

## Electrical Settings

The ElectricalSetting class provides access to different electrical settings, such as fitting angles, wire types, and voltage types. There is one ElectricalSetting object per document and it is accessible through the static method ElectricalSetting.GetElectricalSettings().

### General Settings

The following general settings are available as properties of the ElectricalSetting class:

-   CircuitSequence - Accesses the circuit sequence numbering schema
-   CircuitNamePhaseA - Accesses the circuit naming by phase (Phase A Label).
-   CircuitNamePhaseB - Accesses the circuit naming by phase (Phase B Label).
-   CircuitNamePhaseC - Accesses the circuit naming by phase (Phase C Label).
    
    ### Fitting Angles
    

Fitting angle settings for cable trays and conduits are available from the following methods of the ElectricalSetting class:

-   GetSpecificFittingAngles()
-   GetSpecificFittingAngleStatus()
-   SetSpecificFittingAngleStatus()

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/ElectricalAnglesSettings.png)

**Fitting Angles**

### Other Electrical Settings

Properties of the ElectricalSetting class provide access to:

-   Distribution System Types
-   Voltage Types
-   Wire Conduit Types
-   Wire Material Types
-   Wire Types

Methods also are available to add or remove from the project distribution system types, voltate types, wire material types and wire types.

## Circuit Naming

`Autodesk.Revit.DB.Electrical.CircuitNamingScheme` represents a scheme used for electrical circuit naming. Significant methods on this class allow schemes to be created and allowing access to the list of combined parameters associated with the scheme:

-   CircuitNamingScheme.Create()
-   CircuitNamingScheme.GetCombinedParameters()
-   CircuitNamingScheme.SetCombinedParameters()

`Autodesk.Revit.DB.Electrical.CircuitNamingSchemeSettings` represents the circuit naming scheme settings object in a project document. Members on this class include:

-   CircuitNamingSchemeSettings.GetCircuitNamingSchemeSettings()
-   CircuitNamingSchemeSettings.CircuitNamingSchemeId
