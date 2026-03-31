---
created: 2026-01-28T21:09:45 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_Rebar_Containers_html
author: 
---

# Help | Rebar Containers | Autodesk

> ## Excerpt
> Rebar Containers are elements which represent an aggregation of rebars in one host. This element can only be created via the API.

---
Rebar Containers are elements which represent an aggregation of rebars in one host. This element can only be created via the API.

The advantages of using the RebarContainer element are:

-   Defining new types of rebar distributions not possible with the Revit user interface
-   Improve rebar performance by combining multiple rebar sets into the definition of a single element
-   The bars don’t react to the host’s geometry modifications

Each RebarContainer contains a collection (empty when first created) of RebarContainerItem objects. RebarContainerItem provides properties and methods similar to that of a Rebar element.

## Creating a new RebarContainer

You may use the static method RebarContainer.Create() which requires the Document in which you want to create a new RebarContainer, the host Element which will host the new RebarContainer and the ElementId of the RebarContainerType which will be assigned to the new RebarContainer.

The following example creates a new rebar container and specifies that any items in the container will be presented as subelements in schedules and tags.

<table summary="" id="GUID-AACF9518-D4B4-401D-933A-E1B7E619AE63__TABLE_0CDC6E31685E4EB2BDE96CA3BBAC7072"><tbody><tr><td><b>Code Region: Creating a rebar container</b></td></tr><tr><td><pre><code><span>RebarContainer</span><span> </span><span>CreateRebarContainer</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>FamilyInstance</span><span> beam</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Create a new rebar container</span><span>
    </span><span>ElementId</span><span> defaultRebarContainerTypeId </span><span>=</span><span> </span><span>RebarContainerType</span><span>.</span><span>CreateDefaultRebarContainerType</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>RebarContainer</span><span> container </span><span>=</span><span> </span><span>RebarContainer</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> beam</span><span>,</span><span> defaultRebarContainerTypeId</span><span>);</span><span>

    </span><span>// Any items for this container should be presented in schedules and tags as separate subelements</span><span>
    container</span><span>.</span><span>PresentItemsAsSubelements</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>

    </span><span>return</span><span> container</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Filling a RebarContainer

Once you have a new RebarContainer object, you can fill it up with RebarContainerItems by calling one of the following methods on the RebarContainer object:

-   AppendItemFromRebar() - Appends a RebarContainerItem to the collection using properties of the Rebar element used to create it.
-   AppendItemFromCurves() - Appends a RebarContainerItem to the collection from a list of curves using properties from the specified RebarBarType.
-   AppendItemFromRebarShape() - Appends a RebarContainerItem to the collection using properties from the specified RebarBarType and RebarShapeType.
-   AppendItemFromCurvesAndShape() - Appends a RebarContainerItem to the collection from a list of curves using properties from the specified RebarBarType and RebarShapeType. Note that in creating the container items, you will often be required to specify the normal of the plane in which the curves exist. This normal also defines the direction of multiple rebar creation if you set the layout rules to anything other than single. If you set the RebarContainerItem to a FixedNumber layout rule, for instance, those additional bars will be distributed along a line perpendicular to the plane you specify when creating the RebarContainerItem. In this sense the Normal also serves as the direction of distribution for RebarContainerItems with layout rules applied.

## Accessing RebarContainerItems

Use the method RebarContainer.Contains() to query whether the particular RebarContainerItem exists in the RebarContainer.

RebarContainer provides methods to remove individual items, clear all items, get specific items and return the count of RebarContainerItems in the container. The SetItemHiddenStatus() method controls whether specific items in the container are hidden in a specific view or not, and IsItemHidden() identifies if an items is hidden in a view.

