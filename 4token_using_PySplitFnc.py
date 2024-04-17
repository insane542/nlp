text = """This tool is in beta stage. Alexa developers can use Get Metrics API to seamlessly
analyse metrics. It also supports custom skill models, prebuilt Flash Briefing models, and the 
Smart Home Skill API. You can use this tool for creation of monitors, alarms, and dashboards 
that spotlight changes. The release of these three tools will enable developers to create visually 
rich skills for Alexa devices with screens. Amazon describes these tools as a collection of 
tech and tools for creating visually rich and interactive voice experiences."""
data = text.split('.')
for i in data:
    print(i)
