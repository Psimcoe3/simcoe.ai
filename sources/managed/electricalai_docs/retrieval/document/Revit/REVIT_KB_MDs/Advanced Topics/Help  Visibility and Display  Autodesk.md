---
created: 2026-01-28T21:20:21 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Worksharing_Visibility_and_Display_html
author: 
---

# Help | Visibility and Display | Autodesk

> ## Excerpt
> A workset’s visibility can be set for a particular view using View.SetWorksetVisibility(). The WorksetVisibility options are Visible (it will be visible if the workset is open), Hidden, and UseGlobalSetting (indicating not to override the setting for the view). The corresponding View.GetWorksetVisibility() method retrieves the current visibility settings for a workset in that view. However, this method does not consider whether the workset is currently open. To determine if a workset is visible in a View, including taking into account whether the workset is open or closed, use View.IsWorksetVisible().

---
## Visibility

A workset’s visibility can be set for a particular view using View.SetWorksetVisibility(). The WorksetVisibility options are Visible (it will be visible if the workset is open), Hidden, and UseGlobalSetting (indicating not to override the setting for the view). The corresponding View.GetWorksetVisibility() method retrieves the current visibility settings for a workset in that view. However, this method does not consider whether the workset is currently open. To determine if a workset is visible in a View, including taking into account whether the workset is open or closed, use View.IsWorksetVisible().

The class WorksetDefaultVisibilitySettings manages default visibility of worksets in a document. It is not available for family documents. If worksharing is disabled in a document, all elements are moved into a single workset; that workset, and any worksets (re)created if worksharing is re-enabled, is visible by default regardless of any current settings.

The following example hides a workset in a given view and hides it by default in other views.

