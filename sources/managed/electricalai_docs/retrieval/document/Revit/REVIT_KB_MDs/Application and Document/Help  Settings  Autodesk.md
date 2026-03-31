---
created: 2026-01-28T20:42:55 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Settings | Autodesk

> ## Excerpt
> The following table identifies the commands in the Revit Platform UI Manage tab, and corresponding APIs.

---
The following table identifies the commands in the Revit Platform UI Manage tab, and corresponding APIs.

**Table 7: Settings in API and UI**

|  |  |  |
| --- | --- | --- |
| UI command | Associated API | Reference |
| Settings → Project Information | Document.ProjectInformation | See the following note |
| Settings → Project Parameters | Document.ParameterBindings (Only for Shared Parameter) | See [Shared Parameters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Shared_Parameters_html) |
| Project Location panel | Document.ProjectLocations Document.ActiveProjectLocation | [Place and Locations](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Place_and_Locations_html) |
| Settings → Additional Settings → Fill Patterns | FilteredElementCollector filtering on class FillPatternElement | See the following note |
| Settings → Materials | FilteredElementCollector filtering on class Material | See [Material Management](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Material_Material_Management_html) |
| Settings → Object Styles | Document.Settings.Categories | See the following note |
| Phasing → Phases | Document.Phases | See the following note |
| Settings → Structural Settings | Loads and related structural settings are available in the API | See [Structural Engineering](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_html) |
| Settings → Project Units | Document.GetUnits() | See [Units](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Application_and_Document_Units_html) |
| Area and Volume Calculations (on the Room & Area panel) | AreaVolumeSettings.GetAreaVolumeSettings() | See the following note |

Note: Project Information - The API provides the ProjectInfo class which is retrieved using Document.ProjectInformation to represent project information in the Revit project. The following table identifies the corresponding APIs for the Project Information parameters.

**Table 8: ProjectInformation**

<table summary="" id="GUID-24C1A8C9-03A3-4E6D-B3D9-258BE2A28A79__TABLE_6FEDAA922C3549BEBFBB037FC1C40BC9"><tbody><tr><td><b>Parameters</b></td><td><b>Corresponding API</b></td><td><b>Built-in Parameters</b></td></tr><tr><td>Project Issue Date</td><td>ProjectInfo.IssueDate</td><td>PROJECT_ISSUE_DATE</td></tr><tr><td>Project Status</td><td>ProjectInfo.Status</td><td>PROJECT_STATUS</td></tr><tr><td>Client Name</td><td>ProjectInfo.ClientName</td><td>CLIENT_NAME</td></tr><tr><td>Project Address</td><td>ProjectInfo.Address</td><td>PROJECT_ADDRESS</td></tr><tr><td>Project Name</td><td>ProjectInfo.Name</td><td>PROJECT_NAME</td></tr><tr><td>Project Number</td><td>ProjectInfo.Number</td><td>PROJECT_NUMBER</td></tr></tbody></table>

Use the properties exposed by ProjectInfo to retrieve and set all strings. These properties are implemented by the corresponding built-in parameters. You can get or set the values through built-in parameters directly. For more information about how to gain access to these parameters through the built-in parameters, see [Parameter](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Parameter_html) in the [Elements Essentials](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Elements_Essentials_html) section. The recommended way to get project information is to use the ProjectInfo properties.

-   Fill Patterns - Retrieve all Fill Patterns in the current document using a FilteredElementCollector filtering on class FillPatternElement. Specific FillPatterns can be retrieved using the static methods FillPatternElement.GetFillPattern(Document, ElementId) or FillPatternElement.GetFillPatternByName (Document, string).
-   Object Styles - Use Settings.Categories to retrieve all information in Category objects except for Line Style. For more details, see [Other Classifications](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Elements_Essentials_Other_Classifications_html) in the [Elements Essentials](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Elements_Essentials_html)and [Material](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Material_html) sections.
-   Phases - Revit maintains the element lifetime by phases, which are distinct time periods in the project lifecycle. All phases in a document are retrieved using the Document.Phases property. The property returns an array containing Phase class instances. However, the Revit API does not expose functions from the Phase class.
-   Options - The Options command configures project global settings. You can retrieve an Options.Application instance using the Application.Options property. Currently, the Options.Application class only supports access to library paths and shared parameters file.
-   Area and Volume Calculations - The AreaVolumeSettings class allows you to enable or disable volume calculations, and to change the room boundary location.
