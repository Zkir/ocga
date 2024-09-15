"""
OCGA/PY rules example
Gorky Park Rotunda
(c) Zkir 2020
"""

def checkRulesMy(ctx):
    if ctx.getTag("building") != "":
        if ctx.scope_sz() == 0:
            height =  ctx.scope_sx()*1.3
            ctx.tag("height", height)
        ctx.massModel("mass_model")

    if ctx.getTag("building:part") == "mass_model":

        ctx.tag("building:colour", "#B0B0B0")
        ctx.tag("building:material", "plaster")

        ctx.split_z_preserve_roof(( ("~5", "roof"),
                                    ("~0.3", "cornice"),
                                    ("~1.5", "entablement"),
                                    ("~9.2", "collonade"),
                                    ("0.6","stilobate")))

    if ctx.getTag("building:part") == "stilobate":
        ctx.tag("roof:colour", "#101010")
        ctx.tag("roof:material", "stone")
        ctx.tag("building:colour", "#202020")
        ctx.tag("building:material", "stone")

    if ctx.getTag("building:part") == "roof":
        ctx.scale("'0.9", "'0.9")
        ctx.tag("roof:colour", "brown")
        ctx.tag("roof:material", "metal")
        ctx.tag("building:colour", "brown")
        ctx.tag("building:material", "metal")
        ctx.split_z_preserve_roof((("~0.3", "roof4"),
                                   ("~2.5", "dome"),
                                   ("~0.5", "roof2"),
                                   ("~0.9", "roof1")))

    # if ctx.getTag("building:part") == "stilobate1":
    #     pass
    #
    # if ctx.getTag("building:part") == "stilobate2":
    #     ctx.scale("'0.9","'0.9")
    #
    # if ctx.getTag("building:part") == "stilobate3":
    #     ctx.scale("'0.8","'0.8")

    if ctx.getTag("building:part") == "collonade":
        ctx.scale("'0.9", "'0.9")
        ctx.comp_border(ctx.current_object.size/8, "column_pre")

    if ctx.getTag("building:part") == "entablement":
        ctx.scale("'0.9", "'0.9")

    if ctx.getTag("building:part") == "cornice":
        ctx.scale("'1","'1")

    if ctx.getTag("building:part") == "roof1":
        pass

    if ctx.getTag("building:part") == "roof2":
        ctx.scale("'0.9","'0.9")

    if ctx.getTag("building:part") == "dome":
        ctx.scale("'0.8","'0.8")
        roof_height = ctx.getTag("height")-ctx.getTag("min_height")-0.01
        ctx.tag("roof:shape", "dome")
        ctx.tag("roof:height", roof_height)

    if ctx.getTag("building:part") == "roof4":
        ctx.scale("'0.25","'0.25","'2")
        ctx.translate(0,0,"'-0.5")

    if ctx.getTag("building:part") == "column_pre":
        ctx.translate("0","'-0.1")
        ctx.scale(ctx.scope_sy(),"'1")
        ctx.scale("'1.2", "'1.2")
        if ctx.current_object.split_index%2 == 0:
            ctx.split_z_preserve_roof(((ctx.scope_sx()/6,"column_top1"),("~1", "column_trunk_pre")))
        else:
            ctx.nil()

    if ctx.getTag("building:part") == "column_trunk_pre":
        ctx.primitive_cylinder("'1")
        ctx.split_z_preserve_roof(((ctx.scope_sx() / 10, "column_top2"),("~1", "column_trunk")))

    if ctx.getTag("building:part") == "column_trunk":
        ctx.scale("'0.8","'0.8")