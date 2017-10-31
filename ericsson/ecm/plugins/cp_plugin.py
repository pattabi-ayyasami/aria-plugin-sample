

def translate(**args):
    print "inside the ECM Plugin - Translate Connection Point"
    context = args.get("ctx")
    print "Type of context: ", type(context)
    print context

    node = context.node
    print "Node Class: ", type(node)
    print node

    node_template = context.node_template
    print "Node Template Class: ", type(node_template)

    print node.as_raw
    print node_template.as_raw



