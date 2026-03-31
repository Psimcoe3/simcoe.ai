[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UIDocument Members

---



|  |
| --- |
| [UIDocument Class](295b48c8-0571-ad5c-eead-baea84a6787c.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [UIDocument](295b48c8-0571-ad5c-eead-baea84a6787c.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [UIDocument](cd1de090-0a23-96d9-cfe5-e5edddf9839f.htm) | Use a database level Document to construct a UI-level Document. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CanPlaceElementType](d9264f5e-333d-73df-0f9a-02b4c0722206.htm) | Verifies that the user can be prompted to place the input element type interactively. |
| Public method | [Dispose](47d89c68-0225-a534-5ace-b252cf90bfd7.htm) | Releases all resources used by the  [UIDocument](295b48c8-0571-ad5c-eead-baea84a6787c.htm) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | [GetOpenUIViews](1ac8b262-9085-07e9-cef6-85377e8c70f3.htm) | Get a list of all open view windows in the Revit user interface. |
| Public method | [GetPlacementTypes](3069f4c9-3caa-7a3f-f739-375482380805.htm) | Get a collection of valid placement types for input family symbol. |
| Public method Static member | [GetRevitUIFamilyLoadOptions](8475fa65-390b-f227-baa8-24db9b632506.htm) | Return the option object that allows you to use Revit's dialog boxes to let the user respond to questions that arise during loading of families. |
| Public method | [GetSketchGalleryOptions](3324ef29-2fd8-1760-f47a-030f5e2ccb2f.htm) | Gets the valid sketch gallery options of a family symbol. |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [PostRequestForElementTypePlacement](f9bf4ed3-0354-6bc1-6db3-e34fcbace950.htm) | Places a request on Revit's command queue for the user to place instances of the specified ElementType. This does not execute immediately, but instead when control returns to Revit from the current API context. |
| Public method | [PromptForFamilyInstancePlacement(FamilySymbol)](33d1a534-161c-6b25-7336-caf753c69b78.htm) | Prompts the user to place instances of the specified FamilySymbol. |
| Public method | [PromptForFamilyInstancePlacement(FamilySymbol, PromptForFamilyInstancePlacementOptions)](619d8d3f-ac64-26bf-cd82-0f6c37221367.htm) | Prompts the user to place instances of the specified FamilySymbol. |
| Public method | [PromptToMatchElementType](48e7741b-970c-8ee7-5987-914ca6e2f321.htm) | Prompts the user to select elements to change them to the input type. |
| Public method | [PromptToPlaceElementTypeOnLegendView](f9f2c603-2a3d-f333-42ea-fecfad359c6f.htm) | Prompts the user to place an element type onto a legend view. |
| Public method | [PromptToPlaceViewOnSheet](32a59cc7-1e27-35b4-2dc3-2892f14dd760.htm) | Prompts the user to place a specified view onto a sheet. |
| Public method | [RefreshActiveView](5d9f248c-a1be-ac2e-1f4c-2219ed0fc5ae.htm) | Refresh the display of the active view in the active document. |
| Public method | [RequestViewChange](a2e920d4-2849-282e-c25f-40a4d2cbef2d.htm) | Requests an asynchronous change of the active view in the currently active document. |
| Public method | [SaveAndClose](b7a3b928-bca9-d060-72b6-d7feaa2e8439.htm) | Close the document, prompting the user for saving it when necessary. |
| Public method | [SaveAs](32b06707-cfd5-837c-9951-791fd50a6bc9.htm) | Saves the document to a file name obtained from the Revit user without prompting the user to overwrite file if it exists. |
| Public method | [SaveAs(UISaveAsOptions)](7a5b49c3-f01d-9105-3b36-e04bea72887f.htm) | Saves the document to a file name obtained from the Revit user optionally prompting the user to overwrite file if it exists. |
| Public method | [ShowElements(Element)](6c40c35b-1b2b-1741-dafa-5ab6b1744634.htm) | Shows the element by zoom to fit. |
| Public method | [ShowElements(ElementId)](4a60dd3d-3c60-9298-2252-b5e263c35e4c.htm) | Shows the element by zoom to fit. |
| Public method | [ShowElements(ICollection ElementId )](4c3aaa9a-679a-b49a-f162-48e199cc5b4b.htm) | Shows the elements by zoom to fit. |
| Public method | [ShowElements(ElementSet)](97a4f04c-5e3e-b2d5-f15c-d802bafd0dc3.htm) | Shows the elements by zoom to fit. |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |
| Public method | [UpdateAllOpenViews](5cc3231e-ee7e-e1fc-2bd6-d164da617954.htm) | Update all open views in this document after elements have been changed, deleted, selected or de-selected. Graphics in the views are fully redrawn regardless of which elements have changed. |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ActiveGraphicalView](db91f0b0-7197-4a4d-91c8-43d1b9d549f2.htm) | The currently active graphical view of the currently active document. |
| Public property | [ActiveView](b6adb74b-39af-9213-c37b-f54db76b75a3.htm) | The currently active view of the currently active document. |
| Public property | [Application](afecfdc0-04cd-47d5-ddd5-e94b41d8555b.htm) | Retrieves an object that represents the current Application. |
| Public property | [Document](b2ec237a-74c9-d0ed-c192-65186d2d434e.htm) | Returns the database level document represented by this UI-level document. |
| Public property | [IsValidObject](2163a816-a155-c469-28ba-e40bd8a4d84d.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [Selection](4f5f9d48-c094-4aa6-ce7c-7d347a567244.htm) | Retrieve the currently selected Elements in Autodesk Revit. |

# See Also

[UIDocument Class](295b48c8-0571-ad5c-eead-baea84a6787c.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)