---
created: 2026-01-28T21:09:49 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_Reinforcement_Settings_html
author: 
---

# Help | Reinforcement Settings | Autodesk

> ## Excerpt
> Several settings regarding reinforcement in the model are controlled at the document level and are accessed through the ReinfocementSettings class for the document.

---
Several settings regarding reinforcement in the model are controlled at the document level and are accessed through the ReinfocementSettings class for the document.

These settings include reinforcement rounding document level overrides, hosting of rebar elements on path and area reinforcement, as well as tag abbreviations for reinforcement tagging.

Access the document reinforcement settings object by calling the static ReinforcementSettings.GetReinforcementSettings() which takes a reference to the document and returns the corresponding reinforcement settings object.

## Reinforcement rounding overrides

You may access settings for document level reinforcement rounding overrides by using the methods GetRebarRoundingManager() or GetFabricRoundingManager()

## Hosting rebar on area and path reinforcing

The property HostStructuralRebar controls whether Revit will automatically host real rebar on path and area reinforcement. Before setting this property to true, you must verify that there are no path or area reinforcing objects currently in the document by using a FilteredElementCollector.

## Include hooks in rebar shape definition

The RebarShapeDefinesHooks property controls whether rebar shape definitions include hooks in the definition. This maps to the UI property "Include hooks in Rebar Shape definition" setting in Reinforcement Settings. Note that this property may not be changed if the model contains: rebar elements, area or path reinforcing, or rebar containers. Use a FilteredElementCollector to query the model for the existence of any of these elements before attempting to set this property.

## Include end treatments in rebar shape definition

The RebarShapeDefinesEndTreatments property indicates if end treatments are defined by the RebarShape. This property can only be set if there are no rebars, area reinforcements or path reinforcements.

You may access as well as apply new rebar tag abbreviations. Engineers typically specify rebar with certain abbreviations (E.g., NF = near face, E.W. = each way). There are 16 different abbreviation tags stored by the ReinforcementSettings object and are indexed by the enumeration ReinforcementAbbreviationTagType.

Query current abbreviation tags by calling the method GetReinforcementAbbreviationTag() which will return a string value of the current abbreviation corresponding to the tag type passed to the method. You may also retrieve all of the abbreviation tags associated with either path or area reinforcement by calling the method GetReinforcementAbbreviationTags().

Set new abbreviations by calling the method SetReinforcementAbbreviationTag() passing a ReinforcementAbbreviationTagType to specify for which tag type you wish to set the new abbreviation.

## Varying Rebar Set

The NumberVaryingLengthRebarsIndividually property of ReinforcementSettings modifies the way varying length bars are numbered (individually or as a whole). If true, then each bar in a varying rebar set will be assigned a rebar number. Otherwise, the whole rebar set will be assigned a unique rebar number and each bar within the set will be assigned a suffix that is unique within the set.

The ReinforcementSettings.RebarVaryingLengthNumberSuffix property is a unique string identifier used for a bar within a variable length rebar set.