<table summary="" id="GUID-AACF9518-D4B4-401D-933A-E1B7E619AE63__TABLE_D2975572CF144E9582C227C448096E39"><tbody><tr><td><b>Code Region: Adding items to a rebar container</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>AddItemsToRebarContainer</span><span>(</span><span>RebarContainer</span><span> container</span><span>,</span><span> </span><span>FamilyInstance</span><span> beam</span><span>,</span><span> </span><span>RebarBarType</span><span> barType</span><span>,</span><span> </span><span>RebarHookType</span><span> hookType</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Define the rebar geometry information - Line rebar</span><span>
    </span><span>LocationCurve</span><span> location </span><span>=</span><span> beam</span><span>.</span><span>Location</span><span> </span><span>as</span><span> </span><span>LocationCurve</span><span>;</span><span>
    XYZ origin </span><span>=</span><span> location</span><span>.</span><span>Curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>);</span><span>
    </span><span>// create rebar along the length of the beam</span><span>
    XYZ rebarLineEnd </span><span>=</span><span> location</span><span>.</span><span>Curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>);</span><span>
    </span><span>Line</span><span> line </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>origin</span><span>,</span><span> rebarLineEnd</span><span>);</span><span>
    XYZ normal </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>Curve</span><span> rebarLine </span><span>=</span><span> line</span><span>.</span><span>CreateOffset</span><span>(</span><span>0.5</span><span>,</span><span> normal</span><span>);</span><span>

    </span><span>// Create the line rebar</span><span>
    </span><span>IList</span><span>&lt;</span><span>Curve</span><span>&gt;</span><span> curves </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>Curve</span><span>&gt;();</span><span>
    curves</span><span>.</span><span>Add</span><span>(</span><span>rebarLine</span><span>);</span><span>

    </span><span>RebarContainerItem</span><span> item </span><span>=</span><span> container</span><span>.</span><span>AppendItemFromCurves</span><span>(</span><span>RebarStyle</span><span>.</span><span>Standard</span><span>,</span><span> barType</span><span>,</span><span> hookType</span><span>,</span><span> hookType</span><span>,</span><span> normal</span><span>,</span><span> curves</span><span>,</span><span> </span><span>RebarHookOrientation</span><span>.</span><span>Right</span><span>,</span><span> </span><span>RebarHookOrientation</span><span>.</span><span>Left</span><span>,</span><span> </span><span>true</span><span>,</span><span> </span><span>true</span><span>);</span><span>

    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> item</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// set specific layout for new rebar as fixed number, with 10 bars, distribution path length of 1.5'</span><span>
        </span><span>// with bars of the bar set on the same side of the rebar plane as indicated by normal</span><span>
        </span><span>// and both first and last bar in the set are shown</span><span>
        item</span><span>.</span><span>SetLayoutAsFixedNumber</span><span>(</span><span>10</span><span>,</span><span> </span><span>1.5</span><span>,</span><span> </span><span>true</span><span>,</span><span> </span><span>true</span><span>,</span><span> </span><span>true</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>// Hide the new item in the active view</span><span>
    container</span><span>.</span><span>SetItemHiddenStatus</span><span>(</span><span>container</span><span>.</span><span>Document</span><span>.</span><span>ActiveView</span><span>,</span><span> item</span><span>.</span><span>ItemIndex</span><span>,</span><span> </span><span>true</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## RebarContainerType

Rebar Containers will have types. These types are agnostic to the individual RebarContainerItems contained in them but will afford access to the Container's parameters at the type level. It is a required argument for creation of a new RebarContainer. Obtain a default by calling the static method RebarContainerType.CreateDefaultRebarContainerType() to obtain the ElementId of a RebarContainerType if the desired one does not exist in the database.

## RebarContainer parameters management

Because the RebarContainer may contain several different configurations of individual RebarContainerItems, the overall RebarContainer parameters will be derived from the contained RebarContainerItem members if possible. If the parameter exists on all RebarContainerItems and it is the same across all RebarContainerItems in the RebarContainer then the RebarContainer parameter will show this value. If they are different, or do not exist on all RebarContainerItems in the Container, the parameter will display without value.

To allow you to manage this and specify necessary parameters for the RebarContainer as a whole, you may request the RebarContainerParameterManager from the RebarContainer calling the method GetParametersManager() which will return an object you can use to override the parameters of the RebarContainer. As an example, TotalLength in a RebarContainer with multiple RebarContainerItems with differing lengths, will show an empty parameter for TotalLength. You can call the RebarContainerParametersManager method AddOverride() which has 4 overloads so that you can override the value of any of four value types of parameters (ElementId, Double, Integer, String). Use the method IsRebarContainerParameter() to determine if the parameter is a RebarContainer parameter before attempting to add an override for the parameter.

You can also add a shared parameter as an override to a RebarContainer by calling the method AddSharedParameterAsOverride() and passing in the id of the shared parameter. Check to see that the parameter has not already been added to the RebarContainer before calling this method.

You may remove overrides by calling the method RemoveOverride() or remove all overrides by calling ClearOverrides().

Individual overridden parameters may be set to be modifiable or read only by calling the methods SetOverriddenParameterModifiable() or SetOverriddenParameterReadonly() and query the same with the IsOverriddenParameterModifiable() method.

Lastly, to check if a RebarContainer parameter is overridden, call the method IsParameterOverridden() passing in the ElementId of the parameter in question.

<table summary="" id="GUID-AACF9518-D4B4-401D-933A-E1B7E619AE63__TABLE_3156988F75974323985FCE1D46FE02C5"><tbody><tr><td><b>Code Region: RebarContainer parameters management</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>ManageParameters</span><span>(</span><span>RebarContainer</span><span> container</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>RebarContainerParameterManager</span><span> paramManager </span><span>=</span><span> container</span><span>.</span><span>GetParametersManager</span><span>();</span><span>

    </span><span>Parameter</span><span> aParam </span><span>=</span><span> container</span><span>.</span><span>LookupParameter</span><span>(</span><span>"A"</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>aParam </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        paramManager</span><span>.</span><span>AddOverride</span><span>(</span><span>aParam</span><span>.</span><span>Id</span><span>,</span><span> </span><span>0.4</span><span>);</span><span>
        paramManager</span><span>.</span><span>SetOverriddenParameterModifiable</span><span>(</span><span>aParam</span><span>.</span><span>Id</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## RebarContainerItems

Rebar container items offer many of the same properties as do Rebar elements. They are a much lighter representation of a modeled rebar and unlike the Rebar class which is derived from Element, RebarContainerItem is derived from the IDisposable Interface.

You may redefine the RebarContainerItem represented by any RebarContainerItem by calling the class methods available on RebarContainerItem objects:

-   SetFromRebar()
-   SetFromCurves()
-   SetFromRebarShape()
-   SetFromCurvesAndShape() These methods mimic the methods which were used on RebarContainer to create the RebarContainerItem in the first place and have identical or nearly identical arguments which can be used to modify any RebarContainerItem in the RebarContainer.

You may query the RebarBarType ID with the class property BarTypeId. In order to apply a different RebarBarType to the RebarContainerItem you must use the SetFrom methods on the RebarContainerItem (i.e. SetFromCurves() or SetFromRebar()).