<table summary="" id="GUID-F002C5C5-CDEF-437B-9250-984DF8C51860__TABLE_AE77CC75BFB1470DB482D427DF80149F"><tbody><tr><td><b>Code Region: Hide a Workset</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>HideWorkset</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>View</span><span> view</span><span>,</span><span> </span><span>WorksetId</span><span> worksetId</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// get the current visibility</span><span>
    </span><span>WorksetVisibility</span><span> visibility </span><span>=</span><span> view</span><span>.</span><span>GetWorksetVisibility</span><span>(</span><span>worksetId</span><span>);</span><span>

    </span><span>// and set it to 'Hidden' if it is not hidden yet</span><span>
    </span><span>if</span><span> </span><span>(</span><span>visibility </span><span>!=</span><span> </span><span>WorksetVisibility</span><span>.</span><span>Hidden</span><span>)</span><span>
    </span><span>{</span><span>
        view</span><span>.</span><span>SetWorksetVisibility</span><span>(</span><span>worksetId</span><span>,</span><span> </span><span>WorksetVisibility</span><span>.</span><span>Hidden</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>// Get the workset’s default visibility      </span><span>
    </span><span>WorksetDefaultVisibilitySettings</span><span> defaultVisibility </span><span>=</span><span> </span><span>WorksetDefaultVisibilitySettings</span><span>.</span><span>GetWorksetDefaultVisibilitySettings</span><span>(</span><span>doc</span><span>);</span><span>

    </span><span>// and making sure it is set to 'false'</span><span>
    </span><span>if</span><span> </span><span>(</span><span>true</span><span> </span><span>==</span><span> defaultVisibility</span><span>.</span><span>IsWorksetVisible</span><span>(</span><span>worksetId</span><span>))</span><span>
    </span><span>{</span><span>
        defaultVisibility</span><span>.</span><span>SetWorksetVisibility</span><span>(</span><span>worksetId</span><span>,</span><span> </span><span>false</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Display Modes

In addition to getting and setting information about the workset visibility, the View class also provides methods to access information on the worksharing display mode and settings. The WorksharingDisplayMode enumeration indicates which mode a view is in, if any:

<table summary="" id="GUID-F002C5C5-CDEF-437B-9250-984DF8C51860__TABLE_626E2FBB86D24496A52442096DE4266D"><tbody><tr><td><b>Member Name</b></td><td><b>Description</b></td></tr><tr><td><b>Off</b></td><td>No active worksharing display mode.</td></tr><tr><td><b>CheckoutStatus</b></td><td>The view is displaying the checkout status of elements.</td></tr><tr><td><b>Owners</b></td><td>The view is displaying the specific owners of elements.</td></tr><tr><td><b>ModelUpdates</b></td><td>The view is displaying model updates.</td></tr><tr><td><b>Worksets</b></td><td>The view is displaying which workset each element is assigned to.</td></tr></tbody></table>

<table summary="" id="GUID-F002C5C5-CDEF-437B-9250-984DF8C51860__TABLE_C842939754CF4799BCFD7C76042B5F46"><tbody><tr><td><b>Code Region: Activate different worksharing display modes</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Result</span><span> </span><span>Execute</span><span>(</span><span>ExternalCommandData</span><span> commandData</span><span>,</span><span> </span><span>ref</span><span> </span><span>string</span><span> message</span><span>,</span><span> </span><span>ElementSet</span><span> elements</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>View</span><span> activeView </span><span>=</span><span> commandData</span><span>.</span><span>View</span><span>;</span><span>
    </span><span>Document</span><span> doc </span><span>=</span><span> activeView</span><span>.</span><span>Document</span><span>;</span><span>

    </span><span>// Prepare settings</span><span>
    </span><span>Color</span><span> red </span><span>=</span><span> </span><span>new</span><span> </span><span>Color</span><span>(</span><span>0xFF</span><span>,</span><span> </span><span>0x00</span><span>,</span><span> </span><span>0x00</span><span>);</span><span>
    </span><span>WorksharingDisplayGraphicSettings</span><span> settingsToApply </span><span>=</span><span> </span><span>new</span><span> </span><span>WorksharingDisplayGraphicSettings</span><span>(</span><span>true</span><span>,</span><span> red</span><span>);</span><span>

    </span><span>// Toggle mode based on the current mode</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Toggle display mode"</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>

        </span><span>WorksharingDisplaySettings</span><span> settings </span><span>=</span><span> </span><span>WorksharingDisplaySettings</span><span>.</span><span>GetOrCreateWorksharingDisplaySettings</span><span>(</span><span>doc</span><span>);</span><span>

        </span><span>switch</span><span> </span><span>(</span><span>activeView</span><span>.</span><span>GetWorksharingDisplayMode</span><span>())</span><span>
        </span><span>{</span><span>
            </span><span>case</span><span> </span><span>WorksharingDisplayMode</span><span>.</span><span>Off</span><span>:</span><span>
                activeView</span><span>.</span><span>SetWorksharingDisplayMode</span><span>(</span><span>WorksharingDisplayMode</span><span>.</span><span>CheckoutStatus</span><span>);</span><span>
                settings</span><span>.</span><span>SetGraphicOverrides</span><span>(</span><span>CheckoutStatus</span><span>.</span><span>OwnedByOtherUser</span><span>,</span><span> settingsToApply</span><span>);</span><span>
                </span><span>break</span><span>;</span><span>
            </span><span>case</span><span> </span><span>WorksharingDisplayMode</span><span>.</span><span>CheckoutStatus</span><span>:</span><span>
                activeView</span><span>.</span><span>SetWorksharingDisplayMode</span><span>(</span><span>WorksharingDisplayMode</span><span>.</span><span>ModelUpdates</span><span>);</span><span>
                settings</span><span>.</span><span>SetGraphicOverrides</span><span>(</span><span>ModelUpdatesStatus</span><span>.</span><span>UpdatedInCentral</span><span>,</span><span> settingsToApply</span><span>);</span><span>
                </span><span>break</span><span>;</span><span>
            </span><span>case</span><span> </span><span>WorksharingDisplayMode</span><span>.</span><span>ModelUpdates</span><span>:</span><span>
                activeView</span><span>.</span><span>SetWorksharingDisplayMode</span><span>(</span><span>WorksharingDisplayMode</span><span>.</span><span>Owners</span><span>);</span><span>
                settings</span><span>.</span><span>SetGraphicOverrides</span><span>(</span><span>"Target user"</span><span>,</span><span> settingsToApply</span><span>);</span><span>
                </span><span>break</span><span>;</span><span>
            </span><span>case</span><span> </span><span>WorksharingDisplayMode</span><span>.</span><span>Owners</span><span>:</span><span>
                activeView</span><span>.</span><span>SetWorksharingDisplayMode</span><span>(</span><span>WorksharingDisplayMode</span><span>.</span><span>Worksets</span><span>);</span><span>
                settings</span><span>.</span><span>SetGraphicOverrides</span><span>(</span><span>doc</span><span>.</span><span>GetWorksetTable</span><span>().</span><span>GetActiveWorksetId</span><span>(),</span><span> settingsToApply</span><span>);</span><span>
                </span><span>break</span><span>;</span><span>
            </span><span>case</span><span> </span><span>WorksharingDisplayMode</span><span>.</span><span>Worksets</span><span>:</span><span>
                activeView</span><span>.</span><span>SetWorksharingDisplayMode</span><span>(</span><span>WorksharingDisplayMode</span><span>.</span><span>Off</span><span>);</span><span>
                </span><span>break</span><span>;</span><span>
        </span><span>}</span><span>

        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Graphics Settings

The WorksharingDisplaySettings class controls how elements will appear when they are displayed in any of the worksharing display modes. The colors stored in these settings are a common setting and are shared by all users in the model. Whether a given color is applied is specific to the current user and will not be shared by other users. Note that these settings are available even in models that are not workshared. This is to allow pre-configuring the display settings before enabling worksets so that they can be stored in template files.

<table summary="" id="GUID-F002C5C5-CDEF-437B-9250-984DF8C51860__TABLE_78E2B7D8D21C45C0ABE8E889FC02021A"><tbody><tr><td><b>Code Region: Worksharing Display Graphic Settings</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>WorksharingDisplayGraphicSettings</span><span> </span><span>GetWorksharingDisplaySettings</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>String</span><span> userName</span><span>,</span><span> </span><span>WorksetId</span><span> worksetId</span><span>,</span><span> </span><span>bool</span><span> ownedbyCurrentUser</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>WorksharingDisplayGraphicSettings</span><span> graphicSettings</span><span>;</span><span>

    </span><span>// get or create a WorksharingDisplaySettings current active document</span><span>
    </span><span>WorksharingDisplaySettings</span><span> displaySettings </span><span>=</span><span> </span><span>WorksharingDisplaySettings</span><span>.</span><span>GetOrCreateWorksharingDisplaySettings</span><span>(</span><span>doc</span><span>);</span><span>

    </span><span>// get graphic settings for a user, if specified</span><span>
    </span><span>if</span><span> </span><span>(!</span><span>String</span><span>.</span><span>IsNullOrEmpty</span><span>(</span><span>userName</span><span>))</span><span>
        graphicSettings </span><span>=</span><span> displaySettings</span><span>.</span><span>GetGraphicOverrides</span><span>(</span><span>userName</span><span>);</span><span>

     </span><span>// get graphicSettings for a workset, if specified</span><span>
    </span><span>else</span><span> </span><span>if</span><span> </span><span>(</span><span>worksetId </span><span>!=</span><span> </span><span>WorksetId</span><span>.</span><span>InvalidWorksetId</span><span>)</span><span>
        graphicSettings </span><span>=</span><span> displaySettings</span><span>.</span><span>GetGraphicOverrides</span><span>(</span><span>worksetId</span><span>);</span><span>

    </span><span>// get graphic settings for the OwnedByCurrentUser status</span><span>
    </span><span>else</span><span> </span><span>if</span><span> </span><span>(</span><span>ownedbyCurrentUser</span><span>)</span><span>
        graphicSettings </span><span>=</span><span> displaySettings</span><span>.</span><span>GetGraphicOverrides</span><span>(</span><span>CheckoutStatus</span><span>.</span><span>OwnedByCurrentUser</span><span>);</span><span>

    </span><span>// otherwise get graphic settings for the CurrentWithCentral status</span><span>
     </span><span>else</span><span>
          graphicSettings </span><span>=</span><span> displaySettings</span><span>.</span><span>GetGraphicOverrides</span><span>(</span><span>ModelUpdatesStatus</span><span>.</span><span>CurrentWithCentral</span><span>);</span><span>

     </span><span>return</span><span> graphicSettings</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The overloaded method WorksharingDisplaySettings.SetGraphicOverrides() sets the graphic overrides assigned to elements based on the given criteria.

<table summary="" id="GUID-F002C5C5-CDEF-437B-9250-984DF8C51860__TABLE_91FCA3F081244BB7A8B8530AE5D14092"><tbody><tr><td><b>Code Region: Graphic Overrides</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>SetWorksharingDisplaySettings</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>WorksetId</span><span> worksetId</span><span>,</span><span> </span><span>String</span><span> userName</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>String</span><span> message </span><span>=</span><span> </span><span>String</span><span>.</span><span>Empty</span><span>;</span><span>

    </span><span>// get or create a WorksharingDisplaySettings current active document</span><span>
    </span><span>WorksharingDisplaySettings</span><span> displaySettings </span><span>=</span><span> </span><span>WorksharingDisplaySettings</span><span>.</span><span>GetOrCreateWorksharingDisplaySettings</span><span>(</span><span>doc</span><span>);</span><span>

    </span><span>// set a new graphicSettings for CheckoutStatus - NotOwned</span><span>
    </span><span>WorksharingDisplayGraphicSettings</span><span> graphicSettings </span><span>=</span><span> </span><span>new</span><span> </span><span>WorksharingDisplayGraphicSettings</span><span>(</span><span>true</span><span>,</span><span> </span><span>new</span><span> </span><span>Color</span><span>(</span><span>255</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>));</span><span>
    displaySettings</span><span>.</span><span>SetGraphicOverrides</span><span>(</span><span>CheckoutStatus</span><span>.</span><span>NotOwned</span><span>,</span><span> graphicSettings</span><span>);</span><span>

    </span><span>// set a new graphicSettings for ModelUpdatesStatus - CurrentWithCentral</span><span>
    graphicSettings </span><span>=</span><span> </span><span>new</span><span> </span><span>WorksharingDisplayGraphicSettings</span><span>(</span><span>true</span><span>,</span><span> </span><span>new</span><span> </span><span>Color</span><span>(</span><span>128</span><span>,</span><span> </span><span>128</span><span>,</span><span> </span><span>0</span><span>));</span><span>
    displaySettings</span><span>.</span><span>SetGraphicOverrides</span><span>(</span><span>ModelUpdatesStatus</span><span>.</span><span>CurrentWithCentral</span><span>,</span><span> graphicSettings</span><span>);</span><span>

    </span><span>// set a new graphicSettings by a given userName</span><span>
    graphicSettings </span><span>=</span><span> </span><span>new</span><span> </span><span>WorksharingDisplayGraphicSettings</span><span>(</span><span>true</span><span>,</span><span> </span><span>new</span><span> </span><span>Color</span><span>(</span><span>0</span><span>,</span><span> </span><span>255</span><span>,</span><span> </span><span>0</span><span>));</span><span>
    displaySettings</span><span>.</span><span>SetGraphicOverrides</span><span>(</span><span>userName</span><span>,</span><span> graphicSettings</span><span>);</span><span>

    </span><span>// set a new graphicSettings by a given workset Id</span><span>
    graphicSettings </span><span>=</span><span> </span><span>new</span><span> </span><span>WorksharingDisplayGraphicSettings</span><span>(</span><span>true</span><span>,</span><span> </span><span>new</span><span> </span><span>Color</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>255</span><span>));</span><span>
    displaySettings</span><span>.</span><span>SetGraphicOverrides</span><span>(</span><span>worksetId</span><span>,</span><span> graphicSettings</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The WorksharingDisplaySettings class can also be used to control which users are listed in the displayed users for the document. The RemoveUsers() method removes users from the list of displayed users and permanently discards any customization of the graphics. Only users who do not own any elements in the document can be removed. The RestoreUsers() method adds removed users back to the list of displayed users and permits customization of the graphics for those users. Note that any restored users will be shown with default graphic overrides and any customizations that existed prior to removing the user will not be restored.

<table summary="" id="GUID-F002C5C5-CDEF-437B-9250-984DF8C51860__TABLE_2C78F82752EC4B40BC74159A3679941A"><tbody><tr><td><b>Code Region: Removing Users</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>RemoveAndRestoreUsers</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// get or create a WorksharingDisplaySettings current active document</span><span>
    </span><span>WorksharingDisplaySettings</span><span> displaySettings </span><span>=</span><span> </span><span>WorksharingDisplaySettings</span><span>.</span><span>GetOrCreateWorksharingDisplaySettings</span><span>(</span><span>doc</span><span>);</span><span>

    </span><span>// get all users with GraphicOverrides</span><span>
    </span><span>ICollection</span><span>&lt;string&gt;</span><span> users </span><span>=</span><span> displaySettings</span><span>.</span><span>GetAllUsersWithGraphicOverrides</span><span>();</span><span>

    </span><span>// remove the users from the display settings (they will not have graphic overrides anymore)</span><span>
    </span><span>ICollection</span><span>&lt;string&gt;</span><span> outUserList</span><span>;</span><span>
    displaySettings</span><span>.</span><span>RemoveUsers</span><span>(</span><span>doc</span><span>,</span><span> users</span><span>,</span><span> </span><span>out</span><span> outUserList</span><span>);</span><span>

    </span><span>// show the current list of removed users</span><span>
    </span><span>ICollection</span><span>&lt;string&gt;</span><span> removedUsers </span><span>=</span><span> displaySettings</span><span>.</span><span>GetRemovedUsers</span><span>();</span><span>

    </span><span>String</span><span> message </span><span>=</span><span> </span><span>"Current list of removed users: "</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>removedUsers</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>0</span><span> </span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>String</span><span> user </span><span>in</span><span> removedUsers</span><span>)</span><span>
        </span><span>{</span><span>
           message </span><span>+=</span><span> </span><span>"\n"</span><span> </span><span>+</span><span> user</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        message </span><span>=</span><span> </span><span>"[Empty]"</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Users Removed"</span><span>,</span><span> message</span><span>);</span><span>

    </span><span>// restore the previously removed users</span><span>
    </span><span>int</span><span> number </span><span>=</span><span> displaySettings</span><span>.</span><span>RestoreUsers</span><span>(</span><span>outUserList</span><span>);</span><span>

    </span><span>// again, show the current list of removed users</span><span>
    </span><span>// it should not contain the users that were restored</span><span>
    removedUsers </span><span>=</span><span> displaySettings</span><span>.</span><span>GetRemovedUsers</span><span>();</span><span>

    message </span><span>=</span><span> </span><span>"Current list of removed users: "</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>removedUsers</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>0</span><span> </span><span>)</span><span>
    </span><span>{</span><span>
       </span><span>foreach</span><span> </span><span>(</span><span>String</span><span> user </span><span>in</span><span> removedUsers</span><span>)</span><span>
        </span><span>{</span><span>
           message </span><span>+=</span><span> </span><span>"\n"</span><span> </span><span>+</span><span> user</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        message </span><span>=</span><span> </span><span>"[Empty]"</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Removed Users Restored"</span><span>,</span><span> message</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
