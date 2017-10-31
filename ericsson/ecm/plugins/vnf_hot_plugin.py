
cache = {}

def translate(**args):
    print "inside the ECM Plugin - Translate VNF HOT Node Instance"
    for a in args:
        print a, args[a]

    context = args.get("ctx")
    print "Type of context: ", type(context)
    print context

    node = context.node

    node_template = context.node_template
    print "Node Class: ", node.__class__.__name__
    print "Node Template Class: ", type(node_template)

    node_info = node.as_raw
    print node_info

    node_template_info = node_template.as_raw
    print node_template_info

    attributes = context.node.attributes
    for k,v in attributes.iteritems():
        print k
        print type(v)
        print v

    print attributes.get("nso_payload_data").value
    args.get("ctx").node.attributes.get("nso_payload_data").value = "nso_payload"

    #context.node.attributes["nso_payload_data"] = "nso_payload"

    #print node.attributes(type(node))
    #context.node.get("attributes")["name"] = "Hello World"
    #print context.node.attributes

def deploy(**kwargs):
    print "inside the ECM Plugin - Deploy VNF HOT Node Instance"
    for k in kwargs:
        print k, kwargs[k]
