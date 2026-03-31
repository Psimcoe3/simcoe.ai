---
created: 2026-01-28T21:09:54 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_Reinforcement_Rounding_html
author: 
---

# Help | Reinforcement Rounding | Autodesk

> ## Excerpt
> Reinforcement rounding is important for preparation of construction documents. You can use numerical rounding of rebar lengths to simplify organization and annotation when tagging, filtering, or scheduling rebar.

---
Reinforcement rounding is important for preparation of construction documents. You can use numerical rounding of rebar lengths to simplify organization and annotation when tagging, filtering, or scheduling rebar.

Revit enables overriding of three different reinforcement parameters: Fabric Sheet lengths, Rebar total lengths, and Rebar segment lengths. Rebar segment lengths are the individual segments which make up a rebar shape.

The application of Rebar and/or Fabric Sheet rounding is controlled initially at the Document level. If rounding is not enabled at the document level, the rounding for Reinforcement Length (structural unit settings) will be applied to rebar lengths in schedules and tags. If the Document level reinforcement settings are overridden then the rebar settings control rounding for rebars and fabric sheets and may be overridden further at the type and element level.

## Overriding reinforcement rounding settings

The ReinforcementSettings class provides methods to obtain either the fabric or rebar rounding managers by calling GetFabricRoundingManager() or GetRebarRoundingManager() respectively. These rounding managers represent the document level rounding overrides and will control rounding for any types or elements which are not otherwise overridden by accessing the corresponding rounding manager for the type or element in question.

Reinforcement rounding override is enabled by setting the ReinforcementRoundingManager.IsActiveOnElement property to true at the document level. This property must be set to true before attempting to override the reinforcement rounding settings for the document, a type, or an element.

The ReinforcementRoundingManager has two derived classes, FabricRoundingManager and RebarRoundingManager, to handle overrides for these different types of elements. FabricRoundingManager is used for managing reinforcement rounding override settings used by FabricSheetType and FabricSheet elements while RebarRoundingManager is used for managing reinforcement rounding override settings used by RebarBarTypes, Rebar and RebarInSystem elements.

To override reinforcement rounding settings for a rebar type, call Rebar.GetReinforcementRoundingManager() to get a reference to a RebarRoundingManager. Once you have access to the RebarRoundingManager, to override the rounding settings, first set RebarRoundingManager.IsActiveOnElement to true before attempting to set any of the rounding properties.

RebarRoundingManager.TotalLengthRounding is the rounding increment that will be used in rounding. (e.g., 1" means that the actual length will be rounded to an increment of 1") RebarRoundingManager.TotalLengthRoundingMethod takes a RoundingMethod enum which has the following possible values:

-   Nearest - Standard rounding: round to nearest
-   Up - Round up
-   Down - round down

RebarRoundingManager also provides access to the Segment length rounding with properties RebarRoundingManager.SegmentLengthRounding and RebarRoundingManager.SegmentLengthRoundingMethod.

To override reinforcement settings on a fabric sheet type or a fabric sheet element, calling GetReinforcementRoundingManager() on the corresponding class will return a FabricRoundingManager. The FabricRoundingManager class has similar functionality to the RebarRoundingManager for controlling rounding for fabric sheets.

## Querying an element's current reinforcement rounding settings

You may access information about what is currently controlling the reinforcement rounding for any element by querying the following properties: RebarRoundingManager.ApplicableReinforcementRoundingSource (for rebar) or FabricRoundingManager.ApplicableReinforcementRoundingSource (for fabric sheets). You may also query current rounding settings by using the ApplicableTotalLengthRoundingMethod and ApplicableTotalLengthRounding properties, available from both types of rounding managers .
