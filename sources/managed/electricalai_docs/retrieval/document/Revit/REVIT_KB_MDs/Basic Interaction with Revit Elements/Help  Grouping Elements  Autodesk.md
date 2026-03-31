---
created: 2026-01-28T20:51:02 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Grouping_Elements_html
author: 
---

# Help | Grouping Elements | Autodesk

> ## Excerpt
> The Revit Platform API uses the Creation.Document.NewGroup() method to select an element or multiple elements or groups and then combines them. With each instance of a group that you place, there is associatively among them. For example, you create a group with a bed, walls, and window and then place multiple instances of the group in your project. If you modify a wall in one group, it changes for all instances of that group. This makes modifying your building model much easier because you can change several instances of a group in one operation.

---
The Revit Platform API uses the Creation.Document.NewGroup() method to select an element or multiple elements or groups and then combines them. With each instance of a group that you place, there is associatively among them. For example, you create a group with a bed, walls, and window and then place multiple instances of the group in your project. If you modify a wall in one group, it changes for all instances of that group. This makes modifying your building model much easier because you can change several instances of a group in one operation.

<table summary="" id="GUID-1A0E4AB2-86B2-40C4-A11C-48636284FCE4__TABLE_7A648D1F5F024144B570518E4D82A45A"><tbody><tr><td><b>Code Region 10-9: Creating a Group</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>MakeGroup</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Group</span><span> </span><span>group</span><span> </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>UIDocument</span><span> uidoc </span><span>=</span><span> </span><span>new</span><span> </span><span>UIDocument</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> selectedIds </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>();</span><span>

    </span><span>if</span><span> </span><span>(</span><span>selectedIds</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Group all selected elements</span><span>
        </span><span>group</span><span> </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewGroup</span><span>(</span><span>selectedIds</span><span>);</span><span>
        </span><span>// Initially, the group has a generic name, such as Group 1\. It can be modified by changing the name of the group type as follows:</span><span>
        </span><span>// Change the default group name to a new name "MyGroup"</span><span>
        </span><span>group</span><span>.</span><span>GroupType</span><span>.</span><span>Name</span><span> </span><span>=</span><span> </span><span>"MyGroup"</span><span>;</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

There are three types of groups in Revit; Model Group, Detail Group, and Attached Detail Group. All are created using the NewGroup() method. The created Group's type depends on the Elements passed.

-   If no detail Element is passed, a Model Group is created.
-   If all Elements are detail elements, then a Detail Group is created.
-   If both types of Elements are included, a Model Group that contains an Attached Detail Group is created and returned.

Note: When elements are grouped, they can be deleted from the project.

-   When a model element in a model group is deleted, it is still visible when the mouse cursor hovers over or clicks the group, even if the application returns Succeeded to the UI. In fact, the model element is deleted and you cannot select or access that element.
-   When the last member of a group instance is deleted, excluded, or removed from the project, the model group instance is deleted.

When elements are grouped, they cannot be moved or rotated. If you perform these operations on the grouped elements, nothing happens to the elements, though the Move() or Rotate() method returns true.

You cannot group dimensions and tags without grouping the elements they reference. If you do, the API call will fail.

You can group dimensions and tags that refer to model elements in a model group. The dimensions and tags are added to an attached detail group. The attached detail group cannot be moved, copied, rotated, arrayed, or mirrored without doing the same to the parent group.

## Attached Detail Groups

To determine if a group is an attached detail group, use the `Group.IsAttached` property. To find the group to which a detail group is attached, use the `Group.AttachedParentId` property.

If a Model Group has attached detail groups, the visibility of these detail groups can be controlled with:

-   Group.ShowAttachedDetailGroups()
-   Group.ShowAllAttachedDetailGroups()
-   Group.HideAttachedDetailGroups()
-   Group.HideAllAttachedDetailGroups()

The attached detail groups available for a group or group type can be found with:

-   Group.GetAvailableAttachedDetailGroupTypeIds()
-   GroupType.GetAvailableAttachedDetailGroupTypeIds()

`Group.IsCompatibleAttachedDetailGroupType()` checks if the orientation of an attached detail group matches the orientation of a view. To prevent displaying detail groups in the wrong view, verify that the OwnerViewId of a detail group matches the view in which you are trying to display it.
